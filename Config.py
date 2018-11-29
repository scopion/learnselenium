# -*- coding:utf-8 -*-
# @File    : Config.py

# 浏览器的配置
TIMEOUT = 30 # 网页超时时间

OPTIONS = {
    '--start-maximized':False,
    '--headless':True,
    '--no-sandbox':True,
    '--single-process':False, # windows下不能使用
    '--disable-gpu':True,
    '--disable-speech-input':True,
    '--no-first-run':True,
    '--no-startup-window':True,
    '--disable-print-preview':True,
    '--user-agent':"user-agent=Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
}

CountryDict = {
        "zh":{
            "login_url":"https://www.paypal.com/c2/signin?country.x=C2&locale.x=zh_C2",
            "login_title":"登录您的PayPal账户",
            "email_id":"email",
            "btn_next":"btnNext",
            "password_id":"password",
            "login_btn_id":"btnLogin",
            "verification_text":"以后再说",
            "login_success":"PayPal: 账户首页"
        },
        "us":{
            "login_url":"https://www.paypal.com/us/signin",
            "login_title":"Log in to your PayPal account",
            "email_id":"email",
            "btn_next":"btnNext",
            "password_id":"password",
            "login_btn_id":"btnLogin",
            "verification_text":"Not now",
            "login_success":"PayPal: Summary"
        }

}
# 以下二选一即可，格式：ip:port
proxy_url = "" # 代理IP的URL
proxy_file = "proxy_pool.txt"

# 任务文件，格式:xxxxxxxx@gmail.com:********
TASK_FILE = "tasks.txt"

# 任务结果保存到sqlite3数据库
TASK_RESULT = "data.db"

# 多进程配置
TIMES_CPU = 4 # multi_login_paypal.py中使用，四核CPU时，同时开启4 * 4 = 16 个进程
