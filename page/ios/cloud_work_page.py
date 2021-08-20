from base import By
from page.ios_common_page import IosCommonPage


class CloudWorkPage(IosCommonPage):
    """云端作品页面"""

    # 搜索输入框
    _search_input = (By.IOS_PREDICATE, 'type == "XCUIElementTypeStaticText" AND name == "云端作品"', '搜索输入框')
    # _search_input = (By.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "云端作品"`]', '搜索输入框')
    # 返回按钮
    _back_btn = (By.XPATH, '//*[@name="icon／24／exit"]', '返回按钮')
    # 云端作品下载按钮
    _download_btn = (By.IOS_PREDICATE, 'name == "icn work cloud download"', '作品下载按钮')
    # 作品删除按钮
    _works_del_btn = (By.IOS_PREDICATE, 'name == "icn cloud trash"', '作品删除按钮')
    # 取消删除按钮
    _cancel_del_btn = (By.IOS_PREDICATE, 'type == "XCUIElementTypeButton" AND name == "icn work cancel gray"', '取消删除按钮')
    # 确认删除按钮
    _confirm_del_btn = (By.IOS_PREDICATE, 'name == "icn work confirm gray"', '确认删除按钮')
    # 作品时间
    _with_update_del_locator = (
        By.XPATH, '//XCUIElementTypeStaticText[contains(@name,"更新")]/../preceding-sibling::XCUIElementTypeButton[2]',
        '带更新的作品')
    # works_date_time_locator = (By.IOS_PREDICATE, ' type == XCUIElementTypeStaticText AND name CONTAINS "更新"', '作品时间')
    # _clear_btn = (By.IMAGE, IosCommonPage.get_img_base64(config.clear_btn_path), '清除按钮')
    _clear_btn = (By.IOS_PREDICATE, 'name == "清除文本"', '清除文本按钮')
    # 第一个云端作品名称元素
    _first_cloud_works_name = (
        By.XPATH, '//XCUIElementTypeButton[@name="icn cloud trash"]/following-sibling::XCUIElementTypeStaticText[1]',
        '第一个云端作品名称')
    _first_cloud_works_date = (By.XPATH,
                               '//XCUIElementTypeButton[@name="icn cloud trash"]/following-sibling::XCUIElementTypeButton/XCUIElementTypeStaticText[1]',
                               '第一个云端作品创建时间')
    # 键盘删除键
    # _delete_key_btn = (By.IOS_PREDICATE, 'name == "delete"', '键盘删除键')

    _search_cancel_btn = (By.IOS_PREDICATE, 'name == "取消"', '云端搜索-取消按钮')




    def get_works_name_and_date(self):
        """获取作品名称和发布时间"""
        works_name = self.get_elements_value(self._first_cloud_works_name)
        works_date = self.get_elements_value(self._first_cloud_works_date)
        return works_name, works_date

    def is_works_exists(self, works_name, works_date):
        """检查有作品名称和发布时间的作品存在"""
        if not works_name or not works_date:
            return False
        works_name_locator = (By.IOS_PREDICATE, f'name == "{works_name}"', '作品名称')
        works_date_locator = (By.IOS_PREDICATE, f'name == "{works_date}"', '作品发布时间')
        works_name_result = self.is_element_exist(works_name_locator)
        works_date_result = self.is_element_exist(works_date_locator)
        if works_name_result and works_date_result:
            return True
        else:
            return False

    def click_search_cancel_btn(self):
        """点击搜索取消按钮"""
        self.click(self._search_cancel_btn)

    def search_cloud_word(self, keyword):
        """搜索云端作品"""
        _search_locator = [self._search_input, self._key_search_btn]
        self.submit(_search_locator, keyword)

    def is_works_name_exist(self, keywords):
        """根据关键字，判断包含关键字的作品名字元素是否存在"""
        _work_name = (By.IOS_PREDICATE, f'type == "XCUIElementTypeStaticText" AND name CONTAINS "{keywords}"', '作品名字')
        return self.is_element_exist(_work_name)

    def get_works_name_count(self, keyword):
        """根据关键字，获取包含该关键字的作品数量"""
        _work_name = (By.IOS_PREDICATE, f'type == "XCUIElementTypeStaticText" AND name CONTAINS "{keyword}"', '作品名字')
        count = self.get_group_elements_count(_work_name)
        self.logger.info(f'获取到包含关键字{keyword}的作品数量：{count}')
        return count

    def click_del_btn(self):
        """点击删除按钮"""
        self.click(self._works_del_btn)

    def cancel_delete_cloud_works(self):
        """取消删除云端作品"""
        self.click_del_btn()
        self.click(self._cancel_del_btn)

    def delete_cloud_works(self):
        """确认删除云端作品"""
        self.click_del_btn()
        self.click(self._confirm_del_btn)

    def click_download_btn(self):
        """点击下载按钮"""
        self.click(self._download_btn)

    def click_clear_btn(self):
        """点击清除按钮"""
        self.tap_element(self._clear_btn)
