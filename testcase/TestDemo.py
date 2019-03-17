#!/usr/bin/env python
# -*- Coding:utf-8 -*-
import pytest
from pages.login_page import LoginPage


class TestDemo:

    @pytest.mark.parametrize('username, password',
                             [('myrebate@qq.com', 'db147258')
                             ])
    def test_douban(self, username, password):
        login_page_object = LoginPage()

        #allure.step
        login_page_object.switch_to_login_frame()
        #allure step
        login_page_object.click_login_tab()
        #allure step
        login_page_object.input_user_name(username)
        # allure step
        login_page_object.input_password(password)

        login_page_object.click_login_button()
        '''
        login_page_object.login(username, password)
        '''
        text = login_page_object.get_my_douban_text()
        assert text == "我的豆瓣"