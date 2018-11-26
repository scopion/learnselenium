# -*- coding:utf-8 -*-
# @File    : test_selenium.py

"""
测试browser.py里的driver是否正常工作
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

from browser import browser

get_url = 'http://httpbin.org/get'

driver = browser()
driver.get(get_url)
print(driver.page_source)