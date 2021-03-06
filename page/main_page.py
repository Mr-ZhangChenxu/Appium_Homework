# /usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021-03-06  上午9:40
# @Author  : ZhangChenXu
# @File    : main_page.py
from page.base_page import BasePage
from page.members_page import MembersPage


class MainPage(BasePage):
    # 跳转通讯录页
    def goto_members_page(self):
        self.parse_action('../page/datas/main.yaml')
        return MembersPage(self.driver)