from base import By
from page import IosCommonPage


class TemplatePage(IosCommonPage):
    _artboard = (By.ACCESSIBILITY_ID, "Artboard", "点击 + 按钮")
    _add_template = (By.IOS_CLASS_CHAIN, "**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther"
                                         "/XCUIElementTypeOther/XCUIElementTypeOther["
                                         "2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]",
                                         "创作页面")
    _immediately_create = (By.IOS_PREDICATE, 'label == "立即创作" AND name == "立即创作" AND value == "立即创作"', "立即创作")
    _template_menu_but = (By.ACCESSIBILITY_ID, 'icon 创作 导航 更多未激活', "模板作品菜单按钮")
    _template_out_but = (By.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "退出"`]', "模板作品-退出按钮")
    _out_page_ok = (By.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "好的"`]', "退出页面-好的")
    _out_page_no = (By.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "不用了"`]', "退出页面-不用了")
    # 我的-第一个作品 创建时间
    _my_page_first_work_time = '**/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[1]'
    _by_name_immediately_create = (By.NAME, '立即创作', '立即创作')

    # 点击首页"+"添加模板
    def click_add(self):
        self.click(self._artboard)

    # 点击从模板中创建
    def click_template_work(self):
        self.click(self._add_template)

    # 选择模板页面->点击立即创建
    def click_immediately_create(self):
        self.click(self._immediately_create)

    # 选择模板页面->点击立即创建->模板菜单按钮
    def click_template_menu_op(self):
        self.click(self._template_menu_but)

    # 选择模板页面->点击立即创建->退出按钮
    def click_template_out_but(self):
        self.click(self._template_out_but)

    # 选择模板页面->点击立即创建->退出按钮-点击退出页面"好的"
    def click_out_page_ok(self):
        self.click(self._out_page_ok)

    # 选择模板页面->点击立即创建->退出按钮-点击退出页面"好的"
    def get_my_page_first_work_time(self):
        return self.driver.find_element_by_ios_class_chain(self._my_page_first_work_time).text

    # 选择模板页面->点击立即创建->退出按钮-点击退出页面"不用了"
    def click_out_page_no(self):
        self.click(self._out_page_no)

    # 是否存在name="立即创作"
    def is_by_name_immediately_create(self):
        return self.is_element_exist(self._by_name_immediately_create)


