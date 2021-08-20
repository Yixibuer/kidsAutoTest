import allure
import pytest
from base.testcase import TestCase
from page.android.login_page import LoginPage
from page.android.account_login_page import AccountloginPage
from utils import data


class TestLoginPage(TestCase):
    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.login_page=LoginPage(cls.driver)
        cls.account_login_page=AccountloginPage(cls.driver)


    def test_click_account_login(self):
        """测试从首页快捷入口点击跳转到登录页"""
        with allure.step("点击已购课用户请登录"):
            self.login_page.click_fast_enter_login()









