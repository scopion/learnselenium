# -*- coding:utf-8 -*-
# @File    : browser.py

"""
实例化一个浏览器
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")
import Config

def browser(proxy_ip=None):
    chrome_options = Options()

    for option_value,is_active in Config.OPTIONS.items():
        if is_active:
            chrome_options.add_argument(option_value)
        if option_value == '--user-agent':
            chrome_options.add_argument(is_active)

    profile = {"plugins.plugins_disabled": ['Chrome PDF Viewer'], # 禁用PDF
               "plugins.plugins_disabled": ['Adobe Flash Player'], # 禁用 Flash
               "profile.managed_default_content_settings.images": 2} # 不加载图

    chrome_options.add_experimental_option("prefs", profile)

    if proxy_ip:
        chrome_options.add_argument('--proxy-server=http://' + proxy_ip)

    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(Config.TIMEOUT)
    driver.set_script_timeout(Config.TIMEOUT)

    return driver