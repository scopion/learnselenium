# -*- coding:utf-8 -*-
# @File    : multi_login_paypal.py

import os
import time
import queue
import urllib3
import requests
import multiprocessing
from single_login_paypal import login_paypal
import Config

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def make_task(task_queue):
    # 读取本地的任务文件，放到queue中

    if os.path.exists(Config.TASK_FILE):
        with open(Config.TASK_FILE, 'r') as fd:
            for line in fd:
                task = line.strip("\n")
                print("上传任务到队列:{}".format(task))
                task_queue.put(task)

def proxy_ip(proxy_queue):
    proxy_pool = set()

    if Config.proxy_url:
        # 尝试从这个URL读取proxy地址
        r = requests.get(Config.proxy_url)

        if r.status_code == 200:
            for line in r.text.split("\n"):
                line = line.strip()
                proxy_pool.add(line)
        else:
            raise IOError("获取代理的URL:{}无效".format(Config.refresh_url))
    elif os.path.exists(Config.proxy_file):
        # 本地是否有提供代理地址文件
        with open(Config.proxy_file,'r') as fd:
            for line in fd:
                proxy_ip = line.strip("\n")
                proxy_pool.add(proxy_ip)
    else:
        raise ValueError("没有找到可用的代理")

    if proxy_pool:
        for line in proxy_pool:
            proxy_queue.put(line)

def main(task_queue,proxy_queue=None):
    # 多进程并行
    start_time =time.time()

    MAX_PROCESS = (os.cpu_count() or 1) * Config.TIMES_CPU
    pool = multiprocessing.Pool(processes=MAX_PROCESS)

    while True:
        try:
            task = task_queue.get(block=True, timeout=5)
            email, password = tuple(task.split(":"))

            if proxy_queue:
                proxy_ip = proxy_queue.get(block=True, timeout=5)
                pool.apply_async(login_paypal, (email, password, proxy_ip, True))
                # print(email, " ", password, " ", proxy_ip)
            else:
                pool.apply_async(login_paypal, (email, password))
        except queue.Empty:
            break

    pool.close()
    pool.join()

    end_time = time.time() # 通过运行时间，了解下性能

    print(end_time-start_time)
    print("Done")

if __name__ == '__main__':
    task_queue = queue.Queue()
    proxy_queue = queue.Queue()

    make_task(task_queue)
    proxy_ip(proxy_queue)

    main(task_queue,proxy_queue)
