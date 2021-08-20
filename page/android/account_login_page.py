#!/usr/bin/env python
# coding=utf-8
from base import By
from page.android_common_page import AndroidCommonPage


class AccountloginPage(AndroidCommonPage):
    """
    账号登录页面
    """
    back_button=(By.ID,"cn.codemao.android.kids.lite:id/tv_back")  #返回按钮
    account_edit=(By.ID,"cn.codemao.android.kids.lite:id/et_account") #账号编辑框
    pwd_edit=(By.ID,"cn.codemao.android.kids.lite:id/et_pwd")
    forget_password=(By.ID,"cn.codemao.android.kids.lite:id/ftv_forget_password")
    login_button=(By.ID,"cn.codemao.android.kids.lite:id/tv_login")


    def account_login(self,acccount,password):
        self.send_keys(self.account_edit,acccount)
        self.send_keys(self.pwd_edit,password)
        self.click(self.login_button)



