#!/usr/bin/env python
# coding = utf-8
import os
import codecs
import yaml


class Config:
    """读取配置数据

    """

    def __init__(self, path=None):
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if path is None:
            self.yml_path = os.path.join(self.base_path, 'config', 'config.yml')
        else:
            self.yml_path = path

        self._yml_obj = codecs.open(self.yml_path, 'r', 'utf-8')
        self.yml_data = yaml.safe_load(self._yml_obj)

        # driver 路径
        self.chrome_driver_path = os.path.join(self.base_path, 'driver', 'chromedriver')
        self.firefox_driver_path = os.path.join(self.base_path, 'driver', 'geckodriver')

        # 报告路径
        self.report_path = os.path.join(self.base_path, 'report')
        if not os.path.exists(self.report_path):
            os.mkdir(self.report_path)
        # 测试数据路径
        self.data_path = os.path.join(self.base_path, 'data')
        # 临时文件路径
        self.tmp_path = os.path.join(self.base_path, 'tmp')
        if not os.path.exists(self.tmp_path):
            os.mkdir(self.tmp_path)
        self.tmp_img_path = os.path.join(self.tmp_path, 'cv_ss_img')
        if not os.path.exists(self.tmp_img_path):
            os.mkdir(self.tmp_img_path)
        # 日志文件路径
        self.log_file_path = os.path.join(self.report_path, 'log')
        # 上传文件路径
        self.upload_files_path = os.path.join(self.data_path, 'upload_files')
        # 定位图片文件路径
        self.locate_img_path = os.path.join(self.data_path, 'locate_img')
        # player图像文件路径
        self.player_path = os.path.join(self.data_path, 'player')
        # 截图保存路径
        self.screenshot_path = os.path.join(self.report_path, 'screenshot')
        # template路径
        self.template_path = os.path.join(self.report_path, 'template')
        # 配置数据
        self.conf = self.yml_data["conf"]
        # url
        self.url = self.conf["url"]
        # 环境配置
        self.env = self.conf["env"]
        # 浏览器
        self.browser = self.conf["browser"]
        # 运行平台
        self.platform = self.conf["platform"]
        # 无头模式默认关闭
        self.headless = False

        # 显式等待时间
        self.wait_time = self.conf["wait_time"]
        # appium 连接地址
        self.command_executor = self.conf["command_executor"]
        try:
            # android desired_caps数据
            self.android_caps = self.yml_data["android_caps"]
            self.platformName = self.android_caps["platformName"]
            self.platformVersion = self.android_caps["platformVersion"]
            self.deviceName = self.android_caps["deviceName"]
            self.appPackage = self.android_caps["appPackage"]
            self.appActivity = self.android_caps["appActivity"]

            # grid caps
            self.grid_caps = self.yml_data["grid_caps"]
            # selenium grid url
            self.hub_url = self.grid_caps["hub_url"]

            # ios caps 路径
            self.ios_caps = self.yml_data["ios_caps"]

        except KeyError as e:
            print(f'配置项不存在: {e}')

        # 图片文件路径
        self.open_later_tips = os.path.join(self.locate_img_path, 'open_later_tips.png')


if __name__ != "__main__":
    config = Config()
