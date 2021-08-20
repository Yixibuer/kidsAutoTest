#!/usr/bin/env python
# coding=utf-8
"""
公共参数配置和公共函数模块
"""
import os
from functools import wraps
from inspect import signature
import threading
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from appium import webdriver as mobile_driver
from utils import config
import platform


def get_env_var(variable: str):
    """获取环境变量或配置变量"""
    var = os.environ.get(variable)
    if not var:
        var = getattr(config, variable)
    return var


def get_grid_driver(caps=None):
    """获取 grid driver"""
    hub_url = config.hub_url
    if caps is None:
        browser = get_env_var('browser')
        caps = {'browserName': browser}
    driver = webdriver.Remote(
        command_executor=hub_url,
        desired_capabilities=caps
    )
    return driver


def get_web_driver():
    """获取 web driver"""
    browser = get_env_var('browser')
    if browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        if platform.system() == "Linux":
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--hide-scrollbars")
        elif platform.system() in ("Windows", 'Darwin'):
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--hide-scrollbars")
            # 无头模式配置
            headless = get_env_var('headless')
            if headless:
                chrome_options.add_argument("--headless")
        try:
            driver = webdriver.Chrome(options=chrome_options)
        except WebDriverException:
            driver = webdriver.Chrome(executable_path=config.chrome_driver_path, options=chrome_options)
        return driver
    elif browser == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        # 无头模式配置
        headless = get_env_var('headless')
        if headless:
            firefox_options.add_argument('-headless')
        try:
            driver = webdriver.Firefox(options=firefox_options)
        except WebDriverException:
            driver = webdriver.Firefox(executable_path=config.firefox_driver_path, options=firefox_options)
        return driver
    else:
        raise ValueError('可选值：chrome、firefox')


def get_android_driver(platform_version=None, device_name=None):
    """获取 Android driver"""
    desired_caps = config.android_caps
    if platform_version is not None:
        desired_caps['platformVersion'] = platform_version
    if device_name is not None:
        desired_caps['deviceName'] = device_name
    driver = mobile_driver.Remote(config.command_executor, desired_caps)
    return driver


def get_ios_driver(platform_version=None, device_name=None, app_path=None):
    """获取ios driver"""
    desired_caps = config.ios_caps
    if platform_version is not None:
        desired_caps['platformVersion'] = platform_version
    if device_name is not None:
        desired_caps['deviceName'] = device_name
    if app_path is not None:
        desired_caps['app'] = app_path
    driver = mobile_driver.Remote(config.command_executor, desired_caps)
    return driver


def get_driver():
    """根据配置返回不同的driver"""
    test_platform = get_env_var('platform')
    if test_platform == 'web':
        return get_web_driver()
    if test_platform == 'android':
        return get_android_driver()
    if test_platform == 'ios':
        return get_ios_driver()
    if test_platform == 'grid':
        return get_grid_driver()


def get_env_url(url=None):
    """根据环境，拼接web端url地址

    """
    if url is None:
        url = config.url
    env_tag = get_env_var('env').lower()
    if env_tag in ('test', 'staging'):
        env_url = "https://{}-{}".format(env_tag, url)
    elif env_tag == "prod":
        env_url = "https://{}".format(url)
    else:
        raise ValueError('环境只能为test、staging、pro')
    return env_url


def synchronized(func):
    func.__lock__ = threading.Lock()

    def lock_func(*args, **kwargs):
        with func.__lock__:
            return func(*args, **kwargs)

    return lock_func


class Singleton(object):
    """单例类"""

    @synchronized
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


def type_assert(*ty_args, **ty_kwargs):
    """验证方法的入参类型"""

    def decorate(func):

        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(f'Argument {name} must be {bound_types[name]}')
            return func(*args, **kwargs)

        return wrapper

    return decorate