#!/usr/bin/env python
# coding=utf-8
from base import WebPage
from base import By


class WebCommonPage(WebPage):
    """
    Web端公共页面常用的元素和公共方法
    """
    # 元素属性
    home_link = (By.LINK_TEXT, '首页', '首页tab')
    # 用户登录元素
    user_name_input_box = (By.CSS_SELECTOR, 'input[placeholder="手机号/用户名/邮箱"]')
    pwd_input_box = (By.XPATH, '//input[@placeholder="密码"]')
    login_btn = (By.XPATH, '//button[contains(text(), "登录")]')
    login_locator = [user_name_input_box, pwd_input_box, login_btn]

    def click_to_home_page(self):
        """点击首页"""
        self.click(self.home_link)

    def login(self, data):
        """登录操作"""
        self.submit(self.login_locator, data)

    def open_and_maximize(self, url):
        """打开网址并最大化窗口"""
        self.logger.info("访问URL：{}".format(url))
        self.get(url)
        try:
            self.maximize_window()
        except SystemError:
            self.logger.info('system does not support change window size')

    def check_url_and_log(self, expected_url):
        """检查url和错误日志"""
        current_url = self.get_current_url()
        self.logger.info("预期url地址： {0}".format(expected_url))
        current_log = self.get_error_log()
        if expected_url in current_url and not current_log:
            return True
        else:
            return False
