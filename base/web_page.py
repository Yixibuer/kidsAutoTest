#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from base import BasePage


class WebPage(BasePage):
    """web端页面基类

    提供web端定位元素的api和各种操作元素的api

    """

    def maximize_window(self):
        """浏览器窗口最大化"""
        self.driver.maximize_window()

    def get_title(self):
        """获取浏览器窗口标题"""
        return self.driver.title

    def get_alert_text(self):
        """获取弹窗文本"""
        alert_obj = Alert(self.driver)
        alert_text = alert_obj.text
        alert_obj.accept()
        self.logger.info("弹窗提示： {0}".format(alert_text))
        return alert_text

    def drag_drop(self, locator, x_offset, y_offset):
        """拖拽某个元素到坐标点"""
        action = ActionChains(self.driver)
        source = self.find_element(locator)
        action.drag_and_drop_by_offset(source, x_offset, y_offset)
        time.sleep(1)
        action.perform()

    def get_current_url(self):
        """获取当前页面的url"""
        current_url = self.driver.current_url
        self.logger.info("当前的页面地址: {0}".format(current_url))
        return current_url

    def get_window_handles(self):
        """获取浏览器窗口"""
        return self.driver.window_handles

    def switch_window(self, index=-1):
        """切换窗口，默认切换到最新窗口"""
        windows = self.get_window_handles()
        self.logger.debug("打开的窗口：{0}".format(windows))
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[index])
        self.sleep(1)

    def get_error_log(self):
        """判断浏览器是否有错误日志"""
        logs = self.driver.get_log("browser")
        self.logger.info("获取到浏览器控制台日志：{}".format(logs))
        if len(logs) == 0:
            self.logger.info("页面未获取到错误日志")
            return False
        else:
            for log in logs:
                if log["level"] in ["ERROR", "SEVERE"]:
                    self.logger.error("页面获取到错误日志：{0}".format(log))
                    return True
                else:
                    self.logger.warning("页面获取到非Error日志：{0}".format(log))
                    continue
            return False

    def refresh(self):
        """刷新页面"""
        self.driver.refresh()
        self.logger.info('刷新页面')

    def mouse_hover(self, locator_or_element, sleep_time=2):
        """鼠标悬停"""
        action = ActionChains(self.driver)
        element = self.is_element(locator_or_element)
        self.logger.info("鼠标移动到元素：{0}".format(element))
        action.move_to_element(element).perform()
        self.sleep(sleep_time)

    def select_option(self, locator_or_element, option_value=None, index=0):
        """下拉框选择

        根据选项值或索引选择下拉选项

        :Args:
            - locator_or_element： 定位元素或WebElement对象
            - option_value：  下拉框选项值，不传则默认选择第一个
            - index：下拉选项索引，默认选择第一个
        """
        element = self.is_element(locator_or_element)
        select = Select(element)
        # 按索引选择
        if option_value is None:
            select_option_values = []
            for select_option in select.options:
                select_option_values.append(select_option.text)
            # 默认选择第一个
            option_value = select_option_values[index]
            select.select_by_visible_text(option_value)
            self.logger.info("选择下拉选项：{0}".format(option_value))
            return option_value
        # 按选项值选择
        select.select_by_visible_text(option_value)
        self.logger.info("选择下拉选项：{0}".format(option_value))

    def close(self):
        """关闭浏览器窗口"""
        self.driver.close()
        self.logger.info("关闭当前窗口")

    def scroll_to_top(self):
        """将滚动条移动到页面的顶部"""
        js = "var q=document.documentElement.scrollTop=0"
        self.execute_js(js)
        self.logger.info('滑动到页面的顶部')

    def scroll_to_bottom(self):
        """将滚动条移动到页面的底部"""
        js = "var q=document.documentElement.scrollTop=10000"
        self.execute_js(js)
        self.logger.info('滑动到页面的底部')

    def switch_frame(self, frame_reference):
        """切换iframe

         :Args:
         - frame_reference: The name of the window to switch to, an integer representing the index,
                            or a webelement that is an (i)frame to switch to.

        :Usage:
            driver.switch_to.frame('frame_name')
            driver.switch_to.frame(1)
            driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
        """
        self.driver.switch_to.frame(frame_reference)
        self.logger.info(f'切换frame：{frame_reference}')

    def switch_to_main_document(self):
        """切换到主文档"""
        self.driver.switch_to.default_content()
        self.logger.info('切换到主文档')

    def switch_to_alert(self):
        """切换到警告框"""
        self.driver.switch_to.alert()
        self.logger.info('切换到警告框')

    def upload_file(self, locator, file_path):
        """上传文件"""
        element = self.find_element(locator)
        element.send_keys(file_path)
        self.logger.info(f'文件：{file_path} 已上传')
