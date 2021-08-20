from base import By
from page import IosCommonPage


class CreationPage(IosCommonPage):
    """创作页面"""
    _top_more_btn = (By.IOS_PREDICATE, 'name == "icon 创作 导航 更多未激活"', '顶部四点-更多按钮')
    _exit_btn = (By.IOS_PREDICATE, 'name == "退出"', '顶部-退出按钮')
    _publish_btn = (By.IOS_PREDICATE, 'name == "发布"', '顶部四点-发布按钮')
    _help_btn = (By.IOS_PREDICATE, 'name == "帮助"', '顶部四点-帮助按钮')
    _top_locators = [_publish_btn, _help_btn]

    def click_more_btn(self):
        """点击更多按钮"""
        self.click(self._top_more_btn)

    def get_top_element(self):
        """获取顶部的元素"""
        return self.is_elements_exist(self._top_locators)

    def click_exit_btn(self):
        """点击退出按钮"""
        self.click(self._exit_btn)