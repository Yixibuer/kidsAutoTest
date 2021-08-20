from page import IosCommonPage
from base import By
from utils import data


class LoginPage(IosCommonPage):
    """页面类示例
    页面类一般推荐继承对应的common_page，

    common_page主要用于公共页面元素和公共方法的封装，所有页面共用

    元素示例：
    由定位方式，定位的值，元素信息组成，
    locator = (By.ID, 'element_id', "元素信息")  元素信息可选，主要用于打印调试日志以及方便后期维护元素
    或
    locator = (By.ID, 'element_id')

    页面操作封装

    直接调用base_page, mobile_page提供的方法即可

    def step(self):
        self.xx(self.locator)

    """
    # 新用户注册按钮
    _register_btn = (By.XPATH, '//XCUIElementTypeStaticText[@name="新用户注册"]')
    # 忘记密码
    _forgot_pwd_btn = (By.XPATH, '//XCUIElementTypeStaticText[@name="忘记密码"]', '忘记密码按钮')
    # 错误提示
    user_or_pwd_error_tips = (By.IOS_PREDICATE, 'type == "XCUIElementTypeStaticText" AND name == "用户或者密码不正确"')

    def click_to_register_page(self):
        """点击跳转到注册页面"""
        self.click(self._register_btn)
        # self.sleep(1)

    def click_to_forgot_pwd_page(self):
        """点击跳转到忘记密码页面"""
        self.click(self._forgot_pwd_btn)
        self.back()

    def get_error_tips(self):
        """
        获取登录失败的错误提示
        """
        return self.get_elements_text(self.user_or_pwd_error_tips)

    def get_my_btn(self):
        """获取我的按钮"""
        return self.is_element_exist(self._my_btn)
