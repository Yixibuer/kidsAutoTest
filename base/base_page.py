#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import re
import time
import traceback
from base64 import b64encode
from datetime import datetime

import allure
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidArgumentException, \
    ElementNotInteractableException, ElementNotVisibleException, UnexpectedAlertPresentException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from base import By
from utils import logger, common
from utils import config
from utils import type_assert

# 常用配置
WAIT_TIME = float(config.wait_time)


class BasePage:
    """
    页面基类

    提供基本的查找元素及通用操作元素的方法，用于web页面和移动端页面继承

    """

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.logger = logger
        self.platform = common.get_env_var('platform')

    # 获取元素和元素信息，返回元素信息数组
    @type_assert(locator=tuple)
    def find_element(self, locator, sleep_time=WAIT_TIME, condition=None):
        """
        查找可见的页面元素

        :Args:
         - locator - 定位元素
            格式示例：(By.ID, 'element_id', "元素信息") 或 (By.ID, 'element_id')，
            元素信息可选，主要用于打印调试日志以及后期维护
         - sleep_time - 可选参数
            显式等待时间，默认读取配置时间
         - condition - 可选参数
            expected_conditions模块提供的等待条件，默认使用presence_of_element_located
         Note: 参数类型需要匹配：locator：tuple, condition：str

        :Usage:
         _locator = (By.ID, 'element_id', "元素信息")
         self.find_element(self._locator)
         self.find_element(self._locator, sleep_time=5, condition=EC.element_to_be_clickable)

        :Returns:
         返回Webelement对象
        """
        self.logger.debug(f'定位的元素：{locator}')
        start = time.time()
        try:
            wait = WebDriverWait(self.driver, sleep_time, poll_frequency=0.1)
            if condition is None:
                element = wait.until(EC.presence_of_element_located(locator[:2]))
            else:
                element = wait.until(condition(locator[:2]))
            self.logger.info(f"获取元素 {locator[-1]} SUCCESS Spend {time.time() - start} seconds")
            self.logger.debug(f"获取到的元素：{element}")
            return element
        except (NoSuchElementException, TimeoutException):
            self.screenshot_to_report('获取元素失败')
            self.logger.error(f"获取元素 {locator[-1]} FAIL Spend {time.time() - start} seconds")
            traceback.print_exc()

    def find_elements(self, locators, sleep_time=WAIT_TIME, condition=None):
        """
        根据locators获取一个元素或多个可见元素

        主要为操作多个元素或单个元素的方法提供支持

        :Args:
         - locators: 定位元素, 参数类型：元祖或数组
            格式示例：(By.ID, 'element_id', "元素信息") 或 [(By.ID, 'element_id', "元素信息"),(By.ID, 'element_id', "元素信息")]，
            元素信息参数可选，主要用于打印调试日志以及后期维护
         - sleep_time - 可选参数
            显式等待时间，默认读取配置时间

        :Usage:
         _locator1 = (By.ID, 'element_id', "元素信息")
         _locator2 = (By.ID, 'element_id', "元素信息")
         _locators = [_locator1, _locator2]
         self.find_elements(_locator1)
         self.find_elements(_locators, sleep_time=5)

        :Returns:
         locator参数为单个元素或单个元素的数组，返回Webelement对象
         locator参数是多个元素组成的数组，返回多个Webelement对象组成的数组
        """
        self.logger.debug(f'定位的元素：{locators}')
        if locators and isinstance(locators, tuple):
            return self.find_element(locators, sleep_time, condition=condition)
        elif locators and isinstance(locators, list):
            if len(locators) == 1:
                return self.find_element(locators[0], sleep_time, condition=condition)
            else:
                elements = []
                for locator in locators:
                    elements.append(self.find_element(locator, sleep_time, condition=condition))
                self.logger.debug("获取到的元素对象列表：{0}".format(elements))
                return elements
        else:
            raise InvalidArgumentException("参数类型错误，请传入元祖或数组")

    @type_assert(locator=tuple)
    def find_group_elements(self, locator, sleep_time=WAIT_TIME, num=None):
        """
        获取一组相同类型或属性的元素

        :Args:
         - locator - 定位元素
            格式示例：(By.ID, 'element_id', "元素信息") 或 (By.ID, 'element_id')，
            元素信息可选，主要用于打印调试日志以及后期维护
         - sleep_time - 可选参数
            显式等待时间，默认读取配置时间
         - num - 可选参数
            获取元素的数量，默认为None，返回所有元素

        :Usage:
         _locator = (By.ID, 'element_id', "元素信息")
         self.find_group_elements(self._locator)
         # 获取前两个元素
         self.find_group_elements(self._locator, sleep_time=5, num=2)

        :Returns:
         返回Webelement对象组成的数组
        """
        start = time.time()
        try:
            wait = WebDriverWait(self.driver, sleep_time, poll_frequency=0.1)
            group_elements = wait.until(EC.presence_of_all_elements_located(locator[:2]))
            self.logger.info(f"获取元素 {locator[-1]} SUCCESS Spend {time.time() - start} seconds")
            self.logger.debug("已获取元素：{0}".format(group_elements))
            # 获取指定个数的元素
            if group_elements and isinstance(num, int):
                return group_elements[:num]
            return group_elements
        except (TimeoutException, NoSuchElementException):
            self.screenshot_to_report('获取一组元素失败')
            self.logger.error(f"获取元素 {locator[-1]} FAIL Spend {time.time() - start} seconds")
            traceback.print_exc()

    def get_group_elements_text(self, locator, sleep_time=WAIT_TIME):
        """
        获取一组元素(标签内)的文本

         :Args:
         - locator - 定位元素 格式示例：(By.ID, 'element_id', "元素信息") 或 (By.ID, 'element_id')，
            元素信息可选，主要用于打印调试日志以及后期维护
         - sleep_time - 可选参数
            显式等待时间，默认读取配置时间

        :Usage:
         _locator = (By.ID, 'element_id', "元素信息")
         self.get_group_elements_text(self._locator)
         self.get_group_elements_text(self._locator, sleep_time=5)

        :Returns:
         返回一组文本组成的数组
        """
        elements = self.find_group_elements(locator, sleep_time=sleep_time)
        elements_text = [element.text for element in elements]
        self.logger.info("获取到的元素文本列表：{}".format(elements_text))
        return elements_text

    def get_group_elements_value(self, locator, sleep_time=WAIT_TIME):
        """
        获取一组元素的value属性值

         :Args:
         - locator - 定位元素 格式示例：(By.ID, 'element_id', "元素信息") 或 (By.ID, 'element_id')，
            元素信息可选，主要用于打印调试日志以及后期维护
         - sleep_time - 可选参数
            显式等待时间，默认读取配置时间

        :Usage:
         _locator = (By.ID, 'element_id', "元素信息")
         self.get_group_elements_text(self._locator)
         self.get_group_elements_text(self._locator, sleep_time=5)

        :Returns:
         返回一组文本组成的数组
        """
        elements = self.find_group_elements(locator, sleep_time=sleep_time)
        elements_value = [element.get_attribute("value") for element in elements]
        self.logger.info("获取到的元素文本列表：{}".format(elements_value))
        return elements_value

    def return_elements_count(self, elements):
        """返回元素的数目

        :Args:
            - elements - 元素对象

        :Returns:
         返回elements数组长度，1 或 0
        """
        if isinstance(elements, list):
            elements_num = len(elements)
            self.logger.info("获取元素的个数为：{}".format(elements_num))
            return elements_num
        elif isinstance(elements, WebElement):
            self.logger.info("获取元素的个数为：1")
            return 1
        else:
            self.logger.info("获取元素的个数为：0")
            return 0

    def get_elements_count(self, locator, sleep_time=WAIT_TIME):
        """
        获取多个元素的个数

         :Args:
         - locator - 定位元素 格式示例：(By.ID, 'element_id', "元素信息") 或 (By.ID, 'element_id')，
            元素信息可选，主要用于打印调试日志以及后期维护
         - sleep_time - 可选参数
            显式等待时间，默认读取配置时间

        :Usage:
        class XXPage(BasePage):
             _locator = (By.ID, 'element_id', "元素信息")
             _locators = [(By.ID, 'element_id', "元素信息"), (By.ID, 'element_id', "元素信息")]

             def get_xx_count(self):
                 count = self.get_elements_count(self._locator)
                 return count

        :Returns:
         返回多个元素的数量
        """
        elements = self.find_elements(locator, sleep_time=sleep_time)
        return self.return_elements_count(elements)

    def get_group_elements_count(self, locator, sleep_time=WAIT_TIME):
        """
        获取一组相同类型或相同属性的元素的个数

         :Args:
         - locator - 定位元素 格式示例：(By.ID, 'element_id', "元素信息") 或 (By.ID, 'element_id')，
            元素信息可选，主要用于打印调试日志以及后期维护
         - sleep_time - 可选参数
            显式等待时间，默认读取配置时间

        :Usage:
         _locator = (By.ID, 'element_id', "元素信息")
         self.get_group_elements_count(self._locator)
         self.get_group_elements_count(self._locator, sleep_time=5)

        :Returns:
         返回一组元素的数量
        """
        group_elements = self.find_group_elements(locator, sleep_time=sleep_time)
        return self.return_elements_count(group_elements)

    def is_element(self, locator_or_element, sleep_time=WAIT_TIME):
        """
        根据不同参数，返回Webelement对象，内部调用

         :Args:
         - locator_or_element - 定位元素参数或Webelement对象
         - sleep_time - 可选参数
            显式等待时间，默认读取配置时间

        :Usage:
         _locator = (By.ID, 'element_id', "元素信息")
         self.is_element(self._locator)
         element = self.find_element(self._locator)
         self.is_element(element)

        :Returns:
         返回Webelement对象
        """
        if isinstance(locator_or_element, tuple):
            element = self.find_element(locator_or_element, sleep_time)
            return element
        if isinstance(locator_or_element, WebElement):
            return locator_or_element

    def send_keys(self, locator, test_data, sleep_time=WAIT_TIME):
        """
        输入操作

         :Args:
         - locator - 定位元素, 参数类型：元祖或数组
            格式示例：(By.ID, 'element_id', "元素信息") 或 [(By.ID, 'element_id', "元素信息"),(By.ID, 'element_id', "元素信息")]，
         - test_data - 输入数据
            单个输入，传入单个数据即可
            多个输入，传入多个数据即可，类型一般为元祖或数组

        :Usage:
         # 两个输入框输入数据
         _locator1 = (By.ID, 'element_id', "元素信息")
         _locator2 = (By.ID, 'element_id', "元素信息")
         _locator = [_locator1, _locator2]
         test_data = [123, 345]
         self.send_keys(_locator, 123)
         self.send_keys(_locator, test_data)

        """
        start = time.time()
        try:
            elements = self.find_elements(locator, sleep_time=sleep_time)
            if isinstance(elements, list) and isinstance(test_data, (tuple, list)):
                if len(elements) != len(test_data):
                    raise InvalidArgumentException(f'输入框和输入数据数量不一致, 元素数目：{len(elements)}，输入数据列表数目：{len(test_data)}')
                for index, element in enumerate(elements):
                    element.clear()
                    element.send_keys(test_data[index])
                    self.logger.info(
                        "{0} send_keys {1}, Spend {2} seconds".format(locator[index][-1], test_data[index],
                                                                      time.time() - start))
            elif isinstance(elements, WebElement):
                elements.clear()
                elements.send_keys(test_data)
                self.logger.info(
                    "{0} send_keys {1}, Spend {2} seconds".format(locator[-1], test_data, time.time() - start))
            else:
                raise NoSuchElementException(f'{locator} 未获取到元素')
        except (ElementNotInteractableException, ElementNotVisibleException):
            self.screenshot_to_report('输入失败')
            traceback.print_exc()

    def click(self, locator, sleep_time=WAIT_TIME):
        """
        点击操作

        :Args:
         - locator - 定位元素 格式示例：(By.ID, 'element_id', "元素信息") 或 (By.ID, 'element_id')，
            元素信息可选，主要用于打印调试日志以及后期维护
         - sleep_time - 可选参数
            显式等待时间，默认读取配置时间

        :Usage:
         _locator = (By.ID, 'element_id', "元素信息")
         self.click(self._locator)
         self.click(self._locator, sleep_time=5)

        """
        start = time.time()
        element = self.find_element(locator, sleep_time=sleep_time, condition=EC.element_to_be_clickable)
        try:
            if isinstance(element, WebElement):
                element.click()
                self.logger.info("点击  {0}  Spend {1} seconds".format(locator[-1], time.time() - start))
                self.sleep(0.5)
            else:
                self.logger.error(f'{locator}，未获取到元素')
        except UnexpectedAlertPresentException:
            traceback.print_exc()

    def click_existing_element(self, locator, sleep_time=WAIT_TIME):
        element = self.find_element(locator, sleep_time=sleep_time)
        if isinstance(element, WebElement):
            element.click()
            self.logger.info(f'元素{locator[-1]}存在, 点击成功')
        else:
            self.logger.info(f'元素{locator[-1]}不存在，无需点击')

    def clear(self, locator, sleep_time=WAIT_TIME):
        """
        输入框清空
        """
        element = self.find_element(locator, sleep_time=sleep_time)
        element.clear()

    @type_assert(locator=list)
    def submit(self, locator, test_data, sleep_time=1):
        """
        输入数据并点击按钮，提交表单

        适用场景：
        多个输入框输入数据后，需要点击提交

        :Args:
         - locator - 定位元素 由至少一个输入框元素和一个提交按钮元素组成的数组
            格式示例：[(By.ID, 'element_id', "输入框元素"), (By.ID, 'element_id', '提交按钮')]
         - test_data - 输入数据
            单个输入，则传入一个测试数据
            多个输入，则传入多个测试数据组成的元祖或数组
         - sleep_time - 可选参数
            输入完成后的等待时间，默认1s

        :Usage:
         _locator1 = (By.ID, 'element_id', "输入框1")
         _locator2 = (By.ID, 'element_id', "输入框2")
         _locator = (By.ID, 'element_id', "提交按钮")
         _locator = [_locator1, _locator2, _locator]
         test_data = [123, 345]
         self.submit(_locator, test_data)

        """
        # 输入数据
        # 两个元素，则直接取第一个元素输入
        if len(locator) == 2:
            self.send_keys(locator[0], test_data)
        else:
            self.send_keys(locator[:-1], test_data)
        self.sleep(sleep_time)
        # 点击最后一个元素提交
        self.click(locator[-1])

    def get_elements_text(self, locator, sleep_time=WAIT_TIME):
        """
        获取一个或多个元素的文本值

        :Args:
         - locator - 定位元素 格式示例：(By.ID, 'element_id', "元素信息") 或 (By.ID, 'element_id')，
            元素信息可选，主要用于打印调试日志以及后期维护
         - sleep_time - 可选参数
            显式等待时间，默认读取配置时间

        :Usage:
         _locator = (By.ID, 'element_id', "元素信息")
         self.get_elements_text(self._locator)
         _locator1 = (By.ID, 'element_id', "元素信息")
         _locator2 = (By.ID, 'element_id', "元素信息")
         _locator = [_locator1, _locator2]
         self.get_elements_text(_locator, sleep_time=5)

        :Returns:
         传入单个元素，返回单个文本
         传入多个元素，返回多个文本组成的数组
        """
        try:
            elements = self.find_elements(locator, sleep_time=sleep_time)
            if elements and isinstance(elements, list):
                text = [element.text for element in elements]
                self.logger.info(f'获取元素的文本： {text}')
            if isinstance(elements, WebElement):
                text = elements.text
                self.logger.info(f'获取元素的文本： {text}')
                return text
        except AttributeError:
            traceback.print_exc()

    def get_elements_attr(self, locator, attr, sleep_time=WAIT_TIME):
        """
        获取一个或多个元素的属性值

        :Args:
            attr: 获取的属性，例如label、name、text、value等等
        :Usage:
            用法同get_elements_text
        """
        elements = self.find_elements(locator, sleep_time=sleep_time)
        if elements and isinstance(elements, list):
            attrs = [element.get_attribute(attr) for element in elements]
            self.logger.info("元素的{}属性值列表为：{}".format(attr, attrs))
            return attrs
        if isinstance(elements, WebElement):
            attrs = elements.get_attribute(attr)
            self.logger.info("元素的{}属性值为：{}".format(attr, attrs))
            return attrs

    def get_elements_value(self, locator, sleep_time=WAIT_TIME):
        """
        获取一个或多个元素的value属性值

        用法同get_elements_text
        """
        return self.get_elements_attr(locator, attr='value', sleep_time=sleep_time)

    @type_assert(locator=tuple)
    def is_element_contains_text(self, locator, text):
        """
        判断元素内是否包含text文本信息
        """
        element_text = self.get_elements_text(locator)
        self.logger.info("预期结果的文本：{0}".format(text))
        self.logger.info("实际获取到元素中的文本：{0}".format(element_text))
        if element_text:
            return text in element_text
        return False

    @type_assert(locator=tuple)
    def is_element_value_contains_text(self, locator, text, sleep_time=WAIT_TIME):
        """
        判断元素属性值是否有text文本信息
        """
        element_value = self.get_elements_value(locator, sleep_time=sleep_time)
        self.logger.info("预期结果的文本：{0}".format(text))
        self.logger.info("实际获取到元素文本：{0}".format(element_value))
        if element_value:
            return text in element_value
        return False

    def is_selected(self, locator_or_element, sleep_time=WAIT_TIME):
        """
        检查单选框或复选框选中
        """
        element = self.is_element(locator_or_element, sleep_time=sleep_time)
        try:
            if element:
                return element.is_selected()
            return False
        except StaleElementReferenceException:
            traceback.print_exc()

    def is_enabled(self, locator_or_element, sleep_time=WAIT_TIME):
        """
        检查元素是否可用
        """
        element = self.is_element(locator_or_element, sleep_time=sleep_time)
        try:
            if element:
                return element.is_enabled()
            return False
        except StaleElementReferenceException:
            traceback.print_exc()

    def is_displayed(self, locator_or_element, sleep_time=WAIT_TIME):
        """
        检查元素是否可见
        """
        element = self.is_element(locator_or_element, sleep_time)
        try:
            if element:
                return element.is_displayed()
            return False
        except StaleElementReferenceException:
            traceback.print_exc()

    def back(self, times=1, sleep_time=1):
        """返回上一页

          :Args:
            times: 返回次数，默认执行返回一次
            sleep_time: 返回操作后等待时间
        """
        for i in range(times):
            self.driver.back()
            self.sleep(sleep_time)
            self.logger.info("返回上一页")

    @staticmethod
    def sleep(second=2):
        """等待时间

        """
        time.sleep(second)

    def get(self, url: str):
        """输入url进入页面

        :Args
        - url 浏览器访问地址

        """
        self.driver.get(url)

    def page_source(self):
        """获取页面结构元素"""
        source = self.driver.page_source
        self.logger.debug(f'当前页面结构：{source}')
        return source

    def execute_js(self, *args, **kwargs):
        """执行js"""
        self.driver.execute_script(*args, **kwargs)
        self.logger.info(f"execute javascript : {args}, {kwargs}")

    @type_assert(locator=tuple)
    def is_element_exist(self, locator, sleep_time=WAIT_TIME):
        """判断定位的元素是否存在"""
        element = self.find_element(locator, sleep_time=sleep_time)
        # 查找到元素，返回True，否则返回False
        if isinstance(element, WebElement):
            return True
        else:
            return False

    @type_assert(locators=list)
    def is_elements_exist(self, locators, sleep_time=WAIT_TIME):
        """判断定位的多个元素是否存在"""
        elements = self.find_elements(locators, sleep_time=sleep_time)
        result = [isinstance(element, WebElement) for element in elements]
        if False in result:
            return False
        else:
            return True

    def screenshot(self, file_name=""):
        """截图

        截图文件名称：当前时间+窗口标题(web)+file_name(可选)

        """
        screenshot_path = os.path.abspath(config.screenshot_path)
        if not os.path.exists(screenshot_path):
            os.mkdir(screenshot_path)
        time_str = self.get_datetime_str()
        if self.platform == 'web':
            window_title = self.driver.title
            file_path = f'{screenshot_path}/{time_str}{window_title}{file_name}.png'
        else:
            file_path = f'{screenshot_path}/{time_str}{file_name}.png'
        self.driver.get_screenshot_as_file(file_path)
        self.logger.info("截图保存在: {0}".format(screenshot_path))
        return file_path

    def screenshot_to_report(self, img_desc='异常'):
        """截图添加到测试报告

        :Args:
            img_src: 测试报告中的截图描述
        """
        file_path = self.screenshot()
        with open(file_path, 'rb') as f:
            img = f.read()
            allure.attach(img, img_desc, allure.attachment_type.PNG)

    @staticmethod
    def get_number_from_str(string):
        """提取字符串中的数字"""
        number = re.search(r'\d+', string).group()
        return int(number)

    @staticmethod
    def get_img_base64(path):
        with open(path, 'rb') as f:
            b64_byte = b64encode(f.read())
            b64_str = b64_byte.decode('utf-8')
            return b64_str

    @staticmethod
    def get_datetime_str():
        """获取日期字符串"""
        datetime_str = datetime.now().strftime('%Y%m%d%H%M%S%f')
        return datetime_str
# if __name__=="__main__":
#
#     driver=common.get_android_driver()
#     codemao_login_btn = (By.ID, 'com.codemao.nemo:id/tv_account', '手机/账号登录按钮')
#     time.sleep(10)
#     driver.find_element(By.ID,"com.codemao.nemo:id/tv_account").click()
