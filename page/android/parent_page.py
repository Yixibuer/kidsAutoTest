#!/usr/bin/env python
# coding=utf-8
from base import By
from page.android_common_page import AndroidCommonPage


class ParentPage(AndroidCommonPage):
    """
    家长中心页面
    """
    login_button=(By.ID,"cn.codemao.android.kids.lite:id/tv_login") #未登录态时立即登录按钮
    achievement_button=(By.ID,"cn.codemao.android.kids.lite:id/view_achievement") #邀请有礼入口
    account_button=(By.ID,"cn.codemao.android.kids.lite:id/layout_account") #账号管理入口
    order_button=(By.ID,"cn.codemao.android.kids.lite:id/layout_order") #我的订单入口
    qa_button=(By.ID,"cn.codemao.android.kids.lite:id/layout_qa")  #常见问题入口
    setting_button=(By.ID,"cn.codemao.android.kids.lite:id/layout_setting") #设置入口


    def click_login(self):
        '''未登录状态时点击立即登录'''
        self.click(self.login_button)
