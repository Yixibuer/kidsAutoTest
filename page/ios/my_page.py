from page import IosCommonPage
from base import By


class MyPage(IosCommonPage):
    """我的页面"""
    # 云端作品入口icon
    _cloud_icon = (By.XPATH, '//*[@name="icn clound black"]', '云端作品入口icon')
    # 草稿箱元素
    _draft_tab = (By.IOS_PREDICATE, 'name CONTAINS "草稿箱"', '草稿箱元素')
    _published_tab = (By.IOS_PREDICATE, 'name CONTAINS "已发布"', '草稿箱元素')
    _right_arrow_icon = (By.IOS_PREDICATE, 'name == "icn_arrow_right_white"', '右箭头图标')
    # 我的昵称
    _my_nickname = (By.XPATH,
                    '//XCUIElementTypeImage[@name="icn_arrow_right_white"]/preceding-sibling::XCUIElementTypeButton[1]/XCUIElementTypeStaticText',
                    '用户昵称')
    # 复制按钮
    _copy_btn = (By.IOS_PREDICATE, 'name == "icn work copy black"', "草稿箱-作品复制按钮")
    _edit_draft_works_name_btn = (By.XPATH,
                                  '//XCUIElementTypeCell[1]/XCUIElementTypeButton[@name="icn work publish black"]/following-sibling::XCUIElementTypeButton[1]',
                                  '编辑作品名称按钮')
    _draft_works_name_input = (By.IOS_PREDICATE, 'type == "XCUIElementTypeTextView"', '作品名称输入框')
    _edit_name_confirm_btn = (By.IOS_PREDICATE, 'name == "确定"', '编辑作品名称确定按钮')
    _edit_name_locator = [_draft_works_name_input, _edit_name_confirm_btn]
    _draft_del_btn = (By.IOS_PREDICATE, 'name == "icn work trash black"', '作品删除按钮')
    _del_works_confirm_btn = (By.IOS_PREDICATE, 'name == "icn work confirm"', '删除确定按钮')
    _cancel_publish_btn = (By.IOS_CLASS_CHAIN,
                           '**/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeButton[`name == "icn work cancel published"`]',
                           '草稿箱-取消发布按钮')
    _popup_cancel_publish_btn = (By.IOS_PREDICATE, 'name == "取消发布"', '确认弹窗-取消发布按钮')
    _published_works_cover = (
    By.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeImage[1]', '已发布-第一个作品封面')
    _edit_more_btn = (By.IOS_PREDICATE, 'name == "icon／24／more"', '作品详情-右上角-更多按钮')
    _edit_works_info_btn = (By.IOS_PREDICATE, 'name == "编辑信息"', '作品详情-右上角-编辑信息')
    _publish_works_name_input = (
    By.XPATH, '//XCUIElementTypeButton[@name="作品封面"]/following-sibling::XCUIElementTypeTextView[1]', '作品发布-作品名称输入框')
    _publish_works_summary_tips = (By.XPATH, '//XCUIElementTypeTextView[@value="喜欢我喵作品吗?点个赞再走吧"]', '作品发布-作品简介默认提示')
    # _publish_works_summary_input = (By.XPATH, '//XCUIElementTypeTextView[@value="喜欢我喵作品吗?点个赞再走吧"]', '作品发布-作品简介输入框')
    # _publish_works_summary_input = (
    # By.XPATH, '//XCUIElementTypeStaticText[@name="请输入作品名称"]/../following-sibling::XCUIElementTypeTextView[1]', '作品发布-作品简介输入框')
    _publish_works_summary_input = (
    By.XPATH, '//XCUIElementTypeButton[@name="作品封面"]/following-sibling::XCUIElementTypeTextView[2]', '作品发布-作品简介输入框')
    _publish_works_cover_btn = (By.IOS_PREDICATE, 'name == "作品封面"', '作品发布-作品简介输入框')
    _upload_photo_btn = (By.IOS_PREDICATE, 'name == "上传图片"', '作品发布-作品简介输入框')
    _allow_access_btn = (By.IOS_PREDICATE, 'name == "允许访问"', '访问照片-允许访问')
    _nemo_sys_photo_btn = (By.IOS_PREDICATE, 'name == "照片"', '系统设置-照片')
    _read_write_btn = (By.IOS_PREDICATE, 'name == "读取和写入"', '照片权限-读取和写入')
    _album_first_photo = (
    By.XPATH, '//XCUIElementTypeImage[@name="icon／32／相机白"]/../../following-sibling::XCUIElementTypeCell[1]',
    '作品发布-作品简介输入框')
    _choose_photo_btn = (By.IOS_PREDICATE, 'name == "选取"', '上传封面-选取按钮')
    # _copy_link_btn = (By.XPATH, '//XCUIElementTypeButton[@name="menu close"]/preceding-sibling::XCUIElementTypeOther[1]/XCUIElementTypeCollectionView[1]/XCUIElementTypeCell[1]/XCUIElementTypeOther[1]/XCUIElementTypeImage[1]', '分享卡片页-复制链接按钮')
    _copy_link_btn = (By.XPATH, '//XCUIElementTypeCollectionView/XCUIElementTypeCell[1]', '分享卡片页-复制链接按钮')
    _save_picture_btn = (By.XPATH, '//XCUIElementTypeCollectionView/XCUIElementTypeCell[2]', '分享卡片页-保存图片按钮')
    _miao_code_btn = (By.XPATH, '//XCUIElementTypeCollectionView/XCUIElementTypeCell[3]', '分享卡片页-生成喵口令按钮')
    _to_paste_btn = (By.IOS_PREDICATE, 'type == "XCUIElementTypeButton" AND name == " 去粘贴"', '喵口令-去粘贴')
    _share_close_btn = (By.IOS_PREDICATE, 'type == "XCUIElementTypeButton" AND name == "menu close"', '分享卡片页-关闭按钮')
    _generate_share_card_close_btn = (By.IOS_PREDICATE, 'type == "XCUIElementTypeButton" AND name="share close"', '生成分享卡片-关闭按钮')
    _miao_code_card_close_btn = (By.IOS_PREDICATE, 'type == "XCUIElementTypeButton" AND name="icon／48／关闭白"', '喵口令卡片-关闭按钮')

    # 上传按钮    /XCUIElementTypeOther[1]/XCUIElementTypeImage[1]
    _upload_btn = (By.XPATH, "//XCUIElementTypeButton[@label='icn work upload black']", "上传按钮")
    # 分享按钮
    _share_btn = (By.XPATH, "//XCUIElementTypeButton[@label='icn work share black']", "分享按钮")
    # 取消分享
    _cancel_share = (By.XPATH, '//*[@name="menu close"]', "取消分享按钮")
    # 分享路径
    _share_type = (By.XPATH, "//XCUIElementTypeCell[1]",)

    # 发布按钮
    _draft_publish_btn = (By.IOS_CLASS_CHAIN,
                          "**/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeButton[`name == 'icn work publish black'`]",
                          "草稿箱-发布按钮")
    _publish_btn = (By.IOS_PREDICATE, 'name == "发布"', '发布页-发布按钮')


    # 确定删除
    _delete_cofirm_btn = (By.XPATH, '//*[@name="icn work confirm"]', "确定删除按钮")

    # 取消删除
    _delete_cancel_btn = (By.XPATH, '//*[@name="icn work cancel"]', "取消删除按钮")

    # 删除中的toast
    _delete_toast = (By.XPATH, "//*[contains(@label,'正在删除')]", "删除中toast提示")

    # 喵口令-去粘贴
    _miao_paste = (By.XPATH, "//XCUIElementTypeButton[contains(@label,'去粘贴')]", "喵口令-去粘贴")

    # 喵口令——稍后打开、立即打开
    _miao_open_immediately = (By.XPATH, "//XCUIElementTypeButton[contains(@label,'立即打开')]", "喵口令-立即打开")
    _miao_open_later = (By.XPATH, "//XCUIElementTypeButton[contains(@label,'稍后查看')]", "喵口令-稍后打开")

    _edit_name_cancel_btn = (By.IOS_PREDICATE, 'name == "icn work close gray"', '编辑草稿箱作品-取消按钮')

    def click_share_close_btn(self):
        """关闭分享卡片页"""
        self.click(self._share_close_btn)

    def click_generate_card_close_btn(self):
        """关闭生成分享卡片页"""
        self.click(self._generate_share_card_close_btn)

    def enter_publish_work_name(self, name):
        """编辑发布的作品名称"""
        self.click(self._publish_works_name_input)
        self.element_slide_to(self._keyboard_space_btn)
        self.send_keys(self._publish_works_name_input, name)
        return self.get_elements_value(self._publish_works_name_input)

    def enter_publish_works_summary(self, text):
        """编辑发布作品的简介"""
        # self.click(self._publish_works_name_input)
        # self.long_press(self._publish_works_name_input)
        # self.select_all_and_delete()
        # self.element_slide_to(self._keyboard_space_btn, distance=210)
        self.send_keys(self._publish_works_summary_input, text)
        self.driver.set_value()

    def get_publish_works_summary(self, summary):
        """获取发布作品的简介"""
        summary_locator = (By.IOS_PREDICATE, f'type == "XCUIElementTypeStaticText" AND name == "{summary}"', '作品简介')
        # return self.is_element_exist(self._publish_works_summary_input)
        return self.is_element_exist(summary_locator)

    def get_publish_works_summary_tips(self):
        """获取作品简介默认提示"""
        return self.is_element_exist(self._publish_works_summary_tips)

    def upload_works_cover(self):
        """上传作品封面"""
        self.tap_element(self._publish_works_cover_btn)
        self.click(self._upload_photo_btn)
        # 没有照片访问权限，则设置访问权限
        if self.is_element_exist(self._allow_access_btn, sleep_time=5):
            self.click(self._allow_access_btn, sleep_time=5)
            self.click(self._nemo_sys_photo_btn, sleep_time=5)
            self.click(self._read_write_btn, sleep_time=5)
            self.reset()
            self.click_my_btn()
            self.click_published_works()
            self.click_published_works_cover()
            self.click_edit_works_info_btn()
            self.tap_element(self._publish_works_cover_btn)
            self.click(self._upload_photo_btn)
        self.click(self._album_first_photo)
        self.click(self._choose_photo_btn)

    def is_works_name_exist(self, name):
        """检查页面上给定的作品名称存在"""
        works_name_locator = (By.IOS_PREDICATE, f'type == "XCUIElementTypeStaticText" AND name == "{name}"', '作品名称')
        return self.is_element_exist(works_name_locator)

    def click_edit_works_info_btn(self):
        """编辑已发布的作品名称"""
        self.click(self._edit_more_btn)
        self.click(self._edit_works_info_btn)

    def click_published_works_cover(self):
        """点击已发布作品的封面"""
        self.click(self._published_works_cover)

    def click_edit_name_cancel_btn(self):
        """点击编辑草稿箱作品-取消按钮"""
        self.click(self._edit_name_cancel_btn)

    def click_upload_button(self):
        """点击上传按钮"""
        # 上传前上传按钮数量
        a1 = self.get_group_elements_count(self._upload_btn)
        self.click(self._upload_btn)
        # 上传前】后上传按钮数量
        # sleep(3)
        a2 = self.get_group_elements_count(self._upload_btn)
        return a1, a2

    def click_trash_button(self, level):
        """点击删除按钮"""
        # 删除按钮
        _trash_btn = (
        By.IOS_CLASS_CHAIN, f"**/XCUIElementTypeCell[{level}]/XCUIElementTypeButton[`name == 'icn work trash black'`]",
        "删除按钮")
        self.click(_trash_btn)

    def delete_draft_works(self, level=1):
        """确认删除草稿作品"""
        self.click_trash_button(level=level)
        self.click(self._delete_cofirm_btn)

    def delete_cancel(self, level=1):
        """取消删除草稿"""
        self.click_trash_button(level=level)
        self.click(self._delete_cancel_btn)

    def click_share_button(self):
        """点击分享按钮"""
        self.click(self._share_btn)

    def click_copy_link(self):
        """点击复制链接"""
        self.click(self._copy_link_btn)

    def click_save_picture(self):
        """点击保存图片的按钮"""
        self.click(self._save_picture_btn)

    def click_gen_miao_code(self):
        """点击生成喵口令"""
        self.click(self._miao_code_btn)

    def click_miao_code_close_btn(self):
        """点击生成喵口令"""
        self.click(self._miao_code_card_close_btn)

    def click_to_paste(self):
        """点击去粘贴"""
        self.click(self._to_paste_btn)

    def get_cancel_publish_button(self):
        """验证草稿箱第一个取消发布按钮是否存在"""
        return self.is_element_exist(self._cancel_publish_btn)

    def get_publish_button(self):
        """验证草稿箱第一个取消发布按钮是否存在"""
        return self.is_element_exist(self._draft_publish_btn)

    def cancel_publish_works(self):
        """取消发布作品"""
        self.click(self._cancel_publish_btn)
        self.click(self._popup_cancel_publish_btn)

    def click_publish_btn(self):
        """点击发布按钮"""
        self.click(self._publish_btn)

    def publish_works(self):
        """发布作品"""
        self.click(self._draft_publish_btn)
        self.click_publish_btn()

    def click_draft_tab(self):
        """点击草稿箱"""
        self.click(self._draft_tab)

    def get_draft_tab(self):
        """获取草稿箱tab是否存在"""
        return self.is_element_exist(self._draft_tab)

    def get_draft_works_count(self):
        """获取草稿作品数量"""
        draft_box_text = self.get_elements_value(self._draft_tab)
        draft_works_count = self.get_number_from_str(draft_box_text)
        self.logger.info(f'获取到草稿作品数量：{draft_works_count}')
        return draft_works_count

    def get_published_works_count(self):
        """获取草稿作品数量"""
        publish_box_text = self.get_elements_value(self._published_tab)
        published_works_count = self.get_number_from_str(publish_box_text)
        self.logger.info(f'获取到草稿作品数量：{published_works_count}')
        return published_works_count

    def click_right_arrow(self):
        """点击右箭头，进入个人中心"""
        self.tap_element(self._right_arrow_icon)

    def get_my_nickname(self):
        """获取我的昵称"""
        return self.get_elements_value(self._my_nickname)

    def click_copy_btn(self):
        """点击草稿箱-作品复制按钮"""
        self.click(self._copy_btn)

    def click_edit_btn(self):
        """点击编辑按钮"""
        self.click(self._edit_draft_works_name_btn)

    def edit_draft_works_name(self, name):
        """编辑作品名称"""
        # 长按
        self.long_press(self._draft_works_name_input)
        # 删除之前的内容
        self.select_all_and_delete()
        self.submit(self._edit_name_locator, name)

    def delete_draft_works(self):
        """删除草稿箱作品"""
        self.click(self._draft_del_btn)
        self.click(self._del_works_confirm_btn)

    def get_contains_works_name_count(self, keyword):
        """获取包含关键字的作品数量"""
        _works_name = (
            By.IOS_CLASS_CHAIN, f'**/XCUIElementTypeButton/XCUIElementTypeStaticText[`name CONTAINS "{keyword}"`]',
            '搜索结果页-作品名称')
        count = self.get_group_elements_count(_works_name)
        self.logger.info(f'获取到包含关键字{keyword}的作品数量：{count}')
        return count

    def get_draft_works_name(self, level=1):
        """获取草稿箱-作品名称, 默认获取第一个"""
        _works_name = (By.XPATH,
                       f'//XCUIElementTypeCell[{level}]/*[@name="icn work trash black"]/following-sibling::XCUIElementTypeButton[3]/XCUIElementTypeStaticText[1]',
                       '草稿箱-作品名称')
        return self.get_elements_value(_works_name)

    def click_published_works(self):
        """点击已发布按钮"""
        self.click(self._published_tab)



    def share_button(self):
        """确认微信、QQ是否安装"""
        a_w = self.driver.is_app_installed("com.tencent.xin")
        a_q = self.driver.is_app_installed("com.tencent.mqq")
        print("hzjhzj", a_q, a_w)
        if a_w == 1 and a_q == 1:
            print('hhhh')
        # 微信、QQ都没有安装
        if a_w == 0 and a_q == 0:
            _winxin_share = 0
            _peng_share = None
            _qq_share = None
            _qone_share = None
            _link_share = (By.XPATH, "//XCUIElementTypeCell[1]", "草稿箱链接分享--链接")
            _pic_share = (By.XPATH, "//XCUIElementTypeCell[2]", "草稿箱图片分享--图片")
            _mao_share = (By.XPATH, "//XCUIElementTypeCell[3]", "草稿箱喵口令分享--喵口令")
        # 微信、QQ都已安装
        elif a_w == 1 and a_q == 1:
            _winxin_share = (By.XPATH, "//XCUIElementTypeCell[1]", "草稿箱微信分享--微信")
            _peng_share = (By.XPATH, "//XCUIElementTypeCell[2]", "草稿箱朋友圈分享--朋友圈")
            _qq_share = (By.XPATH, "//XCUIElementTypeCell[3]", "草稿箱qq分享--qq好友")
            _qone_share = (By.XPATH, "//XCUIElementTypeCell[4]", "草稿箱qq空间分享--qq空间")
            _link_share = (By.XPATH, "//XCUIElementTypeCell[5]", "草稿箱链接分享--链接")
            _pic_share = (By.XPATH, "//XCUIElementTypeCell[6]", "草稿箱图片分享--图片")
            _mao_share = (By.XPATH, "//XCUIElementTypeCell[7]", "草稿箱喵口令分享--喵口令")

        return _winxin_share, _peng_share, _qq_share, _qone_share, _link_share, _pic_share, _mao_share

    # aa_list=share_button()

    def click_mao_share(self):
        """点击分享喵口令
        备注：微信、qq已安装下，喵口令的定位，需要继续调试
        """
        a_w = self.driver.is_app_installed("com.tencent.xin")
        a_q = self.driver.is_app_installed("com.tencent.mqq")
        # 微信、QQ都没有安装
        self.logger.info("微信:{},QQ:{}".format(a_w, a_q))
        if a_w == 0 and a_q == 0:
            _mao_share = (By.XPATH, "//XCUIElementTypeCell[3]", "草稿箱喵口令分享--链接")
        # 微信、QQ都已安装
        elif a_w == 1 and a_q == 1:
            self.swipe_to_left()
            _mao_share = (By.XPATH, "//XCUIElementTypeCell[7]", "草稿箱喵口令分享--链接")
            # _mao_share = (By.XPATH,'//XCUIElementTypeImage[@name="icon／32／喵口令(5)"]',"草稿箱喵口令分享--链接")
        self.click(_mao_share)
        # 微信、QQ都已安装

    def miao_paste(self):
        """
        喵口令-去粘贴
        """
        self.click(self._miao_paste)

    def miao_open_immediately(self):
        """
        喵口令-立即打开
        """
        self.click(self._miao_open_immediately)

    def miao_open_later(self):
        """
        喵口令-稍后打开
        """
        self.click(self._miao_open_later)

    def click_cloud_icon(self):
        """点击云端作品icon"""
        self.click(self._cloud_icon)
