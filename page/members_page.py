# /usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021-03-06  上午9:40
# @Author  : ZhangChenXu
# @File    : members_page.py
from page.addmember_page import AddmemberPage
from page.base_page import BasePage


class MembersPage(BasePage):
    # 跳转到添加成员页
    def goto_addmember_page(self):
        self.parse_action('../page/datas/members.yaml')
        return AddmemberPage(self.driver)