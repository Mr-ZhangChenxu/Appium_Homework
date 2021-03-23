# /usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021-03-06  上午11:11
# @Author  : ZhangChenXu
# @File    : test_addmember.py
from page.app import App
import random

class TestAddmember():

    def setup(self):
        '''
        实例化App（）；
        通过链式调用PO；
        完成联系人添加并验证
        :return:
        '''
        self.app = App()

    def teardown(self):
        pass

    def test_addmember(self):
        '''
        1、添加成员
        2、检验添加成功后的toast
        :return:
        '''

        # 获取随机数
        n1 = random.randint(0, 9)
        num = random.randint(11111111, 99999999)

        # 将要添加的成员信息
        username = f'name_{n1}'
        phone_num = f'136{num}'

        # 添加成员
        add_result = self.app.goto_main_page().goto_members_page().\
            goto_addmember_page().addmember(username, phone_num)

        # 校验是否添加成功
        assert add_result == '添加成功'

