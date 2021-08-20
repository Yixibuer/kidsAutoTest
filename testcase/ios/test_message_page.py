import time

import allure

from base.testcase import TestCase
from page.ios.message_page import MessagePage


class TestMessage(TestCase):

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.message_page = MessagePage(cls.driver)

    @allure.title('TC1020')
    @allure.description('消息通知——点赞/被创作页面切换（p0）')
    def test_TC1020(self):
        with allure.step('点击左上角消息按钮，进入消息页面'):
            self.message_page.click_message()
        with allure.step('切换到被创作'):
            self.message_page.click_create()
            time.sleep(1)
        with allure.step('切换到点赞页'):
            self.message_page.click_like_and_collect()
        with allure.step('点击返回，退出消息页面'):
            self.message_page.click_return_home()
        with allure.step('验证成功回到首页'):
            self.assert_true(self.ios_comm_page.is_element_exist(self.ios_comm_page._discover_btn))

    @allure.title('TC1022')
    @allure.description('消息通知——点赞页面打开点赞用户中心页面')
    def test_TC1022(self):
        with allure.step('点击左上角消息按钮，进入消息页面'):
            self.message_page.click_message()
        with allure.step('获取第一个作品名称'):
            user_name = self.message_page.get_first_user_name()
        with allure.step('点击用户头像，打开用户中心'):
            self.message_page.click_first_user_img()
            time.sleep(1)
        with allure.step('验证用户中心页面打开正常，用户名称正确'):
            user_detail_name = self.message_page.user_detail_name()
            self.assert_true(user_detail_name == user_name)
        with allure.step('点击返回，关闭用户中心'):
            self.message_page.click_return_home()
        with allure.step('验证成功回到点赞页面'):
            self.assert_true(self.ios_comm_page.is_element_exist(self.message_page._like_and_collect))

    @allure.title('TC1023')
    @allure.description('消息通知——点赞页面打开点赞用户中心页面')
    def test_TC1023(self):
        with allure.step('点击左上角消息按钮，进入消息页面'):
            self.message_page.click_message()
        with allure.step('获取第一个作品名称'):
            first_work_name = self.message_page.get_first_works_name()
        with allure.step('点击第一个作品'):
            self.message_page.click_first_work()
            time.sleep(1)
        with allure.step('通过作品名称定位元素是否存在'):
            result = self.message_page.is_accessibility_id_exist(first_work_name)
            time.sleep(1)
        with allure.step('断言获取作品名称正确'):
            self.assert_true(result)
        with allure.step('点击返回，关闭作品详情页'):
            self.message_page.click_return_home()
        with allure.step('验证成功回到点赞页面'):
            time.sleep(1)
            self.assert_true(self.ios_comm_page.is_element_exist(self.message_page._like_and_collect))
        with allure.step('点返回发现首页'):
            self.message_page.click_return_home()

    @allure.title('TC1024')
    @allure.description('消息通知——被再创作页面作品验证')
    def test_TC1024(self):
        with allure.step('点击左上角消息按钮，进入消息页面'):
            self.message_page.click_message()
        with allure.step('切换到被再创作'):
            self.message_page.click_create()
            time.sleep(1)
        with allure.step('获取被创作第一个作品名称'):
            first_work_name = self.message_page.get_first_works_name()
        with allure.step('点击第一个作品'):
            self.message_page.click_first_work()
            time.sleep(1)
        with allure.step('通过作品名称定位元素是否存在'):
            result = self.message_page.is_accessibility_id_exist(first_work_name)
            time.sleep(1)
        with allure.step('断言获取作品名称正确'):
            self.assert_true(result)
        with allure.step('点击返回，关闭作品详情页'):
            self.message_page.click_return_home()
        with allure.step('验证成功回到上一页'):
            time.sleep(1)
            self.assert_true(self.ios_comm_page.is_element_exist(self.message_page._like_and_collect))
        with allure.step('点返回发现首页'):
            self.message_page.click_return_home()

    @allure.title('TC1025')
    @allure.description('消息通知——被再创作页面用户认证')
    def test_TC1025(self):
        with allure.step('点击左上角消息按钮，进入消息页面'):
            self.message_page.click_message()
        with allure.step('切换到被再创作'):
            self.message_page.click_create()
            time.sleep(1)
        with allure.step('获取被创作第一个作品名称'):
            first_user_name = self.message_page.get_first_user_name()
        with allure.step('点击第一个用户'):
            self.message_page.click_first_user_img()
            time.sleep(1)
        with allure.step('通过用户名称定位元素是否存在'):
            result = self.message_page.is_accessibility_id_exist(first_user_name)
            time.sleep(1)
        with allure.step('断言获取用户名称正确'):
            self.assert_true(result)
        with allure.step('点击返回，关闭作品详情页'):
            self.message_page.click_return_home()
        with allure.step('验证成功回到上一页'):
            time.sleep(1)
            self.assert_true(self.ios_comm_page.is_element_exist(self.message_page._like_and_collect))
        with allure.step('点返回发现首页'):
            self.message_page.click_return_home()
