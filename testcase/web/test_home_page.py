import allure
from base.testcase import TestCase
from page.web.home_page import HomePage


@allure.parent_suite('首页')
@allure.suite('首页')
# @allure.sub_suite('页面模块3')
class TestHomePage(TestCase):
    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.home_page = HomePage(cls.driver)

    @allure.title('点击首页')
    def test_home_link(self):
        """点击首页"""
        with allure.step('点击首页'):
            self.home_page.click_to_home_page()

    @allure.title('点击发现')
    def test_discover_link(self):
        """点击发现"""
        self.home_page.click_discover_tab()
        self.screenshot_to_report('点击发现')
        # self.home_page.sleep(3)

    @allure.title('点击论坛')
    def test_forum_tab(self):
        """点击论坛"""
        self.home_page.click_forum_tab()
        self.screenshot_to_report('点击论坛')

    @allure.title('点击工作室')
    def test_work_shop_tab(self):
        """点击工作室"""
        self.home_page.click_work_shop_tab()
        try:
            self.assert_true(1)
        except AssertionError as e:
            self.screenshot_to_report('点击工作室')





