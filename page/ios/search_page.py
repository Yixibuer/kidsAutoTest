from base import By
from page import IosCommonPage


class SearchPage(IosCommonPage):
    # 搜索logo
    _search_text = (By.XPATH, '//XCUIElementTypeNavigationBar[@name=\"nemo.DiscoveryView\"]/XCUIElementTypeStaticText')

    # 作品列表搜索结果第一条数据
    # _first_work_name = (By.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "测试侦测类"`][1]')

    _first_work_name = "**/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[4]"

    _user_tab = (By.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "用户"`]')

    # 用户列表搜索结果第一条数据
    _first_username = (By.XPATH, '//XCUIElementTypeStaticText[@name="测试"]')

    _keyboard_search_btn = '//XCUIElementTypeButton[@name=" '
    '大家都在搜"]/preceding-sibling::XCUIElementTypeButton[1]'

    # 搜索结果页面-用户tab
    _search_user_tab = (By.XPATH, '//XCUIElementTypeStaticText[@name="用户"]', '搜索结果页面-用户tab')

    _first_user_name = "**/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[1]"

    def click_search(self):
        self.click(self._search_text)

    def input_search_text(self, content):
        self.submit(self._search_text, content)

    def click_keyboard_search_btn(self):
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name=" '
                                          '大家都在搜"]/preceding-sibling::XCUIElementTypeButton['
                                          '1]/XCUIElementTypeStaticText[1]').click()

    def get_search_name(self):
        return self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name=" '
                                                 '大家都在搜"]/preceding-sibling::XCUIElementTypeButton['
                                                 '1]/XCUIElementTypeStaticText[1]').text

    def get_tab_first_work_name(self):
        return self.driver.find_element_by_ios_class_chain(self._first_work_name).text

    def click_search_user_tab(self):
        self.click(self._search_user_tab)

    def get_tab_first_user_name(self):
        return self.driver.find_element_by_ios_class_chain(self._first_user_name).text
