from base import By
from page import IosCommonPage


class FindPage(IosCommonPage):
    _click_close_banner = (By.ACCESSIBILITY_ID, 'icon／24／exit黑close')

    _click_banner_share = (By.ACCESSIBILITY_ID, 'icon／24／exit黑share')

    _click_banner_share_copy_link = (By.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell[`label == "拷贝"`]')

    _click_banner_share_copy_link_close = (By.ACCESSIBILITY_ID, '关闭')

    _recommend = (By.IOS_PREDICATE, 'name == "推荐"', '最新tab')

    # 推荐页第一个作品
    _click_first_work = (By.IOS_CLASS_CHAIN, '//XCUIElementTypeStaticText['
                                             '@name="今日推荐"]/../following-sibling::XCUIElementTypeCell['
                                             '1]/XCUIElementTypeOther[0]/XCUIElementTypeOther['
                                             '0]/XCUIElementTypeOther[0]/XCUIElementTypeOther['
                                             '0]/XCUIElementTypeOther[0]/XCUIElementTypeStaticText')

    # 推荐页第一个作品-点赞
    _click_details_work_like = (By.IOS_CLASS_CHAIN, '*//XCUIElementTypeStaticText['
                                                    '@name="今日推荐"]/../following-sibling::XCUIElementTypeCell['
                                                    '1]/XCUIElementTypeOther[0]/XCUIElementTypeOther['
                                                    '0]/XCUIElementTypeOther[0]/XCUIElementTypeOther['
                                                    '0]/XCUIElementTypeOther[0]/XCUIElementTypeButton['
                                                    '1]/XCUIElementTypeStaticText')

    _click_banner = (By.XPATH, '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther['
                               '1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther['
                               '1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther['
                               '1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView['
                               '1]/XCUIElementTypeScrollView[1]/XCUIElementTypeOther['
                               '1]/XCUIElementTypeCollectionView[1]/XCUIElementTypeCell[1]/XCUIElementTypeOther['
                               '1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView['
                               '1]/XCUIElementTypeCell[2]')
    # 获取作品详情点赞数
    _work_like_count = (By.XPATH,
                        '//XCUIElementTypeImage[@name="icon／24／browse-10"]/../following-sibling'
                        '::XCUIElementTypeOther[1]/XCUIElementTypeStaticText',
                        '作品详情-点赞数')

    # 最新页tab
    _latest_tab = (By.IOS_PREDICATE, 'name == "最新"', '最新tab')

    def left_slide_one_banner(self):
        self.driver.execute_script("mobile:dragFromToForDuration",
                                   {"duration": 0.5, "element": None,
                                    "fromX": 300, "fromY": 220,
                                    "toX": 100, "toY": 220})

    def right_slide_one_banner(self):
        self.driver.execute_script("mobile:dragFromToForDuration",
                                   {"duration": 0.5, "element": None,
                                    "fromX": 100, "fromY": 220,
                                    "toX": 300, "toY": 220})

    def up_slide_one_banner(self):
        self.driver.execute_script("mobile:dragFromToForDuration",
                                   {"duration": 0.5, "element": None,
                                    "fromX": 180, "fromY": 650,
                                    "toX": 180, "toY": 300})

    def right_to_left_slide(self):
        self.driver.execute_script("mobile:dragFromToForDuration",
                                   {"duration": 0.5, "element": None,
                                    "fromX": 290, "fromY": 335,
                                    "toX": 90, "toY": 335})

    def left_to_right_slide(self):
        self.driver.execute_script("mobile:dragFromToForDuration",
                                   {"duration": 0.5, "element": None,
                                    "fromX": 90, "fromY": 335,
                                    "toX": 290, "toY": 335})

    def click_banner(self):
        self.click(self._click_banner)

    def click_close_banner(self):
        self.click(self._click_close_banner)

    def click_banner_share(self):
        self.click(self._click_banner_share)

    def click_banner_share_copy_link(self):
        self.click(self._click_banner_share_copy_link)

    def click_banner_share_copy_link_close(self):
        self.click(self._click_banner_share_copy_link_close)

    def click_recommend(self):
        self.click(self._recommend)

    def is_element_exist_theme_tab(self):
        """获取主题tab"""
        return self.is_element_exist(self._recommend)

    def is_element_exist_latest_tab(self):
        """获取最新tab"""
        return self.is_element_exist(self._latest_tab)

    def is_element_exist_recommend_tab(self):
        """获取推荐tab"""
        return self.is_element_exist(self._recommend_tab)

    def get_last_works_creator_name(self):
        """获取最新作品-创作者名称"""
        return self.get_elements_value(self._first_works_creator_name)

    def get_recommend_first_work_name_and_like(self):
        """获取发现-推荐tab-第一个作品点赞数"""
        _recommend_first_works_name = (
            By.IOS_CLASS_CHAIN, '',
            '第一个作品name')
        _recommend_first_works_like = (
            By.IOS_CLASS_CHAIN, '',
            '第一个作品like')
        work_name = self.get_elements_value(_recommend_first_works_name)
        work_like = self.get_elements_value(_recommend_first_works_like)
        return work_name, work_like

    def get_details_works_name_and_creator_name(self):
        _works_name = (
            By.IOS_CLASS_CHAIN, '',
            '详情-作品名称')

        _creator_name = (
            By.IOS_CLASS_CHAIN, '',
            '详情-作品创作者')
        works_name = self.get_elements_value(_works_name)
        creator_name = self.get_elements_value(_creator_name)
        return works_name, creator_name

    def click_last_tab(self):
        self.click(self._latest_tab)

    def click_first_work(self):
        self.click(self._click_first_work)

    def click_details_work_like(self):
        self.click(self._click_details_work_like)

    def get_details_like_count(self):
        """获取作品详情页的点赞数"""
        return int(self.get_elements_value(self._work_like_count))
