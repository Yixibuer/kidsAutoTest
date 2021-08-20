#!/usr/bin/env python
# coding = utf-8

from appium.webdriver.webdriver import WebDriver
from base import MobilePage


class IosPage(MobilePage):
    """移动端操作方法

    包含iOS端的api
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver
        super().__init__(self.driver)

    def double_click(self, locator):
        """双击"""
        element = self.find_element(locator)
        self.execute_js('mobile: doubleTap', {'element': element})
        self.logger.info('双击元素')

    def reset(self):
        """重置应用"""
        self.driver.reset()
