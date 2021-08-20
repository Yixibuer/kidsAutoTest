from ocv.resolution import cocos_min_strategy
from utils import config


class Settings(object):
    """图像识别相关参数设置"""
    DEBUG = False
    SS_DIR = None
    RESIZE_METHOD = staticmethod(cocos_min_strategy)
    CVSTRATEGY = ["surf", "tpl", "brisk"]  # keypoint matching: kaze/brisk/akaze/orb, contrib: sift/surf/brief
    KEYPOINT_MATCHING_PREDICTION = True
    # 点击操作的默认识别匹配度
    THRESHOLD = 0.7  # [0, 1]
    # 查找页面是否存在的默认识别匹配度
    THRESHOLD_STRICT = 0.8  # [0, 1]
    # 识别的图片所在文件夹路径，根据需要自行修改
    IMG_DIR_PATH = config.player_path
    OPDELAY = 0.1
    # 识别图像的默认超时时间
    FIND_TIMEOUT = 20
    FIND_TIMEOUT_TMP = 3
    # 截图的质量
    SNAPSHOT_QUALITY = 10  # 1-99 https://pillow.readthedocs.io/en/5.1.x/handbook/image-file-formats.html#jpeg
