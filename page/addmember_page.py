# /usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021-03-06  上午9:44
# @Author  : ZhangChenXu
# @File    : addmember_page.py
from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage


class AddmemberPage(BasePage):
    # 添加成员
    # 输入姓名、电话，选择性别，点击保存，获取toast文本
    def addmember(self, username, phone_num):
        self._params['username'] = username
        self._params['phone_num'] = phone_num
        self.parse_action('../page/datas/addmember.yaml')
        add_result = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        return add_result