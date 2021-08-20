#!/usr/bin/env python
# coding = utf-8
import base64
import os
import time
import traceback
from airtest import aircv
from appium.webdriver.common.touch_action import TouchAction
from ocv.utils import string_2_img
from airtest.core.error import TargetNotFoundError
from appium.webdriver.webdriver import WebDriver
from utils import config
from base import BasePage, By
from ocv.cv import Template, XYTransformer
from ocv.settings import Settings as ST
from utils import common


class MobilePage(BasePage):
    """移动端操作方法

    包含iOS和Android端的通用api
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self._size = {'width': None, 'height': None}
        self._touch_factor = 0.5
        super().__init__(self.driver)

    def swipe_to_left(self, width=None, height=None, duration=500, position='mid'):
        """屏幕左滑
        :Args:
            position: 滑动位置，upside（上）mid（中间）below（下）
        """
        if width is None or height is None:
            width, height = self.get_window_size()
            start_x, end_x = width / 4 * 3, width / 4
            if position == 'upside':
                start_y, end_y = height / 4, height / 4
            if position == 'mid':
                start_y, end_y = height / 2, height / 2
            if position == 'below':
                start_y, end_y = height * 3 / 4, height * 3 / 4
        if self.platform == 'ios':
            self.execute_js("mobile: swipe", {"direction": "left"})
            self.logger.info(f'屏幕左滑')
        else:
            self.driver.swipe(start_x, start_y, end_x, end_y, duration)
            self.logger.info(f'屏幕左滑{start_x, start_y, end_x, end_y}')

    def swipe_to_right(self, width=None, height=None, duration=800):
        """屏幕右滑"""
        if self.platform == 'ios':
            self.execute_js("mobile: swipe", {"direction": "right"})
        else:
            if width is None or height is None:
                width, height = self.get_window_size()
            self.driver.swipe(width / 4, height / 2, width / 4 * 3, height / 2, duration)
        self.logger.info('屏幕右滑')

    def swipe_to_down(self, width=None, height=None, duration=800):
        """屏幕下滑"""
        if self.platform == 'ios':
            self.execute_js("mobile: swipe", {"direction": "down"})
        else:
            if width is None or height is None:
                width, height = self.get_window_size()
            self.driver.swipe(width / 2, height / 4, width / 2, height / 4 * 3, duration)
        self.logger.info('屏幕下滑')

    def swipe_to_up(self, width=None, height=None, duration=800):
        """屏幕上滑"""
        if self.platform == 'ios':
            self.execute_js("mobile: swipe", {"direction": "up"})
        else:
            if width is None or height is None:
                width, height = self.get_window_size()
            self.driver.swipe(width / 2, height / 4 * 3, width / 2, height / 4, duration)
        self.logger.info('屏幕上滑')

    def tap(self, positions, duration=None, times=1):
        """模拟手指点击（最多五个手指），可设置按住时间长度（毫秒）

        Args:
            positions: an array of tuples representing the x/y coordinates of
                the fingers to tap. Length can be up to five.
            duration: length of time to tap, in ms
            times: 点击次数

        Usage:
            driver.tap([(100, 20), (100, 60), (100, 100)], 500)

        Returns:
            Union['WebDriver', 'ActionHelpers']: Self instance
        """
        if isinstance(positions, tuple):
            positions = [positions]
        if isinstance(times, int) and times > 1:
            for i in range(times):
                self.driver.tap(positions, duration=duration)
        else:
            self.driver.tap(positions, duration=duration)
        self.logger.info(f'点击坐标{positions}完成')

    def get_element_pos(self, locator):
        """获取元素坐标"""
        ele = self.find_element(locator)
        # 获取元素中心坐标
        x_pos = ele.location['x'] + ele.size['width'] / 2
        y_pos = ele.location['y'] + ele.size['height'] / 2
        return x_pos, y_pos

    def tap_element(self, locator):
        """通过获取元素坐标，点击元素"""
        x_pos, y_pos = self.get_element_pos(locator)
        pos = [(x_pos, y_pos)]
        self.logger.info(f'点击的坐标：{pos}')
        self.tap(pos)
        self.logger.info(f'通过坐标点击元素：{locator[-1]} 成功')

    def flick(self, start_x, start_y, end_x, end_y):
        """按住A点后快速滑动至B点"""
        self.driver.flick(start_x, start_y, end_x, end_y)

    def lock(self, lock_time):
        """锁定屏幕"""
        self.driver.lock(lock_time)
        self.logger.info(u"lock the device {0} seconds".format(lock_time))

    def scroll(self, origin_el, destination_el, duration=None):
        """元素滚动
        Args:
            origin_el: the element from which to being scrolling
            destination_el: the element to scroll to
            duration: a duration after pressing originalEl and move the element to destinationEl.
                Default is 600 ms for W3C spec. Zero for MJSONWP.
        Usage:
            driver.scroll(el1, el2)

        Returns:
            Union['WebDriver', 'ActionHelpers']: Self instance
        """
        self.driver.scroll(origin_el, destination_el, duration=duration)

    def hide_keyboard(self, key_name=None, key=None, strategy=None):
        """隐藏键盘,iOS使用key_name隐藏，安卓不使用参数"""
        if self.platform == 'android':
            self.driver.hide_keyboard()
        if self.platform == 'ios':
            self.driver.hide_keyboard(key_name, key, strategy=strategy)

    def contexts(self):
        """列出所有的可用上下文"""
        return self.driver.contexts

    def current_context(self):
        """列出当前上下文"""
        return self.driver.current_context

    def switch_to_context(self, new_context):
        """切换上下文

        """
        self.driver.switch_to.context(new_context)

    def get_window_size(self):
        """获取窗口尺寸"""
        size = self.driver.get_window_size()
        if self.platform == 'ios':
            # ios 获取的尺寸只是屏幕的1/2, 因此需要 size * 2
            width = size['width'] * 2
            height = size['height'] * 2
            self.logger.info(f"current window size: {(width, height)}")
            return width, height
        self.logger.info(f"current window size: {size}")
        return size['width'], size['height']

    def _snapshot(self, filename=None, str_type=False, quality=10):
        """
        take snapshot
        filename: save screenshot to filename
        quality: The image quality, integer in range [1, 99]
        """
        # 获取截图base64编码
        value = self.driver.get_screenshot_as_base64()
        data = base64.b64decode(value)
        if self.platform == 'ios':
            # 实时刷新手机画面，直接返回base64格式，旋转问题交给IDE处理
            if str_type:
                if filename:
                    with open(filename, 'wb') as f:
                        f.write(data)
                return data
            # output cv2 object
            try:
                screen = string_2_img(data)
            except:
                # may be black/locked screen or other reason, print exc for debugging
                traceback.print_exc()
                return None
            h, w = screen.shape[:2]
            # save last res for portrait
            if self.driver.orientation in ['LANDSCAPE', 'UIA_DEVICE_ORIENTATION_LANDSCAPERIGHT']:
                self._size['height'] = w
                self._size['width'] = h
            else:
                self._size['height'] = h
                self._size['width'] = w
            winw, winh = self.get_window_size()
            # ios高度此处要除以2
            self._touch_factor = float(winh / 2) / float(h)
        else:
            try:
                screen = string_2_img(data)
            except Exception:
                # may be black/locked screen or other reason, print exc for debugging
                traceback.print_exc()
                return None
        # save as file if needed
        if filename:
            aircv.imwrite(filename, screen, quality)
        return screen

    def _try_log_screen(self, screen=None):
        """
        Save screenshot to file

        Args:
            screen: screenshot to be saved

        Returns:
            None

        """
        if not ST.SS_DIR:
            ST.SS_DIR = config.tmp_img_path
        if screen is None:
            screen = self._snapshot(quality=ST.SNAPSHOT_QUALITY)
        datetime_str = self.get_datetime_str()
        filename = f"{datetime_str}.jpg"
        filepath = os.path.join(ST.SS_DIR, filename)
        aircv.imwrite(filepath, screen, ST.SNAPSHOT_QUALITY)
        return {"screen": filename, "resolution": aircv.get_resolution(screen)}

    def _touch_point_by_orientation(self, tuple_xy):
        """
        Convert image coordinates to physical display coordinates, the arbitrary point (origin) is upper left corner
        of the device physical display

        Args:
            tuple_xy: image coordinates (x, y)

        Returns:

        """
        x, y = tuple_xy

        # use correct w and h due to now orientation
        # _size 只对应竖直时候长宽
        now_orientation = self.driver.orientation

        if now_orientation in ['PORTRAIT', 'UIA_DEVICE_ORIENTATION_PORTRAIT_UPSIDEDOWN']:
            width, height = self._size['width'], self._size["height"]
        else:
            height, width = self._size['width'], self._size["height"]

        # check if not get screensize when touching
        if not width or not height:
            # use _snapshot to get current resuluton
            self._snapshot()

        x, y = XYTransformer.up_2_ori(
            (x, y),
            (width, height),
            now_orientation
        )
        return x, y

    def get_template(self, filename, threshold=None, record_pos=None, resolution=(), rgb=False):
        """picture as touch/swipe/wait/exists target and extra info for cv match"""
        if not resolution:
            resolution = self.get_window_size()
        if not os.path.exists(filename):
            filename = os.path.join(ST.IMG_DIR_PATH, filename)
        self.logger.info(f"查找图片: {filename}")
        template = Template(filename, threshold=threshold, record_pos=record_pos, resolution=resolution, rgb=rgb)
        return template

    def loop_find(self, filename, timeout=ST.FIND_TIMEOUT, threshold=None, interval=0.5, intervalfunc=None):
        """
        在当前屏幕查找预期图片，直到超时

        Args:
            filename:  mage name or image file path
            timeout: time interval how long to look for the image template
            threshold: default is None
            interval: sleep interval before next attempt to find the image template
            intervalfunc: function that is executed after unsuccessful attempt to find the image template

        Raises:
            TargetNotFoundError: when image template is not found in screenshot

        Returns:
            TargetNotFoundError if image template not found, otherwise returns the position where the image template has
            been found in screenshot

        """

        query = self.get_template(filename, threshold=threshold)
        start_time = time.time()
        while True:
            screen = self._snapshot(filename=None, quality=ST.SNAPSHOT_QUALITY)

            if screen is None:
                self.logger.warning("Screen is None, may be locked")
            else:
                if threshold:
                    query.threshold = threshold
                match_pos = query.match_in(screen)
                if match_pos:
                    self._try_log_screen(screen)
                    return tuple(match_pos)
            if intervalfunc is not None:
                intervalfunc()
            # 超时则raise，未超时则进行下次循环:
            if (time.time() - start_time) > timeout:
                self._try_log_screen(screen)
                raise TargetNotFoundError('Picture %s not found in screen' % query)
            else:
                time.sleep(interval)

    def touch(self, filename, threshold=ST.THRESHOLD, times=1, **kwargs):
        """
        点击识别到的图片位置

        :param threshold: 识别图片的匹配度，默认0.8
        :param filename:  识别图片的文件名或文件路径，直接传文件名，会拼接上ocv/settings文件配置的IMG_DIR_PATH路径
        :param times: how many touches to be performed
        :param kwargs: platform specific `kwargs`, please refer to corresponding docs
        :return: finial position to be clicked
        :platforms: Android, iOS

        用法：
            页面类继承MobilePage
            self.touch('img_name.png', threshold=0.8)
        """
        pos = self.loop_find(filename, timeout=ST.FIND_TIMEOUT, threshold=threshold)
        for _ in range(times):
            if self.platform == 'ios':
                pos = self._touch_point_by_orientation(pos)
                # scale touch postion
                x, y = pos[0] * self._touch_factor, pos[1] * self._touch_factor
                click_pos = [(x, y)]
            else:
                click_pos = [pos]
            self.logger.info(f'{filename},获取到的图像坐标位置：{pos}')
            # 点击坐标
            self.tap(click_pos, **kwargs)
            time.sleep(0.05)
        time.sleep(ST.OPDELAY)

    def is_img_exists(self, filename, threshold=ST.THRESHOLD_STRICT, msg=""):
        """
        验证预期图片是否存在当前屏幕

        :param threshold: 识别图片的匹配度，默认0.8
        :param filename:  识别图片的文件名或文件路径，直接传文件名，会拼接上ocv/settings文件配置的IMG_DIR_PATH路径
        :param msg: short description of assertion, it will be recorded in the report
        :raise AssertionError: if assertion fails
        :return: coordinates of the target
        :platforms: Android, Windows, iOS
        """

        try:
            pos = self.loop_find(filename, timeout=ST.FIND_TIMEOUT, threshold=threshold)
            self.logger.info(f'{filename}获取到的图像坐标位置：{pos}')
            return True
        except TargetNotFoundError:
            self.logger.error(f"没有匹配到图像：{filename}, 匹配度设置：{threshold} message: {msg}")
            return False

    @staticmethod
    def generate_mobile_locator(text, attrs='name', tag_name=None):
        """组装包含text文本的定位元素"""
        if tag_name is None:
            _locator = (By.XPATH, f'//*[contains(@{attrs}, "{text}")]')
        else:
            _locator = (By.XPATH, f'//{tag_name}[contains(@{attrs}, "{text}")]')
        return _locator

    def long_press(self, locator=None, x=None, y=None, duration=2000):
        """长按操作

        通过元素或者坐标，实现长按操作
        """
        action = TouchAction(self.driver)
        if locator is not None:
            element = self.find_element(locator)
            action.long_press(element, duration=duration).perform()
        if x and y:
            action.long_press(x=x, y=y, duration=duration).perform()

    def move_to_coordinate(self, locator_or_element, x, y, duration=None):
        """滑动元素到指定坐标
        :Args:
            locator_or_element: 定位元素或WebElement
            x: 滑动的x坐标
            y: 滑动的y坐标
            duration: Duration to press
        """
        action = TouchAction(self.driver)
        element = self.is_element(locator_or_element)
        if duration is not None:
            action.long_press(element, duration=duration).move_to(element, x, y).perform()
        else:
            action.long_press(element).move_to(element, x, y).perform()

    def element_slide_to(self, locator, direction='right', distance=20, duration=None):
        """按住元素左右滑动
        :Args:
            locator: 定位元素
            direction：滑动方向，默认向右滑动
            distance: 滑动距离，默认元素中心X坐标加20
            duration: Duration to press

        """
        x_pos, y_pos = self.get_element_pos(locator)
        element = self.find_element(locator)
        if direction == 'left':
            self.move_to_coordinate(element, x_pos - distance, y_pos, duration=duration)
        if direction == 'right':
            self.move_to_coordinate(element, x_pos + distance, y_pos, duration=duration)


