import time

import pytest
import allure
from base.testcase import TestCase
from page.ios.find_page import FindPage
from page.ios.works_detail_page import WorksDetailPage


class TestFindPage(TestCase):

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.find_page = FindPage(cls.driver)
        cls.worksDetailPage = WorksDetailPage(cls.driver)

    @allure.title('TC1008')
    @allure.description('验证推荐页banner左右滑动、点击打开功能是否正常')
    @pytest.mark.P0
    def test_tc1008(self):
        with allure.step('从右向左滑动banner1次'):
            self.find_page.left_slide_one_banner()
            time.sleep(1)
        with allure.step('从右向左滑动banner1次'):
            self.find_page.right_slide_one_banner()
            time.sleep(1)
        with allure.step('从右向左滑动banner6次'):
            self.find_page.left_slide_one_banner()
            self.find_page.left_slide_one_banner()
            self.find_page.left_slide_one_banner()
            self.find_page.left_slide_one_banner()
            self.find_page.left_slide_one_banner()
            self.find_page.left_slide_one_banner()
        with allure.step('点击banner打开，并等待5s'):
            self.find_page.click_banner()
            time.sleep(5)
        with allure.step('点击banner页的返回按钮，并等待1s'):
            self.find_page.click_close_banner()
            time.sleep(1)
        with allure.step('验证已成功返回发现首页'):
            # 验证已成功返回发现首页
            self.assert_true(self.ios_comm_page.get_recommend())

    @allure.title('TC1009')
    @allure.description('验证推荐页banner打开后复制链接分享功能正常')
    @pytest.mark.P0
    def test_tc1009(self):
        with allure.step('点击banner，打开详情页'):
            self.find_page.click_banner()
            time.sleep(1)
        with allure.step('点击右上角分享按钮'):
            self.find_page.click_banner_share()
            time.sleep(1)
        with allure.step('点击复制链接'):
            self.find_page.click_banner_share_copy_link()
        # with allure.step('验证toast提示：复制成功'):
        #     # ios暂时没有弹出提示
        #     self.find_page.click_banner()
        # 复制后自动关闭窗口
        # with allure.step('点击关闭分享栏'):
        #     self.find_page.click_banner_share_copy_link_close()
        #     time.sleep(1)
        with allure.step('点击banner页的返回按钮，并等待1s'):
            self.find_page.click_close_banner()
            time.sleep(1)
        with allure.step('验证是否再首页'):
            # 验证已成功返回发现首页
            self.assert_true(self.ios_comm_page.get_recommend())

    @allure.title('TC1010')
    @allure.description('验证推荐页上下滑动加载作品、左右滑动切换最新页和推荐页功能是否正常')
    @pytest.mark.P0
    def test_tc1010(self):
        with allure.step('从下向上滑动5次，查看加载其他屏的作品'):
            self.find_page.up_slide_one_banner()
            self.find_page.up_slide_one_banner()
            self.find_page.up_slide_one_banner()
            self.find_page.up_slide_one_banner()
            self.find_page.up_slide_one_banner()
            time.sleep(1)
        with allure.step('点击“推荐”回到第一屏'):
            self.find_page.click_recommend()
        with allure.step('从右向左滑动1次'):
            self.find_page.right_to_left_slide()
        with allure.step('验证已成功切换到主题页'):
            self.assert_true(self.find_page.is_element_exist_theme_tab())
        with allure.step('从下向上滑动5次，查看加载其他屏的作品'):
            self.find_page.up_slide_one_banner()
            self.find_page.up_slide_one_banner()
            self.find_page.up_slide_one_banner()
            self.find_page.up_slide_one_banner()
            self.find_page.up_slide_one_banner()
        with allure.step('点击“推荐”回到第一屏'):
            self.find_page.click_recommend()
        with allure.step('验证已成功切换到推荐页'):
            # 验证已成功返回发现首页
            self.assert_true(self.ios_comm_page.get_recommend())

    @allure.title('TC1013')
    @allure.description('验证最新页上下滑动、左右滑动切换最新页和推荐页功能是否正常')
    @pytest.mark.P0
    def test_tc1013(self):
        with allure.step('点击换到“最新”'):
            self.find_page.click_last_tab()
        with allure.step('从下向上滑动5次，查看加载其他屏的作品'):
            self.find_page.up_slide_one_banner()
            self.find_page.up_slide_one_banner()
            self.find_page.up_slide_one_banner()
            self.find_page.up_slide_one_banner()
            self.find_page.up_slide_one_banner()
        with allure.step('点击换到“推荐”'):
            self.find_page.click_recommend()

    @allure.title('TC1014')
    @allure.description('验证最新页打开作品详情是否正常')
    @pytest.mark.P0
    def test_tc1014(self):
        with allure.step('点击最新tab'):
            self.find_page.click_last_tab()
        with allure.step('获取第一个作品作品名称和用户名'):
            works_name = self.find_page.get_works_name()
            creator_name = self.find_page.get_last_works_creator_name()
        with allure.step('点击作品，打开作品详情页面'):
            self.find_page.click_latest_works()
        with allure.step('校验列表和详情的作品名和用户是否一致'):
            result = self.worksDetailPage.is_works_name_and_creator_exist(works_name, creator_name)
            self.assert_true(result)

    @allure.title('TC1015')
    @allure.description('验证推荐页点赞作品后，发现页面点赞数刷新')
    @pytest.mark.P0
    def test_tc1015(self):
        with allure.step('获取第一个作品的作品名称和点赞数'):
            # 未实现
            work_name, work_like1 = self.find_page.get_recommend_first_work_name_and_like()
        with allure.step('点击打开作品'):
            self.find_page.click_first_work()
        with allure.step('点击点赞按钮，获取点赞数'):
            self.find_page.click_details_work_like()
            like_count = self.find_page.get_details_like_count()
            self.logger.info(like_count)
        with allure.step('点击返回回到发现页面'):
            self.find_page.back()
            self.find_page.swipe_to_up()
        with allure.step('获取点赞作品名称和点赞数，校验点赞数是否刷新'):
            _works_like_count = self.worksDetailPage.get_details_like_count()
            _detail_works_name = self.worksDetailPage.get_details_work_name()
        with allure.step('校验点赞数'):
            self.assert_true(work_name == _detail_works_name and work_like1 == _works_like_count)
