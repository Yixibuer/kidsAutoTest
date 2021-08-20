import pytest
import allure
from base.testcase import TestCase
from page.ios.cloud_work_page import CloudWorkPage
from page.ios.my_page import MyPage
from page.ios.works_detail_page import WorksDetailPage
from page.ios.user_detail_page import UserDetail


class TestCloudWorkPage(TestCase):
    """云端作品页面测试"""

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.cloud_page = CloudWorkPage(cls.driver)
        cls.my_page = MyPage(cls.driver)
        cls.works_detail_page = WorksDetailPage(cls.driver)
        cls.user_detail = UserDetail(cls.driver)

    # @allure.tag('TC0001')
    # @allure.title('验证云端搜索是否能搜出对应结果')
    # @pytest.mark.P0
    # def test_search_cloud_work(self):
    #     """测试搜索云端作品"""
    #     keyword = '测试'
    #     with allure.step('点击我的'):
    #         self.ios_comm_page.click_my_btn()
    #     with allure.step('点击云端作品入口'):
    #         self.my_page.click_cloud_icon()
    #     with allure.step('点击搜索'):
    #         self.cloud_page.click_search_btn()
    #     with allure.step('输入关键字，搜索'):
    #         self.cloud_page.search_cloud_word(keyword)
    #     with allure.step('断言搜索出来的作品都包含关键字'):
    #         expected_num = self.cloud_page.get_works_count()
    #         actual_num = self.cloud_page.get_works_name_count(keyword)
    #         self.assert_equal(expected_num, actual_num)
    #     with allure.step('点击取消按钮'):
    #         self.cloud_page.click_search_cancel_btn()
    #         self.cloud_page.back()
    #
    # @allure.tag('TC0001')
    # @allure.title('验证云端搜索是否能搜出对应结果')
    # @pytest.mark.P0
    # @pytest.mark.parametrize('keyword', ['作品', '1', 'y', '-'])
    # def test_search_cloud_work2(self, keyword):
    #     """测试搜索云端作品"""
    #     with allure.step('点击搜索'):
    #         self.cloud_page.click_search_btn()
    #     with allure.step('输入关键字，搜索'):
    #         self.cloud_page.search_cloud_word(keyword)
    #     with allure.step('断言搜索出来的作品都包含关键字'):
    #         expected_num = self.cloud_page.get_works_count()
    #         actual_num = self.cloud_page.get_works_name_count(keyword)
    #         self.assert_equal(expected_num, actual_num)
    #     with allure.step('点击取消按钮'):
    #         self.cloud_page.back()

    @allure.tag('TC0002')
    @allure.title('验证云端作品取消删除按钮功能是否正常')
    @pytest.mark.P0
    def test_cancel_delete_works(self):
        """取消删除云端作品"""
        with allure.step('点击我的'):
            self.ios_comm_page.click_my_btn()
        with allure.step('点击云端作品入口'):
            self.my_page.click_cloud_icon()
        with allure.step('点击删除前，获取云端作品名称和时间'):
            works_name, works_date = self.cloud_page.get_works_name_and_date()
        with allure.step('点击删除，点击取消按钮'):
            self.cloud_page.cancel_delete_cloud_works()
        with allure.step('获取取消删除后的作品名称和时间是否存在'):
            result = self.cloud_page.is_works_exists(works_name, works_date)
        with allure.step('断言删除后的作品还存在'):
            self.assert_true(result)

    @allure.tag('TC0003')
    @allure.title('验证云端作品删除按钮功能是否正常')
    @pytest.mark.P0
    def test_delete_cloud_works(self):
        """确认删除云端作品"""
        with allure.step('点击我的'):
            self.ios_comm_page.click_my_btn()
        with allure.step('点击云端作品入口'):
            self.my_page.click_cloud_icon()
        with allure.step('点击删除前，获取云端作品名称和时间'):
            works_name, works_date = self.cloud_page.get_works_name_and_date()
        with allure.step('点击删除，点击确认删除按钮'):
            self.cloud_page.delete_cloud_works()
        with allure.step('获取删除后的作品名称和时间是否存在'):
            result = self.cloud_page.is_works_exists(works_name, works_date)
        with allure.step('断言删除前后的作品数量相等'):
            self.assert_false(result)

    @allure.tag('TC0004')
    @allure.title('验证云端作品下载功能是否正常')
    @pytest.mark.P0
    def test_download_cloud_works(self):
        """下载云端作品"""
        with allure.step('点击我的'):
            self.ios_comm_page.click_my_btn()
        with allure.step('返回上一页'):
            self.cloud_page.back()
        with allure.step('获取草稿作品数量'):
            # 预期结果为，下载前数量 + 1
            expected_works_count = self.my_page.get_draft_works_count() + 1
        with allure.step('点击云端作品入口'):
            self.my_page.click_cloud_icon()
        with allure.step('点击下载按钮'):
            expected_works_name = self.cloud_page.get_works_name()
            self.cloud_page.click_download_btn()
        with allure.step('返回'):
            self.cloud_page.back()
        with allure.step('获取草稿作品数量'):
            actual_works_count = self.my_page.get_draft_works_count()
        with allure.step('断言草稿箱作品数量和下载的作品名称'):
            self.assert_equal(expected_works_count, actual_works_count)
            # 断言草稿箱第一个作品名称包含云端作品下载的作品名称
            self.assert_true(self.cloud_page.is_works_name_exist(expected_works_name))


