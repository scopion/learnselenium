# -*- coding:utf-8 -*-
# @File    : single_login_paypal.py

import time
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

from browser import browser
import Config
import utils

def login_paypal(email,password,proxy_ip=None,save_to_db=False,country="zh"):

    login_info = Config.CountryDict.get(country)

    if proxy_ip:
        driver = browser(proxy_ip=proxy_ip)
    else:
        driver = browser()

    try:
        driver.get(login_info["login_url"])

        wait = WebDriverWait(driver, Config.TIMEOUT)
        wait.until(EC.presence_of_element_located((By.ID, login_info["email_id"])))

        email_address = driver.find_element_by_id(login_info["email_id"])
        btn_next = driver.find_element_by_id(login_info["btn_next"])

        email_address.clear()
        email_address.send_keys(email)
        btn_next.click()
        time.sleep(5)
        password_id = driver.find_element_by_id(login_info["password_id"])
        password_id.send_keys(password)
        btnLoginBtn = driver.find_element_by_id(login_info["login_btn_id"])
        btnLoginBtn.click()
        time.sleep(6)

        try:
            driver.find_element_by_link_text(login_info["verification_text"]).click()
        except NoSuchElementException:
            pass

        if driver.title == login_info["login_success"]:
            flag = 0 # 登录成功
            driver.quit()
        elif driver.title == login_info["login_title"]:
            flag = 1 # 没有登录成功
            driver.quit()
        else:
            flag = 2 # 需要安全验证
            driver.quit()
    except TimeoutException:
        flag = 3 # 网站超时
        driver.quit()
    except:
        flag = 4 # 未知原因
        driver.quit()
    finally:
        if save_to_db:
            insert_sql = "INSERT INTO task_result(task_field,flag) VALUES ('{task_field}',{flag})".format(
                task_field=":".join([email,password]),
                flag=flag
            )
            utils.task_result(insert_sql=insert_sql)

        # 打印结果
        _msg = {
            "0": "成功",
            "1": "失败",
            "2": "验证",
            "3": "超时",
            "4": "未知"
        }.get(str(flag))

        print("任务[{}:{}],结果:{}".format(email,password,_msg))

        driver.quit()

if __name__ == '__main__':
    login_paypal("xyz@gmail.com","************",save_to_db=True)
