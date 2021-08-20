from base import By
from page import IosCommonPage


class MessagePage(IosCommonPage):
    # 信封logo
    _click_message = (By.XPATH, '//XCUIElementTypeNavigationBar[@name="nemo.DiscoveryView"]/XCUIElementTypeOther')

    _click_message_op = (By.XPATH,
                         f'//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther['
                         '1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther['
                         '1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther['
                         '1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView['
                         '1]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView[1]/XCUIElementTypeCell['
                         '1]/XCUIElementTypeOther[1]/XCUIElementTypeImage[1]')

    # like收藏
    _like_and_collect = (By.XPATH, '//XCUIElementTypeStaticText[@name="点赞/收藏"]')

    # create
    _create = (By.XPATH, '//XCUIElementTypeStaticText[@name="被再创作"]')

    # 返回首页
    _return_home = (By.XPATH, '//XCUIElementTypeNavigationBar[1]/XCUIElementTypeButton[1]')

    _first_user_img = (By.XPATH, '//XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeImage[1]')

    # _first_work = (By.XPATH, '//XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeImage[1]')

    _user_detail_name = (
        By.XPATH, '//XCUIElementTypeButton[@name="关注"]/following-sibling::XCUIElementTypeStaticText[1]')

    _first_user_name = '**/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[2]'

    _first_work_name = '**/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[1]'

    _work_detail_name = '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[' \
                        '2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[' \
                        '1]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView[1]/XCUIElementTypeScrollView[' \
                        '1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView[' \
                        '1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[1] '

    def click_message(self):
        self.click(self._click_message)

    def click_create(self):
        self.click(self._create)

    def click_like_and_collect(self):
        self.click(self._like_and_collect)

    def click_return_home(self):
        self.click(self._return_home)

    def get_first_user_name(self):
        return self.driver.find_element_by_ios_class_chain(self._first_user_name).text

    def get_first_works_name(self):
        # _first_user_name = self.driver.find_element_by_ios_class_chain(self._first_user_name).text

        _first_work_name = self.driver.find_element_by_ios_class_chain(self._first_work_name).text
        return _first_work_name

    def click_first_user_img(self):
        self.click(self._first_user_img)

    def click_first_work(self):
        self.driver.find_element_by_ios_class_chain(self._first_work_name).click()

    def user_detail_name(self):
        return self.get_elements_value(self._user_detail_name)

    def is_accessibility_id_exist(self, param):
        """判断作品详情有"""
        param = param.strip()
        result = self.driver.find_element_by_accessibility_id(param).text
        return result == param
