import allure
import pytest
from base.testcase import TestCase
from page.ios.my_page import MyPage
from page.ios.player_page import PlayerPage


class TestPlayerPage(TestCase):
    """player测试"""

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.player = PlayerPage(cls.driver)
        cls.my_page = MyPage(cls.driver)

    @allure.tag('测试画笔积木')
    @allure.title('测试画笔积木')
    @pytest.mark.P0
    def test_brush_blocks(self):
        """测试画笔积木"""
        self.ios_comm_page.enter_player('画笔积木盒-Test')
        result = self.player.check_brush_block()
        self.assert_true(result)

    @allure.tag('测试运算积木')
    @allure.title('测试运算积木')
    @pytest.mark.P0
    def test_calculation_blocks(self):
        """测试运算积木"""
        with allure.step('进入运算积木player页面'):
            self.ios_comm_page.enter_player('运算积木盒-2')
        with allure.step('点击积木，并验证预期页面'):
            result = self.player.check_calculation_block()
        with allure.step('断言获取的预期图片结果'):
            self.assert_true(result)

    @allure.tag('测试事件积木')
    @allure.title('测试事件积木')
    @pytest.mark.P0
    def test_event_blocks(self):
        """测试事件积木"""
        with allure.step('进入测试事件积木player页面'):
            self.ios_comm_page.enter_player('事件积木盒-1')
        with allure.step('点击积木，并验证预期页面'):
            result = self.player.check_event_blocks()
        with allure.step('断言获取的预期图片结果'):
            self.assert_true(result)

    @allure.tag('测试外观积木')
    @allure.title('测试外观积木')
    @pytest.mark.P0
    def test_appearance_blocks(self):
        """测试外观积木"""
        with allure.step('进入测试事件积木player页面'):
            self.ios_comm_page.enter_player('外观类积木盒')
        with allure.step('点击积木，并验证预期页面'):
            result = self.player.check_appearance_blocks()
        with allure.step('断言获取的预期图片结果'):
            self.assert_true(result)


