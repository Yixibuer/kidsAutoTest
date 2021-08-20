from page import IosCommonPage
from base import By


class UserDetail(IosCommonPage):
    """用户详情页面"""

    _collection_btn = (By.IOS_PREDICATE, 'name == "收藏"', '收藏入口')
    _fans_btn = (By.IOS_PREDICATE, 'name == "粉丝"', '粉丝')

    def click_collection_btn(self):
        """点击收藏按钮，进入收藏页面"""
        self.tap_element(self._collection_btn)

    def click_fans_btn(self):
        """点击粉丝"""
        self.tap_element(self._fans_btn)

    def get_fans_result(self, nickname):
        """获取粉丝"""
        fans_name = (By.IOS_PREDICATE, f'name == "{nickname}"', '粉丝昵称')
        flag = False
        while not flag:
            # 获取到粉丝名字即返回True
            if self.is_element_exist(fans_name, sleep_time=5):
                return True
            # 滑动到底部停止循环
            elif self.is_element_exist(self._last_bottom_tips, sleep_time=3):
                flag = True
            # 其他情况继续滑动
            else:
                self.swipe_to_down()
        return False

