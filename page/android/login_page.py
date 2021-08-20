#!/usr/bin/env python
# coding=utf-8
from base import By
from page.android_common_page import AndroidCommonPage


class LoginPage(AndroidCommonPage):
    """
    登录页面
    """

    phone_edit = (By.ID, "cn.codemao.android.kids.lite:id/et_account") #手机号码输入框
    pwd_edit=(By.ID,"cn.codemao.android.kids.lite:id/et_pwd") # 验证码输入框
    captcha_button=(By.ID,"cn.codemao.android.kids.lite:id/tv_captcha") #获取验证码
    login_button= (By.ID,"cn.codemao.android.kids.lite:id/tv_login") #登录按钮
    agreement_box=(By.ID,"cn.codemao.android.kids.lite:id/cb_agreement") #协议勾选框
    wx_login_btn = (By.ID, "cn.codemao.android.kids.lite:id/iv_we_chat") #微信登录
    scan_login_btn = (By.ID, "cn.codemao.android.kids.lite:id/iv_scan") #扫码登录
    account_login_btn = (By.ID, "cn.codemao.android.kids.lite:id/iv_account") #账号登录

    def click_agreement_box(self):
        '''点击勾选同意用户协议'''
        self.click(self.agreement_box())

    def click_account_login(self):
        '''选择账号登录'''
        self.click(self.account_login())

