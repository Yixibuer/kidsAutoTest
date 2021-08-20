"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
import pytest
import allure
from base.testcase import TestCase
from page.ios.login_page import LoginPage


class TestLoginPage(TestCase):
    """测试用例类

    继承自testcase，提供基本的初始化操作和断言方法

    导入涉及到的页面类即可

    测试初始化：
        页面类实例化必须重写setup_class，
        必须要先调用super().setup_class()，初始化driver驱动，才能再实例化页面类

    测试用例：
        直接组合页面实例提供的方法，再对应进行断言即可，

    """

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.login_page = LoginPage(cls.driver)

    def test_to_login_page(self):
        """
        测试跳转到登录页
        """
        self.ios_comm_page.click_codemao_act()
        self.assert_true('断言已跳转到登录页')

    def test_to_register_page(self):
        """
        测试跳转到注册页面
        """
        self.login_page.click_to_register_page()
        self.login_page.back()
        self.assert_true('断言跳转到注册页面')

    def test_to_forgot_pwd_page(self):
        """
        测试跳转到忘记密码页面
        """
        self.login_page.click_to_forgot_pwd_page()
        self.assert_true('断言跳转到忘记密码页面')

    @pytest.mark.parametrize('username, password', [(111, '123'), (222, '456')])
    @allure.title('登录失败测试')
    @allure.description('登录失败测试')
    def test_invalid_login(self, username, password):
        """
        异常登录测试
        """
        test_data = [username, password]
        self.ios_comm_page.login(test_data)
        # 断言错误提示
        self.assert_equal(self.login_page.get_error_tips(), '用户或者密码不正确哦')

    @pytest.mark.P0
    @allure.tag('TC0000')
    @allure.title('正常登录测试')
    def test_valid_login(self):
        """正常登录测试

        """
        with allure.step('点击编程猫账号'):
            self.login_page.click_codemao_act()
        with allure.step('输入账号密码登录'):
            self.ios_comm_page.login()
        with allure.step('断言获取到推荐tab和最新tab'):
            # 断言获取到我的按钮，表明登录成功
            self.assert_true(self.login_page.get_my_btn())
