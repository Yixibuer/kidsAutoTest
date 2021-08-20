#!/usr/bin/env python
# coding = utf-8

from appium.webdriver.connectiontype import ConnectionType
from appium.webdriver.webdriver import WebDriver
from base import MobilePage


class AndroidPage(MobilePage):
    """移动端操作方法

    Android端的api
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver
        super().__init__(self.driver)

    def install_app(self, path):
        """安装应用"""
        self.driver.install_app(path)

    def is_install_app(self, package_name):
        """检查应用是否安装"""
        return self.driver.is_app_installed(package_name)

    def uninstall(self, package_name):
        """卸载应用"""
        self.driver.remove_app(package_name)

    def launch(self):
        """启动应用"""
        self.driver.launch_app()
        self.logger.info("launch app")

    def close_app(self):
        """关闭应用"""
        self.driver.close_app()
        self.logger.info("close app")

    def background(self, sleep_time):
        """把当前应用放到app后台"""
        self.driver.background_app(sleep_time)
        self.logger.info(u"make app background {0} seconds".format(sleep_time))

    def get_activity(self):
        """获取activity"""
        if self.platform == 'android':
            return self.driver.current_activity
        else:
            self.logger.warning('获取activity只支持Android平台')

    def open_notifications(self):
        """打开通知栏

        打开通知栏功能只有Android可用

        """
        self.driver.open_notifications()
        self.logger.info("打开通知栏")

    def wait_activity(self, activity, timeout, interval=1):
        """等待指定的activity出现直到超时，interval为扫描间隔1秒"""
        self.driver.wait_activity(activity, timeout)

    def set_network(self, net_type='wifi_only'):
        """
         设置网络类型
         Sets the network connection type. Android only.
             Possible values:
                 Value (Alias)      | Data | Wifi | Airplane Mode
                 -------------------------------------------------
                 0 (None)           | 0    | 0    | 0
                 1 (Airplane Mode)  | 0    | 0    | 1
                 2 (Wifi only)      | 0    | 1    | 0
                 4 (Data only)      | 1    | 0    | 0
                 6 (All network on) | 1    | 1    | 0
         These are available through the enumeration `appium.webdriver.ConnectionType`
         设置网络类型
         :Args:
          - net_type - a member of the enum appium.webdriver.ConnectionType
        """
        if net_type == "airplane_mode":
            self.driver.set_network_connection(ConnectionType.AIRPLANE_MODE)
        elif net_type == "wifi_only":
            self.driver.set_network_connection(ConnectionType.WIFI_ONLY)
        elif net_type == "data_only":
            self.driver.set_network_connection(ConnectionType.DATA_ONLY)
        else:
            self.driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)

    def key_event(self, key_code):
        """键盘事件"""
        self.driver.keyevent(key_code)
