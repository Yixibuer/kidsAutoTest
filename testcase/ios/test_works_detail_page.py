import allure
import pytest
from page.ios.my_page import MyPage
from page.ios.user_detail_page import UserDetail
from page.ios.works_detail_page import WorksDetailPage
from page.ios.creation_page import CreationPage
from base.testcase import TestCase
from utils import generator


class TestWorksDetailPage(TestCase):
    """作品详情页面测试"""

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.my_page = MyPage(cls.driver)
        cls.works_detail_page = WorksDetailPage(cls.driver)
        cls.user_detail = UserDetail(cls.driver)
        cls.creation_page = CreationPage(cls.driver)

    @allure.tag('TC0005')
    @allure.title('验证作品详情页收藏按钮功能是否正常')
    @pytest.mark.P0
    def test_collect_works(self):
        """测试收藏作品"""
        with allure.step('点击最新tab'):
            self.ios_comm_page.click_latest_tab()
        with allure.step('获取第一个作品名称'):
            expected_works_name = self.ios_comm_page.get_works_name()
        with allure.step('点击第一个作品'):
            self.ios_comm_page.click_latest_works()
            # 置为未收藏状态
            self.works_detail_page.set_as_unfavored()
        with allure.step('作品详情页，点击收藏'):
            self.works_detail_page.click_collect_btn()
        with allure.step('返回上一页'):
            self.works_detail_page.back()
        with allure.step('点击我的'):
            self.ios_comm_page.click_my_btn()
        with allure.step('点击右箭头, 进入个人中心'):
            print(self.ios_comm_page.page_source())
            self.my_page.click_right_arrow()
        with allure.step('点击收藏，进入收藏页面'):
            self.user_detail.click_collection_btn()
        actual_works_name = self.ios_comm_page.get_works_name()
        with allure.step('断言'):
            self.assert_equal(expected_works_name, actual_works_name)

    @allure.tag('TC0006')
    @allure.title('验证作品详情页点赞按钮功能是否正常')
    @pytest.mark.P0
    def test_like_works(self):
        """测试点赞作品"""
        with allure.step('点击最新tab'):
            self.ios_comm_page.click_latest_tab()
        with allure.step('点击第一个作品'):
            self.ios_comm_page.click_latest_works()
            # 还原为未点赞的状态
            self.works_detail_page.set_as_unlike()
        with allure.step('作品详情页，获取点赞数'):
            expected_count = self.works_detail_page.get_details_like_count() + 1
        with allure.step('作品详情页，点赞，获取点赞数'):
            self.works_detail_page.click_like_btn()
            actual_like_count1 = self.works_detail_page.get_details_like_count()
        with allure.step('返回上一页, 下拉刷新'):
            self.works_detail_page.back()
            self.ios_comm_page.swipe_to_up()
            # self.ios_comm_page.swipe_to_up()
        with allure.step('获取第一个作品的点赞数'):
            actual_like_count2 = self.ios_comm_page.get_first_works_like_count()
        with allure.step('点击第一个作品'):
            self.ios_comm_page.click_latest_works()
        with allure.step('作品详情页，获取点赞数'):
            expected_count2 = self.works_detail_page.get_details_like_count() - 1
        with allure.step('作品详情页，取消点赞，获取点赞数'):
            self.works_detail_page.click_like_btn()
            actual_like_count3 = self.works_detail_page.get_details_like_count()
        with allure.step('返回上一页, 下拉刷新'):
            self.works_detail_page.back()
            self.ios_comm_page.swipe_to_up()
        with allure.step('获取第一个作品的点赞数'):
            actual_like_count4 = self.ios_comm_page.get_first_works_like_count()
        with allure.step('断言实际点赞数等于原有点赞数加1'):
            self.assert_equal(expected_count, actual_like_count1)
            self.assert_equal(expected_count, actual_like_count2)
        with allure.step('断言实际点赞数等于原有点赞数减1'):
            self.assert_equal(expected_count2, actual_like_count3)
            self.assert_equal(expected_count2, actual_like_count4)

    @allure.tag('TC0007')
    @allure.title('验证作品详情页分享按钮功能是否正常')
    @pytest.mark.P0
    def test_share_works(self):
        """测试分享作品"""
        with allure.step('点击最新tab'):
            self.ios_comm_page.click_latest_tab()
        with allure.step('点击第一个作品'):
            self.ios_comm_page.click_latest_works()
        with allure.step('作品详情页，点击分享'):
            self.works_detail_page.click_share_btn()
        with allure.step('作品详情页，点击复制链接'):
            self.works_detail_page.click_copy_link()
            result = self.works_detail_page.get_copy_success_tips('链接已复制成功, 快去分享吧')
            self.works_detail_page.click_copy_link()
            result2 = self.works_detail_page.get_copy_success_tips('链接已复制成功, 快去分享吧')
        with allure.step('断言获取提示成功'):
            self.assert_true(result)
            self.assert_true(result2)

    @allure.tag('TC0008')
    @allure.title('验证能否从作品详情页进入/退出Player播放页')
    @pytest.mark.P0
    def test_works_player(self):
        """测试作品详情页进入/退出Player播放页"""
        with allure.step('点击最新tab'):
            self.ios_comm_page.click_latest_tab()
        with allure.step('获取最新列表第一个作品的作品名、作者名'):
            works_name = self.ios_comm_page.get_works_name()
            creator_name = self.ios_comm_page.get_works_creator_name()
        with allure.step('点击第一个作品, 进入作品详情页'):
            self.ios_comm_page.click_latest_works()
        with allure.step('点击播放按钮'):
            self.works_detail_page.click_play_btn()
        with allure.step('获取播放页元素'):
            player_result = self.works_detail_page.check_player_element()
        with allure.step('点击关闭player'):
            self.works_detail_page.click_close_player()
        with allure.step('作品详情页，获取作品名、作者名'):
            result = self.works_detail_page.is_works_name_and_creator_exist(works_name, creator_name)
        with allure.step('断言获取到player元素和作品名、作者名'):
            self.assert_true(player_result)
            self.assert_true(result)

    @allure.tag('TC0009')
    @allure.title('验证最新列表作品信息与作品详情页信息一致')
    @pytest.mark.P0
    def test_latest_works_list_info(self):
        """测试最新作品列表信息"""
        with allure.step('点击最新tab'):
            self.ios_comm_page.click_latest_tab()
        with allure.step('获取最新列表第一个作品的作品名、作者名'):
            works_name = self.ios_comm_page.get_works_name()
            creator_name = self.ios_comm_page.get_works_creator_name()
        with allure.step('点击第一个作品, 进入作品详情页'):
            self.ios_comm_page.click_latest_works()
        with allure.step('作品详情页，获取作品名、作者名'):
            result = self.works_detail_page.is_works_name_and_creator_exist(works_name, creator_name)
        with allure.step('断言获取到作品名、作者名成功'):
            self.assert_true(result)

    @allure.tag('TC0010')
    @allure.title('验证作品详情页再创作按钮功能是否正常')
    @pytest.mark.P0
    def test_create_again(self):
        """测试再创作按钮功能是否正常"""
        with allure.step('点击我的，获取我的昵称'):
            self.ios_comm_page.click_my_btn()
            nickname = self.my_page.get_my_nickname()
        with allure.step('点击最新tab'):
            self.ios_comm_page.click_discover()
            self.ios_comm_page.click_latest_tab()
        with allure.step('点击其他人创作的作品, 获取作品名'):
            self.ios_comm_page.click_other_works(nickname)
            expected_works_name = self.works_detail_page.get_details_work_name()
        with allure.step('点击再创作按钮, 获取弹窗title'):
            self.works_detail_page.click_create_again()
            get_title_result = self.works_detail_page.get_create_again_title('再创作也是学习的方式哦')
        with allure.step('点击学习代码'):
            self.works_detail_page.click_learn_code()
        with allure.step('点击左上角菜单, 获取顶部按钮元素'):
            self.creation_page.click_more_btn()
            get_element_result = self.creation_page.get_top_element()
        with allure.step('点击退出'):
            self.creation_page.click_exit_btn()
        with allure.step('获取草稿箱作品名'):
            actual_works_name = self.my_page.get_draft_works_name()
        with allure.step('断言获取到弹窗title，顶部按钮元素，草稿箱作品名'):
            self.assert_true(get_title_result)
            self.assert_true(get_element_result)
            self.assert_in(expected_works_name, actual_works_name)

    @allure.tag('TC0011')
    @allure.title('验证作品详情页再创作按钮功能是否正常')
    @pytest.mark.P0
    def test_create_again_open_later(self):
        """测试再创作按钮功能是否正常"""
        with allure.step('获取我的昵称'):
            self.ios_comm_page.click_my_btn()
            nickname = self.my_page.get_my_nickname()
        with allure.step('点击最新tab'):
            self.ios_comm_page.click_discover()
            self.ios_comm_page.click_latest_tab()
        with allure.step('点击其他人创作的作品, 获取作品名和再创作数'):
            # 尽量选择一个积木很多的作品，加载时间久一些，方便点击稍后打开
            self.ios_comm_page.click_other_works(nickname)
            expected_works_name = self.works_detail_page.get_details_work_name()
            expected_create_again_count = self.works_detail_page.get_create_again_count() + 1
        with allure.step('点击再创作按钮, 获取弹窗title'):
            self.works_detail_page.click_create_again()
            get_title_result = self.works_detail_page.get_create_again_title('再创作也是学习的方式哦')
        with allure.step('点击学习代码，稍后打开，获取弹窗提示'):
            self.works_detail_page.click_learn_code()
            tips_result = self.works_detail_page.click_open_later()
            actual_create_again_count = self.works_detail_page.get_create_again_count()
        with allure.step('返回，进入我的，获取草稿箱第一个作品名字'):
            self.ios_comm_page.back()
            self.ios_comm_page.click_my_btn()
            actual_works_name = self.my_page.get_draft_works_name()
        with allure.step('断言获取到的数据'):
            self.assert_in(expected_works_name, actual_works_name)
            self.assert_equal(expected_create_again_count, actual_create_again_count)
            self.assert_true(get_title_result)
            self.assert_true(tips_result)

    def to_works_details(self):
        """进入作品详情"""
        with allure.step('获取我的昵称'):
            self.ios_comm_page.click_my_btn()
            nickname = self.my_page.get_my_nickname()
        with allure.step('点击最新tab'):
            self.ios_comm_page.click_discover()
            self.ios_comm_page.click_latest_tab()
        with allure.step('点击其他人创作的作品'):
            self.ios_comm_page.click_other_works(nickname)
        return nickname

    @allure.tag('TC0012')
    @allure.title('验证作品详情页里关注按钮功能是否有效')
    @pytest.mark.P0
    def test_follow_creator(self):
        """测试关注功能"""
        nickname = self.to_works_details()
        with allure.step('点击关注'):
            self.works_detail_page.click_follow_btn()
        with allure.step('点击创作者头像'):
            self.works_detail_page.click_avatar()
        with allure.step('点击粉丝, 进入粉丝列表'):
            self.user_detail.click_fans_btn()
        with allure.step('获取粉丝昵称结果'):
            result = self.user_detail.get_fans_result(nickname)
        with allure.step('返回到作品详情页'):
            self.ios_comm_page.back()
            self.ios_comm_page.back()
        with allure.step('点击已关注，取消关注'):
            self.works_detail_page.click_following_btn()
            unsubscribe_tips = self.works_detail_page.get_unsubscribe_tips()
        with allure.step('点击创作者头像'):
            self.works_detail_page.click_avatar()
        with allure.step('点击粉丝, 进入粉丝列表'):
            self.user_detail.click_fans_btn()
        with allure.step('获取粉丝昵称结果'):
            result2 = self.user_detail.get_fans_result(nickname)
        with allure.step('关注后断言获取到的粉丝昵称'):
            self.assert_true(result)
        with allure.step('取消关注后，断言获取不到粉丝昵称，获取到取消关注的提示'):
            self.assert_false(result2)
            self.assert_true(unsubscribe_tips)

    @allure.tag('TC0013')
    @allure.title('验证作品举报功能是否正常')
    @pytest.mark.P0
    def test_works_report(self):
        """测试作品举报功能"""
        with allure.step('获取我的昵称'):
            self.ios_comm_page.click_my_btn()
            nickname = self.my_page.get_my_nickname()
        with allure.step('点击最新tab'):
            self.ios_comm_page.click_discover()
            self.ios_comm_page.click_latest_tab()
        with allure.step('点击其他人创作的作品'):
            self.ios_comm_page.click_other_works(nickname)
        with allure.step('点击举报按钮，点击选中“色情低俗内容”'):
            self.works_detail_page.click_report_btn()
            self.works_detail_page.click_second_btn()
        with allure.step('输入原因：举报色情测试，并确定'):
            self.works_detail_page.enter_reason_and_confirm('举报色情测试')
        with allure.step('获取举报提示'):
            self.works_detail_page.get_report_success_tips()
        self.ios_comm_page.back()

    @allure.tag('TC0016')
    @allure.tag('验证作品内是否可以发表一级评论')
    @pytest.mark.P0
    def test_comment_works(self):
        """测试评论作品"""
        comment_content = f'第一级评论{generator.random_str(min_chars=3, max_chars=5)}'
        with allure.step('点击最新tab'):
            self.ios_comm_page.click_discover()
            self.ios_comm_page.click_latest_tab()
        with allure.step('点击任一作品'):
            self.ios_comm_page.click_latest_works()
        with allure.step('切换到评论'):
            self.works_detail_page.click_comment_tab()
        with allure.step('评论作品'):
            self.works_detail_page.comment_works(comment_content)
        with allure.step('获取第一个评论结果'):
            comment_result = self.works_detail_page.get_comment_result(comment_content)
        with allure.step('删除第一个评论'):
            self.works_detail_page.delete_first_comment(comment_content)
        with allure.step('获取删除评论结果'):
            delete_comment_tips_result = self.works_detail_page.get_toast_tips('删除成功')
            comment_del_result = self.works_detail_page.get_comment_result(comment_content)
        with allure.step('断言评论结果和删除后的结果'):
            self.assert_true(comment_result)
            self.assert_true(delete_comment_tips_result)
            self.assert_false(comment_del_result)

    @allure.tag('TC0017')
    @allure.tag('验证作品内是否可以发表二、三级评论')
    @pytest.mark.P0
    def test_comment_works_2_3(self):
        """测试评论作品, 可以发表二、三级评论"""
        first_comment_content = f'第一级评论{generator.random_str(min_chars=3, max_chars=5)}'
        second_comment_content = f'第二级评论{generator.random_str(min_chars=3, max_chars=5)}'
        third_comment_content = f'第三级评论{generator.random_str(min_chars=3, max_chars=5)}'
        with allure.step('点击最新tab'):
            self.ios_comm_page.click_discover()
            self.ios_comm_page.click_latest_tab()
        with allure.step('点击任一作品'):
            self.ios_comm_page.click_latest_works(number=1)
        with allure.step('切换到评论'):
            self.works_detail_page.click_comment_tab()
        with allure.step('评论作品'):
            self.works_detail_page.comment_works(first_comment_content)
        with allure.step('获取第一个评论结果'):
            first_comment_result = self.works_detail_page.get_comment_result(first_comment_content)
        with allure.step('点击一级评论，进行评论'):
            self.works_detail_page.click_comment(first_comment_content)
            self.works_detail_page.comment_works(second_comment_content)
        with allure.step('获取二级评论结果'):
            second_comment_result = self.works_detail_page.get_comment_result(second_comment_content)
        with allure.step('点击二级评论, 获取标题结果为：1条回复'):
            self.works_detail_page.click_comment(second_comment_content)
            nav_title_result = self.works_detail_page.get_nav_bar_title('1条回复')
        with allure.step('点击二级评论，进行评论'):
            self.works_detail_page.click_comment(second_comment_content, level=2)
            self.works_detail_page.comment_works(third_comment_content)
        with allure.step('获取三级评论结果'):
            third_comment_result = self.works_detail_page.get_comment_result(third_comment_content, level=2)
        with allure.step('删除第一个评论'):
            # 返回
            self.ios_comm_page.back()
            self.works_detail_page.delete_first_comment(first_comment_content)
        with allure.step('获取删除评论结果'):
            delete_comment_tips_result = self.works_detail_page.get_toast_tips('删除成功')
            comment_del_result = self.works_detail_page.get_comment_result(first_comment_content)
        with allure.step('断言评论结果、导航标题和删除后的结果'):
            self.assert_true(first_comment_result)
            self.assert_true(second_comment_result)
            self.assert_true(nav_title_result)
            self.assert_true(third_comment_result)
            self.assert_true(delete_comment_tips_result)
            self.assert_false(comment_del_result)
