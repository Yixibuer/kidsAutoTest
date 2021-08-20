import time
import allure

from base.testcase import TestCase
from page.ios.search_page import SearchPage


class TestSearchPage(TestCase):

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.search_page = SearchPage(cls.driver)

    @allure.title('点击搜索-作品搜索结果匹配')
    @allure.description('发现-点击搜索-作品搜索结果匹配')
    def test_search_click(self):
        with allure.step('点击搜索'):
            self.search_page.click_search()
        with allure.step('获取热门搜索关键字'):
            searchName = self.search_page.get_search_name()
        with allure.step('点击第一个热门搜索'):
            self.search_page.click_keyboard_search_btn()
            time.sleep(1)
        with allure.step('获取作品列表第一个名称'):
            firstWorkName = self.search_page.get_tab_first_work_name()
        with allure.step('验证作品名称和搜索是否正确'):
            self.assert_true(searchName in firstWorkName)

    @allure.title('点击搜索-用户搜索结果匹配')
    @allure.description('发现-点击搜索-用户搜索结果匹配')
    def test_search_click(self):
        with allure.step('点击搜索'):
            self.search_page.click_search()
        with allure.step('获取热门搜索关键字'):
            searchName = self.search_page.get_search_name()
        with allure.step('点击第一个热门搜索'):
            self.search_page.click_keyboard_search_btn()
            time.sleep(1)
        with allure.step('点击用户tab'):
            self.search_page.click_search_user_tab()
            time.sleep(1)
        with allure.step('获取用户列表第一个用户名称'):
            userName = self.search_page.get_tab_first_user_name()
        with allure.step('验证作品名称和搜索是否正确'):
            self.assert_true(searchName in userName)





