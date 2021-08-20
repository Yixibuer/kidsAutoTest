import time
import allure

from base.testcase import TestCase
from page.ios.template_page import TemplatePage


class TestTemplatePage(TestCase):

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.TemplatePage = TemplatePage(cls.driver)

    @allure.title('TC1004')
    @allure.description('从模板作品进入创作，保存退出')
    def test_TC1004(self):
        with allure.step('点击 + 按钮'):
            self.TemplatePage.click_add()
        with allure.step('点击从模板中创建'):
            self.TemplatePage.click_template_work()
            time.sleep(1)
        with allure.step('点击立即创建'):
            self.TemplatePage.click_immediately_create()
            time.sleep(2)
        with allure.step('点击左上角菜单按钮'):
            self.TemplatePage.click_template_menu_op()
            time.sleep(1)
        with allure.step('点击退出按钮'):
            self.TemplatePage.click_template_out_but()
        with allure.step('选中保存退出'):
            self.TemplatePage.click_out_page_ok()
            time.sleep(2)
        with allure.step('验证模板作品保存成功'):
            # 如果涉及时区问题需要做调整
            # 获取作品时间
            _work_time = int(
                time.mktime(time.strptime(self.TemplatePage.get_my_page_first_work_time(), "%Y-%m-%d %H:%M")))
            # 当前时间
            dt = int(
                time.mktime(time.strptime(time.strftime("%Y-%m-%d %H:%M", time.localtime()), "%Y-%m-%d %H:%M")))
            self.assert_true(_work_time >= dt)

    @allure.title('TC1005')
    @allure.description('从模板作品进入创作，不保存退出')
    def test_TC1005(self):
        with allure.step('点击 + 按钮'):
            self.TemplatePage.click_add()
        with allure.step('点击从模板中创建'):
            self.TemplatePage.click_template_work()
            time.sleep(1)
        with allure.step('点击立即创建'):
            self.TemplatePage.click_immediately_create()
            time.sleep(1)
        with allure.step('点击左上角菜单按钮'):
            self.TemplatePage.click_template_menu_op()
            time.sleep(1)
        with allure.step('点击退出按钮'):
            self.TemplatePage.click_template_out_but()
        with allure.step('不保存退出'):
            self.TemplatePage.click_out_page_no()
        with allure.step('验证回到模板选择页面'):
            # 待验证
            self.assert_true(self.TemplatePage.is_by_name_immediately_create())
