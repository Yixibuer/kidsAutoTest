from page import WebCommonPage
from base import By


class HomePage(WebCommonPage):
    discover_link = (By.LINK_TEXT, '发现', '发现tab')
    forum_tab = (By.LINK_TEXT, '论坛', '论坛tab')
    work_shop_tab = (By.LINK_TEXT, '工作室', '工作室tab')
    login_enter_btn = (By.XPATH, "//span[contains(text(), '登录')]", '登录按钮')

    def click_discover_tab(self):
        self.click(self.discover_link)

    def click_forum_tab(self):
        self.click(self.forum_tab)

    def click_work_shop_tab(self):
        self.click(self.work_shop_tab)

    def to_login_page(self):
        self.click(self.login_enter_btn)
