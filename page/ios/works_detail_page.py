from base import By
from page import IosCommonPage
from utils import config


class WorksDetailPage(IosCommonPage):
    """作品详情页面"""
    _collect_btn = (By.XPATH,
                    '//XCUIElementTypeImage[@name="icon／24／browse-10"]/../preceding-sibling::XCUIElementTypeOther['
                    '1]/XCUIElementTypeImage',
                    '作品详情-收藏按钮')
    _share_btn = (By.IOS_PREDICATE, 'name == "icon／24／browse-10"', '作品详情-分享按钮')
    _copy_link_btn = (By.IOS_PREDICATE, 'name == "复制链接"', '作品分享-复制链接')
    _like_btn = (By.XPATH,
                 '//XCUIElementTypeImage[@name="icon／24／browse-10"]/../following-sibling::XCUIElementTypeOther['
                 '1]/XCUIElementTypeImage',
                 '作品详情-点赞按钮')
    _works_like_count = (By.XPATH,
                         '//XCUIElementTypeImage[@name="icon／24／browse-10"]/../following-sibling'
                         '::XCUIElementTypeOther[1]/XCUIElementTypeStaticText',
                         '作品详情-点赞数')
    _favored_count = (By.XPATH,
                      '//XCUIElementTypeImage[@name="icon／24／browse-10"]/../preceding-sibling::XCUIElementTypeOther['
                      '1]/XCUIElementTypeStaticText',
                      '作品详情收藏数')
    _follow_btn = (By.IOS_PREDICATE, 'name == "关注"', '作品详情-关注按钮')
    _following_btn = (By.IOS_PREDICATE, 'name == "已关注"', '作品详情-已关注按钮')
    _creator_avatar = (
        By.XPATH, '//XCUIElementTypeStaticText[contains(@name, "关注")]/../preceding-sibling::XCUIElementTypeButton[2]',
        '头像')
    _unsubscribe_tips = (By.IOS_PREDICATE, 'name == "已取消关注"', '已取消关注tips')
    _right_menu_btn = (
        By.IOS_CLASS_CHAIN,
        '**/XCUIElementTypeNavigationBar[`name == "nemo.WorksDetailView"`]/XCUIElementTypeButton[2]',
        '顶部右侧三点按钮')
    _report_btn = (By.IOS_PREDICATE, 'name == "举报"', '举报按钮')
    _second_options = (By.IOS_PREDICATE, 'name == "色情低俗"', '色情低俗按钮')
    _report_textview = (By.IOS_PREDICATE, 'type == "XCUIElementTypeTextView"', '举报内容输入框')
    _report_confirm_btn = (By.IOS_PREDICATE, 'type == "XCUIElementTypeStaticText" AND name == "确定"', '举报-确定按钮')
    _keyboard_done_btn = (By.IOS_PREDICATE, 'name == "Done"', '键盘Done按钮')
    # _report_locators = [_report_textview, _report_confirm_btn]
    _comment_tab = (By.IOS_PREDICATE, 'type == "XCUIElementTypeStaticText" AND name CONTAINS "评论"', '评论tab')
    _comment_input = (By.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextView[1]', '评论输入框')
    _send_btn = (By.IOS_PREDICATE, 'name == "发送"', '发送按钮')
    _comment_locator = [_comment_input, _send_btn]
    _comment_del_btn = (By.IOS_PREDICATE, 'name == "删除"', '作品评论-删除按钮')
    _comment_del_confirm_btn = (By.IOS_PREDICATE, 'type == "XCUIElementTypeButton" AND name == "确定"', '删除评论确定按钮')
    _play_confirm_btn = (
        By.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "编程猫"`]/XCUIElementTypeOther[1]', '确认播放按钮')
    _create_again_btn = (
        By.XPATH,
        '//*[@name="icon／24／browse-10"]/../preceding-sibling::XCUIElementTypeOther[2]/XCUIElementTypeImage[1]',
        '再创作按钮')
    _learn_code_btn = (By.IOS_PREDICATE, 'name == "学习代码"', '学习代码按钮')
    _detail_works_name = (
        By.XPATH, '//*[contains(@name, "关注")]/ancestor::XCUIElementTypeOther[2]/XCUIElementTypeStaticText[1]',
        '作品详情页-作品名称')
    _create_again_count = (By.XPATH,
                           '//*[@name="icon／24／browse-7"]/../following-sibling::XCUIElementTypeOther[1]/XCUIElementTypeStaticText[1]',
                           '作品详情页-再创作数')
    _open_later_btn = (By.IOS_PREDICATE, 'name == "稍后打开"', '作品再创作弹窗-稍后打开')

    def click_collect_btn(self):
        """作品详情页，点击收藏"""
        self.tap_element(self._collect_btn)

    def click_share_btn(self):
        """作品详情，点击分享"""
        self.tap_element(self._share_btn)

    def click_copy_link(self):
        """作品分享-点击复制链接"""
        self.click(self._copy_link_btn)

    def get_copy_success_tips(self, tips):
        """获取复制链接成功提示"""
        _copy_success_tips = (By.IOS_PREDICATE, f'name == "{tips}"', '复制链接成功提示')
        return self.is_element_exist(_copy_success_tips)

    def click_like_btn(self):
        """点击点赞按钮"""
        self.tap_element(self._like_btn)

    def get_details_like_count(self):
        """获取作品详情页的点赞数"""
        return int(self.get_elements_value(self._works_like_count))

    def get_favored_count(self):
        """获取作品的收藏数目"""
        return int(self.get_elements_value(self._favored_count))

    def set_as_unlike(self):
        """作品置为未点赞的状态"""
        bf_like_count = self.get_details_like_count()
        if bf_like_count == 0:
            return
        else:
            self.click_like_btn()
            af_like_count = self.get_details_like_count()
            if af_like_count - bf_like_count == 1:
                # 没有点赞的，再次点赞，还原
                self.click_like_btn()
            else:
                # 点过赞的不做处理，第一步点赞就取消了
                pass

    def set_as_unfavored(self):
        """作品置为未收藏的状态"""
        favor_count = self.get_favored_count()
        if favor_count == 0:
            return
        else:
            self.click_collect_btn()
            af_favor_count = self.get_favored_count()
            if af_favor_count - favor_count == 1:
                # 再次点击收藏，还原状态
                self.click_collect_btn()

    def is_works_name_and_creator_exist(self, works_name, creator_name):
        """判断作品详情有"""
        works_name_locator = (By.IOS_PREDICATE, f'name == "{works_name}"')
        creator_name_locator = (By.IOS_PREDICATE, f'name == "{creator_name}"')
        works_name_result = self.is_element_exist(works_name_locator)
        creator_name_result = self.is_element_exist(creator_name_locator)
        if works_name_result and creator_name_result:
            return True
        else:
            return False

    def click_follow_btn(self):
        """点击关注"""
        if self.is_element_exist(self._follow_btn, sleep_time=5):
            self.click(self._follow_btn)
        elif self.is_element_exist(self._following_btn, sleep_time=5):
            # 取消关注
            self.click(self._following_btn)
            # 再次关注
            self.click(self._follow_btn)

    def click_following_btn(self):
        """点击已关注按钮"""
        self.click(self._following_btn)

    def click_avatar(self):
        """点击头像"""
        self.click(self._creator_avatar)

    def get_unsubscribe_tips(self):
        """获取取消关注的提示"""
        if self.is_element_exist(self._unsubscribe_tips):
            return True
        else:
            return False

    def click_report_btn(self):
        """作品详情，点击举报"""
        self.click(self._right_menu_btn)
        self.click(self._report_btn)

    def click_second_btn(self):
        """选择色情低俗按钮"""
        self.click(self._second_options)

    def enter_reason_and_confirm(self, reason):
        """输入举报原因并确定"""
        self.send_keys(self._report_textview, reason)
        self.click(self._keyboard_done_btn)
        self.click(self._report_confirm_btn)
        # self.submit(self._report_locators, reason)

    def get_report_success_tips(self):
        """获取举报成功的提示"""
        report_tips = (By.IOS_PREDICATE, 'name CONTAINS "感谢您对Nemo社区的支持"', '举报提示')
        report_success_tips = (By.IOS_PREDICATE, 'name CONTAINS "举报提交成功"', '举报提交成功提示')
        if self.is_element_exist(report_tips) and self.is_element_exist(report_success_tips):
            return True
        else:
            return False

    def click_comment_tab(self):
        """点击评论tab"""
        self.click(self._comment_tab)

    def comment_works(self, content):
        """评论"""
        # self.click(self._comment_input)
        self.submit(self._comment_locator, content)

    def get_comment_result(self, content, level=1):
        """获取作品评论内容是否存在, 默认获取一级评论"""
        comment_content = (
            By.XPATH,
            f'//XCUIElementTypeCell[{level}]/descendant::XCUIElementTypeStaticText[contains(@name, "{content}")]',
            '第一条评论的内容')
        return self.is_element_exist(comment_content, sleep_time=5)

    def delete_first_comment(self, content):
        """删除第一个评论"""
        first_comment_more_btn = (By.XPATH,
                                  f'//XCUIElementTypeStaticText[contains(@name, "{content}")]/../following-sibling::XCUIElementTypeButton[1]',
                                  '第一条评论的更多按钮')
        self.click(first_comment_more_btn)
        self.click(self._comment_del_btn)
        self.click(self._comment_del_confirm_btn)

    def click_comment(self, content, level=1):
        """点击评论内容(默认点击一级评论)"""
        comment_content = (
            By.XPATH,
            f'//XCUIElementTypeCell[{level}]/descendant::XCUIElementTypeStaticText[contains(@name, "{content}")]',
            '第一条评论的内容')
        self.click(comment_content)

    def get_nav_bar_title(self, title):
        """获取导航栏标题"""
        _nav_bar_title = (
            By.IOS_CLASS_CHAIN, f'**/XCUIElementTypeNavigationBar/XCUIElementTypeStaticText[`name == "{title}"`]',
            "导航栏标题")
        return self.is_element_exist(_nav_bar_title, sleep_time=5)

    def check_player_element(self):
        """检查播放页元素"""
        return self.is_elements_exist(self._player_locators)

    def click_close_player(self):
        """点击关闭player按钮"""
        self.click(self._close_btn)

    def click_create_again(self):
        """点击再创作"""
        self.tap_element(self._create_again_btn)

    def get_create_again_title(self, tips):
        """获取再创作的title"""
        # locator = (By.IOS_PREDICATE, 'name == "再创作也是学习的方式哦！"', '再创作也是学习的方式哦')
        title_locator = self.generate_mobile_locator(tips)
        return self.is_element_exist(title_locator)

    def click_learn_code(self):
        """点击学习代码"""
        self.click(self._learn_code_btn)

    def get_details_work_name(self):
        """获取作品详情页-作品名称"""
        works_name = self.get_elements_value(self._detail_works_name)
        self.logger.info(f'品详情页-作品名称:{works_name}')
        return works_name

    def get_create_again_count(self):
        """获取再创作的数目"""
        return int(self.get_elements_value(self._create_again_count))

    def click_open_later(self):
        """点击稍后打开"""
        self.click(self._open_later_btn)
        return self.is_img_exists(config.open_later_tips)
