from base.testcase import TestCase
from page.web.login_page import LoginPage
from page.web.home_page import HomePage
import pytest
from utils import data


class TestLoginPage(TestCase):

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.home_page = HomePage(cls.driver)
        cls.login_page = LoginPage(cls.driver)

    def test_to_login_page(self):
        self.home_page.to_login_page()
        # 断言失败截图到报告
        try:
            self.assert_equal(1, 2)
        except AssertionError:
            self.screenshot_to_report('登录')

    @pytest.mark.parametrize('username, password', data.invalid_login_data)
    def test_invalid_login(self, username, password):
        """测试无效登录"""
        test_data = [username, password]
        self.login_page.login(test_data)
        # self.home_page.sleep(2)
        self.assert_true(self.login_page.get_wrong_tips())
