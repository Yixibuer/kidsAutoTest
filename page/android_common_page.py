#!/usr/bin/env python
# coding=utf-8

from base import AndroidPage
from base import By
import uiautomator2 as u2


class AndroidCommonPage(AndroidPage):
    """
    android公共页面常用的元素和公共方法
    """

    _fast_enter_login = (By.ID, "cn.codemao.android.kids.lite:id/layout_fast_enter")  # 首页快速登录入口
    _course_button=(By.ID,"cn.codemao.android.kids.lite:id/tab_course") #我的课程页面按钮
    _creat_button=(By.ID,"cn.codemao.android.kids.lite:id/tab_create")  #创作中心按钮
    _parent_button=(By.ID,"cn.codemao.android.kids.lite:id/tv_parent") #家长中心按钮
    _sprite_button=(By.ID,"cn.codemao.android.kids.lite:id/iv_sprite")  #源码精灵按钮

    _login_button=(By.ID,"cn.codemao.android.kids.lite:id/tv_login") #立即登录


    def click_fast_enter_login(self):
        '''未登录时点击快速登录入口'''
        self.click(self._fast_enter_login)



    def click_creat(self):
        '''点击创作中心入口'''
        self.click(self._creat_button)


    def click_parent(self):
        '''点击家长中心入口'''
        self.click(self._parent_button)

    def click_sprite(self):
        '''点击源码精灵入口'''
        self.click(self._sprite_button)




