# /usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021-03-06  上午9:40
# @Author  : ZhangChenXu
# @File    : base_page.py
from typing import List, Dict

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

# 定义基类
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    # 定义传入值字典
    _params = {}

    def __init__(self, driver:WebDriver):
        self.driver = driver

    # 定义查找点击方法
    def find_click(self, locator):
        return self.driver.find_element(MobileBy.XPATH, locator).click()

    # 定义查找传参方法
    def find_sendkey(self, locator, value):
        return self.driver.find_element(MobileBy.XPATH, locator).send_keys(value)

    # 定义滑动查找点击方法
    def swip_click(self, text):
        return self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        f'scrollIntoView(new UiSelector().text("{text}").'
                                                        'instance(0));').click()

    # 定义显示等待
    def waitfor_click(self, locator):
        locato = (MobileBy.XPATH, locator)
        ele = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locato))
        return ele.click()

    # 定义步骤驱动
    def parse_action(self, path):
        # 读取yaml文件
        with open(path, 'r', encoding='utf-8') as f:
            steps: List[Dict] = yaml.safe_load(f)

        # 循环读取stps
        for step in steps:
            if step['action'] == 'find_click':
                self.find_click(step['locator'])
            elif step['action'] == 'swip_click':
                self.swip_click(step['text'])
            elif step['action'] == 'find_sendkey':
                value:str = step['value']
                # 对 self._params 循环读取
                for param in self._params:
                    # 重写value，以self._params[param]替代'{%s}'%param
                    value = value.replace('{%s}'%param, self._params[param])
                self.find_sendkey(step['locator'], value)
            elif step['action'] == 'waitfor_click':
                self.waitfor_click(step['locator'])


