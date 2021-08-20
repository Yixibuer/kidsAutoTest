#!/usr/bin/env python
# coding=utf-8
from base import By
from page.web_common_page import WebCommonPage


class LoginPage(WebCommonPage):
    """
    登录页面
    """
    # 登录失败提示
    wrong_tips = (By.XPATH, "//div[contains(text(), '账户名或密码错误')]")

    def get_wrong_tips(self):
        return self.find_elements(self.wrong_tips)

