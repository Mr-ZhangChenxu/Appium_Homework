# /usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021-03-06  上午9:40
# @Author  : ZhangChenXu
# @File    : app.py
from appium import webdriver

# 定义App，封装App启动和driver
from page.main_page import MainPage


class App():
    def __init__(self):
        self.driver = None
        self.start()

    def start(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        # 不清空缓存启动App
        desired_caps['noReset'] = 'true'
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
        # 生成driver后立刻设置隐式等待
        self.driver.implicitly_wait(10)

    def goto_main_page(self):
        # 跳转到App主页
        return MainPage(self.driver)
