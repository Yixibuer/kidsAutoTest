import pytest
import allure
from page.ios.my_page import MyPage
from page.ios.cloud_work_page import CloudWorkPage
from base.testcase import TestCase
from ocv.settings import Settings as ST
from utils import config


@allure.parent_suite('我的页面')
@allure.suite('我的页面')
@allure.sub_suite('我的页面')
class TestMyPage(TestCase):
    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.my_page = MyPage(cls.driver)
        cls.cloud_page = CloudWorkPage(cls.driver)

    @allure.tag('TC0014')
    @allure.title('验证本地搜索是否能搜出对应结果')
    @pytest.mark.P0
    def test_search_draft_box_works(self):
        """测试本地搜索草稿箱作品"""
        with allure.step('进入我的页面'):
            self.ios_comm_page.click_my_btn()
        with allure.step('点击复制按钮'):
            self.my_page.click_copy_btn()
        with allure.step('修改作品名字'):
            self.my_page.click_edit_btn()
            self.my_page.edit_draft_works_name('本地搜索测试作品')
        with allure.step('点击搜索'):
            self.ios_comm_page.click_search_btn()
        with allure.step('输入关键字，搜索'):
            self.my_page.search_works('本地搜索测试作品')
        with allure.step('搜索出来的作品都包含关键字'):
            expected_num = self.cloud_page.get_works_count()
            actual_num = self.my_page.get_contains_works_name_count('本地搜索测试作品')
        with allure.step('删除复制的作品'):
            self.ios_comm_page.back()
            self.my_page.delete_draft_works()
        with allure.step('断言搜索出来的作品都包含关键字'):
            self.assert_equal(expected_num, actual_num)

    @allure.tag('TC0015')
    @allure.title('验证已发布列表是否能搜出对应结果')
    @pytest.mark.P0
    def test_search_published_works(self):
        """测试搜索已发布的作品"""
        keyword = '作品'
        with allure.step('进入我的页面'):
            self.ios_comm_page.click_my_btn()
        with allure.step('点击搜索'):
            self.ios_comm_page.click_search_btn()
        with allure.step('输入关键字，搜索'):
            self.my_page.search_works(keyword)
        with allure.step('切换到已发布列表'):
            self.my_page.click_published_btn()
        with allure.step('搜索出来的作品都包含关键字'):
            expected_num = self.cloud_page.get_works_count()
            actual_num = self.cloud_page.get_works_name_count(keyword)
        with allure.step('断言搜索出来的作品都包含关键字'):
            self.assert_equal(expected_num, actual_num)

    @allure.tag('TC0015')
    @allure.title('验证已发布列表是否能搜出对应结果')
    @pytest.mark.P0
    def test_search_published_works2(self):
        """测试搜索已发布的作品"""
        keyword = '-'
        with allure.step('进入我的页面'):
            self.ios_comm_page.click_my_btn()
        with allure.step('点击搜索'):
            self.ios_comm_page.click_search_btn()
        with allure.step('输入关键字，搜索'):
            self.my_page.search_works(keyword)
        with allure.step('切换到已发布列表'):
            self.my_page.click_published_btn()
        with allure.step('搜索出来的作品都包含关键字'):
            expected_num = self.cloud_page.get_works_count()
            actual_num = self.cloud_page.get_works_name_count(keyword)
        with allure.step('断言搜索出来的作品都包含关键字'):
            self.assert_equal(expected_num, actual_num)

    @allure.tag('TC2006')
    @allure.title('我的页面-复制草稿箱作品测试')
    @allure.story('草稿箱页面')
    @pytest.mark.P0
    def test_copy_draft_works(self):
        """
        测试复制草稿箱作品功能，点击复制：草稿数量加1
        """
        with allure.step('进入我的页面'):
            self.ios_comm_page.click_my_btn()
        with allure.step('获取草稿箱作品数量'):
            expected_draft_count = self.my_page.get_draft_works_count() + 1
        with allure.step('获取草稿箱第一个作品名称'):
            expected_first_works_name = self.my_page.get_works_name(page=self.ios_comm_page.MY_DRAFT_PAGE)
        with allure.step("点击复制按钮"):
            self.my_page.click_copy_btn()
        with allure.step('获取草稿箱作品数量和第一个作品名称'):
            draft_works_count = self.my_page.get_draft_works_count()
            first_works_name = self.my_page.get_works_name(page=self.ios_comm_page.MY_DRAFT_PAGE)
        with allure.step('删除复制的第一个作品'):
            self.my_page.delete_draft_works()
        with allure.step("断言复制的作品数加1"):
            self.assert_equal(expected_draft_count, draft_works_count)
        with allure.step("断言复制的作品名称"):
            self.assert_in(expected_first_works_name, first_works_name)

    @allure.tag('TC2007')
    @allure.title('我的页面-重命名草稿箱作品测试')
    @allure.story('草稿箱页面')
    @pytest.mark.P0
    def test_rename_draft_works(self):
        """
        重命名草稿箱作品测试
        """
        works_name = ['重命名草稿箱作品测试重命名草稿箱作品测试', 'SDFGHJKCVBNMWERTYUd', 'asdasfs和娃few发我']
        with allure.step('进入我的页面'):
            self.ios_comm_page.click_my_btn()
        with allure.step("点击复制按钮"):
            self.my_page.click_copy_btn()
            expected_works_name = self.my_page.get_works_name(page=self.ios_comm_page.MY_DRAFT_PAGE)
        with allure.step('取消修改作品名字'):
            self.my_page.click_edit_btn()
            self.my_page.click_edit_name_cancel_btn()
        with allure.step('获取第一个作品名称'):
            actual_works_name = self.my_page.get_works_name(page=self.ios_comm_page.MY_DRAFT_PAGE)
        with allure.step("断言取消命名成功"):
            self.assert_equal(expected_works_name, actual_works_name)
        for name in works_name:
            with allure.step('修改作品名字'):
                self.my_page.click_edit_btn()
                self.my_page.edit_draft_works_name(name)
            with allure.step('获取第一个作品名称'):
                actual_works_name2 = self.my_page.get_works_name(page=self.ios_comm_page.MY_DRAFT_PAGE)
            with allure.step("断言草稿箱作品命名成功"):
                self.assert_equal(name, actual_works_name2)
        with allure.step('删除复制的第一个作品'):
            self.my_page.delete_draft_works()

    @allure.tag('TC2008')
    @allure.title('我的页面-发布作品和取消发布')
    @allure.story('草稿箱页面')
    @pytest.mark.P0
    def test_publish_works_and_cancel(self):
        """
        发布作品和取消发布
        """
        with allure.step('进入我的页面'):
            self.ios_comm_page.click_my_btn()
        with allure.step("点击复制按钮"):
            self.my_page.click_copy_btn()
        with allure.step('获取已发布的作品数量'):
            expected_published_num = self.my_page.get_published_works_count() + 1
        with allure.step('发布作品，获取发布后的按钮'):
            self.my_page.publish_works()
            self.my_page.click_draft_tab()
        with allure.step('获取已发布作品数量和取消发布按钮'):
            actual_published_num = self.my_page.get_published_works_count()
            cancel_publish_btn = self.my_page.get_cancel_publish_button()
        with allure.step('断言已发布的作品数量加1，存在取消发布按钮'):
            self.assert_equal(expected_published_num, actual_published_num)
            self.assert_true(cancel_publish_btn)
        with allure.step('取消发布作品'):
            self.my_page.cancel_publish_works()
            published_btn = self.my_page.get_publish_button()
        with allure.step('重新打开应用刷新, 获取已发布的作品数量'):
            self.ios_comm_page.reset()
            self.ios_comm_page.click_my_btn()
            actual_published_num2 = self.my_page.get_published_works_count() + 1
        with allure.step('断言已发布的作品数量减1，存在取消发布按钮'):
            self.assert_equal(actual_published_num, actual_published_num2)
            self.assert_true(published_btn)
        with allure.step('删除复制的第一个作品'):
            self.my_page.delete_draft_works()

    @allure.tag('TC2009')
    @allure.title('我的页面-修改已发布作品名称')
    @pytest.mark.P0
    def test_rename_published_works(self):
        """
        修改已发布作品名称
        验证作品名称最大支持20个字符
        """
        works_name = ['重命名草稿箱作品测试重命名草稿箱作品测试123', 'SDFGHJKCVBNMWERTYUd2131', 'asdasfs和娃few发我wsd3122']
        with allure.step('进入我的页面'):
            self.ios_comm_page.click_my_btn()
            self.my_page.click_published_works()
        with allure.step('点击已发布作品，进入作品详情'):
            self.my_page.click_published_works_cover()
        with allure.step('点击编辑作品信息'):
            self.my_page.click_edit_works_info_btn()
        with allure.step('获取作品简介默认提示,并断言'):
            summary_result = self.my_page.get_publish_works_summary_tips()
            self.assert_true(summary_result)
        with allure.step('编辑作品名称'):
            for name in works_name:
                input_name = self.my_page.enter_publish_work_name(name)
                self.assert_equal(name[:20], input_name)
        self.my_page.click_publish_btn()
        result = self.my_page.is_works_name_exist(works_name[-1][:20])
        self.assert_true(result)

    @allure.tag('TC2010')
    @allure.title('我的页面-修改作品封面成功')
    @pytest.mark.P0
    def test_update_works_cover(self):
        """
        修改作品封面成功
        """
        with allure.step('进入我的页面'):
            self.ios_comm_page.click_my_btn()
            self.my_page.click_published_works()
        with allure.step('点击已发布作品，进入作品详情'):
            self.my_page.click_published_works_cover()
        with allure.step('点击编辑作品信息'):
            self.my_page.click_edit_works_info_btn()
        with allure.step('更新作品封面'):
            self.my_page.upload_works_cover()
        self.my_page.click_publish_btn()
        ST.IMG_DIR_PATH = config.locate_img_path
        result = self.ios_comm_page.is_img_exists('publish_works_success_tips.png', threshold=0.998)
        self.assert_true(result)

    @allure.tag('TC2011')
    @allure.title('我的页面-修改作品描述成功')
    @pytest.mark.P0
    def test_edit_published_works_summary(self):
        """
        修改作品描述成功
        """
        works_summary = '重命名草稿箱作品测试重命名草稿箱作品测试156重命名草稿箱作品测试重命名草稿箱作品测试156重命名草稿箱作品测试重命名草稿箱作品测试156重命名草稿箱作品测试重命名草稿箱作品测试156重命名草稿箱作品测试重命名草稿箱作品测试156重命名草稿箱作品测试重命名草稿箱作品测试156重命名草稿箱作品测试重命名草稿箱作品测试156重命名草稿箱作品测试重命名草稿箱作品测试156重命名草稿箱作品测试重命名草稿箱作品测试12'
        with allure.step('进入我的页面'):
            self.ios_comm_page.click_my_btn()
            self.my_page.click_published_works()
        with allure.step('点击已发布作品，进入作品详情'):
            self.my_page.click_published_works_cover()
        with allure.step('点击编辑作品信息'):
            self.my_page.click_edit_works_info_btn()
        with allure.step('输入作品简介'):
            print(self.ios_comm_page.page_source())
            self.my_page.enter_publish_works_summary(works_summary)
        with allure.step('点击发布'):
            self.my_page.click_publish_btn()
        with allure.step('获取发布后的作品简介，并断言'):
            # summary = self.my_page.get_publish_works_summary('重重重命名草稿箱作品测试重命名草稿箱作重命名草稿箱作品测试重命名草稿箱作品测试喵重命名草稿箱作品测试重命名草稿箱作品测试喵重命名草稿箱作品测试重命名草稿箱作品测试喵重命名草稿箱作品测试重命名草稿箱作品测试喵重命名草稿箱作品测试重命名草稿箱作品测试喵重命名草稿箱作品测试重命名草稿箱作品测试喵重命名草稿箱作品测试重命名草稿箱作品测试喵重命名草稿箱作品测试重命名草稿箱作品测试喵重命名喜欢我喵作品吗')
            summary = self.my_page.get_publish_works_summary(works_summary[:200])
            print(self.ios_comm_page.page_source())
            self.assert_equal(works_summary[:200], summary)

    @allure.tag('TC2011')
    @allure.title('我的页面-修改作品开源状态')
    @pytest.mark.P0
    def test_edit_works_open_status(self):
        """
        修改作品开源状态
        """
        with allure.step('进入我的页面'):
            self.ios_comm_page.click_my_btn()
            self.my_page.click_published_works()
        with allure.step('点击已发布作品，进入作品详情'):
            self.my_page.click_published_works_cover()
        with allure.step('点击编辑作品信息'):
            self.my_page.click_edit_works_info_btn()
            print(self.ios_comm_page.page_source())

    @allure.tag('TC2019')
    @allure.title('我的页面-草稿箱作品复制分享链接')
    @pytest.mark.P0
    def test_copy_draft_works_share_link(self):
        """
        草稿箱作品复制分享链接
        """
        with allure.step('进入我的页面'):
            self.ios_comm_page.click_my_btn()
        with allure.step("点击复制按钮"):
            self.my_page.click_copy_btn()
        with allure.step('点击分享,复制链接'):
            self.my_page.click_share_button()
            self.my_page.click_copy_link()
        with allure.step('获取复制成功的提示，并断言'):
            result = self.my_page.get_toast_tips('链接已复制成功，快去分享吧')
            self.assert_true(result)
        with allure.step('删除复制的第一个作品'):
            self.my_page.click_share_close_btn()
            self.my_page.delete_draft_works()

    @allure.tag('TC2020')
    @allure.title('我的页面-草稿箱作品保存分享图片')
    @pytest.mark.P0
    def test_save_draft_works_share_pic(self):
        """
        草稿箱作品保存分享图片
        """
        with allure.step('进入我的页面'):
            self.ios_comm_page.click_my_btn()
        with allure.step("点击复制按钮"):
            self.my_page.click_copy_btn()
        with allure.step('点击分享,复制链接'):
            self.my_page.click_share_button()
            self.my_page.click_save_picture()
        with allure.step('获取复制成功的提示，并断言'):
            result = self.my_page.get_toast_tips('图片保存成功')
            self.assert_true(result)
        with allure.step('删除复制的第一个作品'):
            self.my_page.click_share_close_btn()
            self.my_page.delete_draft_works()

    @allure.tag('TC2021')
    @allure.title('我的页面-草稿箱作品分享生成喵口令')
    @pytest.mark.P0
    def test_save_draft_works_share_pic(self):
        """
        草稿箱作品分享生成喵口令
        """
        with allure.step('进入我的页面'):
            self.ios_comm_page.click_my_btn()
        with allure.step("点击复制按钮"):
            self.my_page.click_copy_btn()
        with allure.step('点击分享,复制链接'):
            self.my_page.click_share_button()
            self.my_page.click_gen_miao_code()
        with allure.step('获取复制成功的提示，并断言'):
            result = self.ios_comm_page.get_toast_tips('喵口令已生成')
            self.assert_true(result)
        with allure.step('点击去粘贴，并断言提示'):
            self.my_page.click_to_paste()
            tips_result = self.ios_comm_page.get_toast_tips('喵口令已粘贴成功')
            self.assert_true(tips_result)
        with allure.step('删除复制的第一个作品'):
            self.my_page.delete_draft_works()

    @allure.tag('TC2022')
    @allure.title('我的页面-草稿箱作品取消生成分享链接')
    @pytest.mark.P0
    def test_cancel_generate_share_link(self):
        """
        草稿箱作品取消生成分享链接
        """
        with allure.step('进入我的页面'):
            self.ios_comm_page.click_my_btn()
        with allure.step("点击复制按钮"):
            self.my_page.click_copy_btn()
        with allure.step('点击分享'):
            self.my_page.click_share_button()
        with allure.step('点击生成分享卡片的关闭按钮'):
            self.my_page.click_generate_card_close_btn()
        with allure.step('获取草稿箱按钮,并断言'):
            self.assert_true(self.my_page.get_draft_tab())
        with allure.step('删除复制的第一个作品'):
            self.my_page.delete_draft_works()

    @allure.tag('TC2023')
    @allure.title('我的页面-草稿箱作品-关闭分享卡片页面')
    @pytest.mark.P0
    def test_close_share_card_page(self):
        """
        草稿箱作品-关闭分享卡片页面
        """
        with allure.step('进入我的页面'):
            self.ios_comm_page.click_my_btn()
        with allure.step("点击复制按钮"):
            self.my_page.click_copy_btn()
        with allure.step('点击分享,复制链接'):
            self.my_page.click_share_button()
        with allure.step('生成分享卡片后，点击关闭按钮'):
            self.my_page.click_copy_link()
            self.my_page.click_share_close_btn()
        with allure.step('获取草稿箱按钮,并断言'):
            self.assert_true(self.my_page.get_draft_tab())
        with allure.step('删除复制的第一个作品'):
            self.my_page.delete_draft_works()

    @allure.tag('TC2024')
    @allure.title('我的页面-草稿箱作品-关闭喵口令卡片页面')
    @pytest.mark.P0
    def test_close_miao_code_card_page(self):
        """
        关闭喵口令卡片页面
        """
        with allure.step('进入我的页面'):
            self.ios_comm_page.click_my_btn()
        with allure.step("点击复制按钮"):
            self.my_page.click_copy_btn()
        with allure.step('点击分享,复制链接'):
            self.my_page.click_share_button()
            self.my_page.click_gen_miao_code()
        with allure.step('关闭喵口令弹窗'):
            self.my_page.click_miao_code_close_btn()
        with allure.step('获取草稿箱按钮,并断言'):
            self.assert_true(self.my_page.get_draft_tab())
        with allure.step('删除复制的第一个作品'):
            self.my_page.delete_draft_works()

    # def test_delete_concel(self):
    #     """
    #     测试删除功能
    #     点击删除：草稿数量减1
    #     验证：删除、取消删除按钮正常
    #     """
    #     self.my_page.click_mine_btn()
    #     self.my_page.click_copy_btn()
    #     a1 = self.my_page.get_draft_works_count()
    #     self.logger.info("开始草稿箱数量为：  {}".format(a1))
    #     with allure.step("点击删除按钮"):
    #         self.my_page.delete_cancel()
    #         a2 = self.my_page.get_draft_works_count()
    #         self.logger.info("点击取消删除后草稿箱数量为：  {}".format(a2))
    #     with allure.step("验证草稿数量不变"):
    #         assert a2 == a1
    #         self.logger.info("success!!!取消删除后，草稿数量不变验证通过")

    #
    # @allure.title('我的-草稿箱上传按钮测试')
    # @allure.description('我的-上传成功测试')
    # @allure.feature('草稿箱页面、已发布页面')
    # @allure.story('草稿箱页面')
    # @pytest.mark.run(order=4)
    # def test_upload(self):
    #     """
    #     测试上传功能
    #     点击删除：上传按钮数量减1
    #     验证：上传按钮数目-1，功能正常
    #     """
    #     self.my_page.click_mine_btn()
    #     self.my_page.click_copy_btn()
    #     self.my_page.click_copy_btn()
    #     a = self.my_page.click_upload_button()
    #     self.logger.info("上传前数量为{}，上传后数量为{}".format(a[0], a[1]))
    #     with allure.step("验证点击上传按钮后，上传按钮数量-1"):
    #         assert a[1] == a[0] - 1
    #         self.logger.info("success!!!点击上传后，上传按钮数量-1验证通过")
    # 
    # @allure.title('我的-草稿箱分享喵口令测试')
    # @allure.description('我的-草稿箱分享喵口令测试')
    # @allure.feature('草稿箱页面、已发布页面')
    # @allure.story('草稿箱页面')
    # @pytest.mark.run(order=5)
    # def test_mao_share(self):
    #     """
    #     测试我的-草稿箱分享喵口令
    #     验证：我的-草稿箱分享喵口令
    #         点击去粘贴
    #         可以识别喵口令
    #     """
    #     self.my_page.click_mine_btn()
    #     # self.my_page.click_copy_btn()
    #     self.my_page.click_share_button()
    #     # sleep(5)
    #     with allure.step("点击分享喵口令"):
    #         self.my_page.click_mao_share()
    #         sleep(5)
    #     with allure.step("点击去粘贴"):
    #         self.my_page.miao_paste()
    #         sleep(3)
    #     with allure.step("重启app"):
    #         self.driver.close_app()
    #         sleep(5)
    #         self.driver.launch_app()
    #     with allure.step("弹出识别喵口令"):
    #         sleep(5)
    #         self.my_page.miao_open_later()
    #         self.logger.info('识别喵口令成功')
