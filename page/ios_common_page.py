#!/usr/bin/env python
# coding=utf-8
from base import IosPage
from base import By
from utils import data


class IosCommonPage(IosPage):
    """IOS公共页面常用的元素和公共方法

    common_page主要用于公共页面元素和公共方法的封装，所有页面共用

    元素示例：
        由定位方式，定位的值，元素信息组成，
        locator = (By.ID, 'element_id', "元素信息")  元素信息可选，主要用于打印调试日志以及方便后期维护元素
        或
        locator = (By.ID, 'element_id')

    常用定位示例：
    底部-我的按钮-
        _my_btn = (By.IOS_PREDICATE, 'type == "XCUIElementTypeButton" AND name == "我的"', '底部-我的按钮')
        _my_btn = (By.IOS_PREDICATE, 'type == "XCUIElementTypeButton" AND name CONTAINS "我的"', '底部-我的按钮')
        _my_btn = (By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "我的"`]', '底部-我的按钮')
        _my_btn = (By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name CONTAINS "我的"`]', '底部-我的按钮')
        _my_btn = (By.ACCESSIBILITY_ID, '我的', '底部-我的按钮')
        _my_btn = (By.XPATH, '//*[@name="我的"]', '底部-我的按钮')

    页面操作封装

    直接调用base_page, mobile_page提供的方法即可

    def step(self):
        self.xx(self.locator)

    """
    # 页面标识，用与不同页面获取类似元素，封装操作步骤
    LATEST_PAGE = '发现-最新页面'
    MY_DRAFT_PAGE = '我的-草稿箱页面'
    # 入口页面-编程猫账号
    _codemao_act_btn = (By.IOS_PREDICATE, 'type == "XCUIElementTypeButton" AND name == "账号登录/注册"', '编程猫账号按钮')
    # 登录页面元素
    _username_input = (By.CLASS_NAME, 'XCUIElementTypeTextField', '用户名输入框')
    _password_input = (By.CLASS_NAME, 'XCUIElementTypeSecureTextField', '密码输入框')
    _login_btn = (By.IOS_PREDICATE, 'name == "登 录"', '登录按钮')
    _login_locator = [_username_input, _password_input, _login_btn]
    # 底部-发现按钮
    _discover_btn = (By.IOS_PREDICATE, 'name == "发现"', '底部-发现按钮')
    # 底部-创作按钮
    _add_btn = (By.IOS_PREDICATE, 'name == "Artboard"', '底部-创作按钮')
    # 自由创作按钮
    _free_creation_btn = (By.IOS_PREDICATE, 'name == "原画／创作自由"', '自由创作按钮')
    # 有name属性即可
    # _free_creation_btn = (By.ACCESSIBILITY_ID, '原画／创作自由', '自由创作按钮')
    # 底部-我的按钮
    _my_btn = (By.IOS_PREDICATE, 'name == "我的"', '底部-我的按钮')
    # 顶部tab
    # 推荐
    _recommend_tab = (By.IOS_PREDICATE, 'name == "推荐"', '推荐tab')
    # 最新tab
    _latest_tab = (By.IOS_PREDICATE, 'name == "最新"', '最新tab')
    # 最新tab-第一个单元格
    _first_works_cell = (By.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[1]', '第一个作品单元格')
    # 最新tab-第一个作品
    _first_works_creator_name = (
        By.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[3]',
        '第一个作品作者名字')
    # 作品单元格
    _works_cell = (By.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable/XCUIElementTypeCell', '作品单元格')
    _first_works_like_count = (By.IOS_CLASS_CHAIN,
                               '**/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeButton[2]/XCUIElementTypeStaticText[1]',
                               '最新作品列表-第一个作品点赞数')
    _creator_nickname_locator = (By.XPATH, '//XCUIElementTypeCell/XCUIElementTypeStaticText[3]', '最新列表-创作者昵称')
    _last_bottom_tips = (By.IOS_PREDICATE, 'name == "喵~已经到最后啦!"', '页面划到最后的提示')
    # 发现-搜索框
    _search_box = (By.IOS_PREDICATE, 'name == "搜索用户和作品"', '搜索用户和作品框')
    # 搜索按钮
    _search_btn = (By.IOS_PREDICATE, 'name == "icn nav search black"', '云端作品页-搜索按钮')
    _search_input = (By.IOS_CLASS_CHAIN,
                     '**/XCUIElementTypeNavigationBar[`name == "nemo.IndividualSearch"`]/XCUIElementTypeStaticText[1]/XCUIElementTypeTextField[1]',
                     '我的页面-搜索输入框')
    # 键盘搜索按钮
    _key_search_btn = (By.IOS_PREDICATE, 'name == "Search"', '键盘搜索按钮')
    _search_locator = [_search_input, _key_search_btn]
    _draft_tab_btn = (By.IOS_PREDICATE, 'name == "草稿箱"', '搜索结果-草稿箱按钮')
    _published_btn = (By.IOS_PREDICATE, 'name == "已发布"', '搜索结果页-已发布按钮')
    _play_btn = (By.IOS_PREDICATE, 'name == "icon／96／play 3"', '作品详情-播放按钮')
    # 用户协议弹窗-同意按钮
    _accept_btn = (By.IOS_PREDICATE, 'name == "同意"', '用户协议弹窗-同意按钮')
    _screenshot_btn = (By.IOS_PREDICATE, 'name == "player jietu"', '作品播放页-截图按钮')
    _player_collect_btn = (By.IOS_PREDICATE, 'name == "icon 24 favorite normal"', '作品播放页-收藏按钮')
    _player_like_btn = (By.IOS_PREDICATE, 'name == "icon 24 support normal"', '作品播放页-点赞按钮')
    _close_btn = (By.IOS_PREDICATE, 'name == "icon／24／关闭白"', '作品播放页-关闭按钮')
    _reset_btn = (By.IOS_PREDICATE, 'name == "icon／24／关闭白 3"', '作品播放页-重置按钮')
    _player_locators = [_screenshot_btn, _player_collect_btn, _player_like_btn, _reset_btn]
    _select_all_btn = (By.IOS_PREDICATE, 'name == "全选"', '输入框长按-全选按钮')
    _keyboard_back_btn = (By.IOS_PREDICATE, 'name == "delete"', '键盘回退按钮')
    _keyboard_space_btn = (By.IOS_PREDICATE, 'name == "space"', '键盘空格按钮')

    def click_back_keys(self):
        """点击键盘回退键"""
        self.click(self._keyboard_back_btn)

    def select_all_and_delete(self):
        """输入框全选再删除"""
        self.click(self._select_all_btn)
        self.click(self._keyboard_back_btn)

    def click_accept_btn(self):
        """点击用户协议弹窗-同意按钮"""
        self.click(self._accept_btn)

    def get_recommend(self):
        """获取推荐tab"""
        return self.is_element_exist(self._recommend_tab)

    def click_codemao_act(self):
        """点击入口页面-编程猫账号"""
        self.click(self._codemao_act_btn)
        # self.click_existing_element(self._accept_btn)

    def click_free_creation_btn(self):
        """点击自由创作按钮"""
        self.tap_element(self._free_creation_btn)

    def login(self, test_data=data.valid_tel_pwd):
        """登录方法"""
        # 默认正常账号登录
        self.submit(self._login_locator, test_data)

    def search(self, keyword):
        """发现页搜索"""
        self.click(self._search_box)
        self.submit(self._search_locator, keyword)

    def click_search_works(self, level=1):
        """点击搜索的作品，默认点击第一个"""
        _search_works_img = (By.XPATH, f'//XCUIElementTypeCell[{level}]/XCUIElementTypeImage[1]', '搜索结果页-作品缩略图')
        self.tap_element(_search_works_img)

    def click_add_btn(self):
        """点击创作按钮"""
        self.click(self._add_btn)

    def click_discover(self):
        """点击发现"""
        self.click(self._discover_btn)

    def click_my_btn(self):
        """点击我的"""
        self.click(self._my_btn)

    def click_latest_tab(self):
        """点击最新"""
        self.click(self._latest_tab)

    # def get_first_works_name(self):
    #     """获取第一个作品名称"""
    #     works_name = self.get_elements_value(self._first_works_name)
    #     self.logger.info(f'获取到的第一个作品名称: {works_name}')
    #     return works_name

    def get_works_name(self, level=1, page=LATEST_PAGE):
        """获取不同列表页的作品名称, 默认获取最新列表第一个作品名称"""
        # 最新页面
        if page == self.LATEST_PAGE:
            works_name_locator = (
                By.IOS_CLASS_CHAIN,
                f'**/XCUIElementTypeTable[1]/XCUIElementTypeCell[{level}]/XCUIElementTypeStaticText[1]',
                '作品名称')
            works_name = self.get_elements_value(works_name_locator)
        # 我的页面-草稿箱
        if page == self.MY_DRAFT_PAGE:
            works_name_locator = (
                By.IOS_CLASS_CHAIN,
                f'**/XCUIElementTypeTable[1]/XCUIElementTypeCell[{level}]/XCUIElementTypeStaticText[2]',
                '草稿箱-作品名称')
            works_name = self.get_elements_value(works_name_locator)
        self.logger.info(f'获取到的第{level}个作品名称: {works_name}')
        return works_name

    def get_works_creator_name(self, level=1):
        """获取作品的创作者名称, 默认获取第一个"""
        _works_creator_name = (
            By.IOS_CLASS_CHAIN, f'**/XCUIElementTypeTable[1]/XCUIElementTypeCell[{level}]/XCUIElementTypeStaticText[3]',
            '作者昵称')
        works_creator_name = self.get_elements_value(_works_creator_name)
        self.logger.info(f'获取到的第{level}个作品创作者名字: {works_creator_name}')
        return works_creator_name

    def click_latest_works(self, number=1):
        """最新tab，默认点击第一个作品"""
        _works_name = (
            By.IOS_CLASS_CHAIN,
            f'**/XCUIElementTypeTable[1]/XCUIElementTypeCell[{number}]/XCUIElementTypeStaticText[1]', '最新作品名称')
        self.click(_works_name)

    def get_first_works_like_count(self):
        """获取最新作品列表，第一个作品点赞数"""
        return int(self.get_elements_value(self._first_works_like_count))

    def get_works_count(self):
        """通过作品单元格，获取作品数量"""
        works_count = self.get_group_elements_count(self._works_cell)
        self.logger.info(f'获取到的作品数量：{works_count}')
        return works_count

    def click_other_works(self, nickname):
        """点击最新tab,不是自己创作的作品"""
        # 获取当前页的所有的创作者昵称
        flag = False
        while not flag:
            creator_nickname_list = self.get_group_elements_value(self._creator_nickname_locator)
            for name in creator_nickname_list:
                _other_works = (
                    By.XPATH, f'//XCUIElementTypeStaticText[@name="{name}"]/parent::XCUIElementTypeCell[1]', '其他人创作的作品')
                if name != nickname:
                    # 点击其他人创作的作品
                    self.click(_other_works)
                    flag = True
                    break
            # 没有匹配到其他人的作品，则滑动到下一页，滑动到底部则停止
            if not flag:
                if self.is_element_exist(self._last_bottom_tips, sleep_time=3):
                    self.logger.info('没有获取到其他人的作品')
                    break
                self.swipe_to_down()

    def click_search_btn(self):
        """点击搜索按钮"""
        self.click(self._search_btn)

    def search_works(self, name):
        """搜索作品"""
        self.submit(self._search_locator, name)

    def get_toast_tips(self, tips):
        """获取弹窗提示"""
        _tips_locator = (By.IOS_PREDICATE, f'name == "{tips}"', f'{tips}弹窗提示')
        return self.is_element_exist(_tips_locator, sleep_time=5)

    def click_published_btn(self):
        """切换到已发布列表"""
        self.click(self._published_btn)

    def search_my_works(self, works_name):
        """搜索我的已发布作品"""
        self.click_search_btn()
        self.search_works(works_name)
        self.click_published_btn()

    def click_my_earch_works(self, level=1):
        """点击搜索到的作品, 默认点击第一个"""
        _locator = (
            By.IOS_CLASS_CHAIN, f'**/XCUIElementTypeTable[1]/XCUIElementTypeCell[{level}]/XCUIElementTypeImage[1]',
            '搜索结果-作品缩略图')
        self.tap_element(_locator)

    def click_play_btn(self):
        """点击作品播放页"""
        self.click(self._play_btn)

    def click_player_play_btn(self):
        """进入player后点击播放"""
        self.touch('play.png')

    def enter_player(self, works_name):
        """进入player播放页面"""
        self.click_my_btn()
        self.search_my_works(works_name)
        self.click_my_earch_works()
        self.click_play_btn()
        self.click_player_play_btn()

    def click_player_reset_btn(self):
        """player作品重置"""
        self.click(self._reset_btn)
