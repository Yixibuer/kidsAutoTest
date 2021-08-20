# coding = utf-8
import os
import time
import platform
import logging.config
from utils import config

log_dir_path = config.log_file_path
"""
获取日志记录器
"""


def create_log_file(log_path=None):
    """创建日志文件"""
    if platform.system() == 'Windows':
        if not os.path.exists(log_dir_path):
            os.mkdir(log_dir_path)
        now_date = time.strftime("%Y-%m-%d-%H", time.localtime())
        log_file_path = os.path.join(log_dir_path, f"{now_date}.log")
        if not os.path.exists(log_file_path):
            os.system(f"type nul > {log_file_path}")
        return log_file_path
    if platform.system() in ('Linux', 'Darwin'):
        # 默认使用配置的日志路径，也可以使用自定义的日志路径
        if log_path is None:
            if not os.path.exists(log_dir_path):
                os.mkdir(log_dir_path)
            os.chdir(log_dir_path)
            log_file_name = "{}.log".format(time.strftime("%Y-%m-%d", time.localtime()))
            log_file_path = os.path.join(log_dir_path, log_file_name)
            if not os.path.exists(log_file_path):
                result = os.system("touch {}".format(log_file_name))
                if result != 0:
                    print("当前环境不能创建日志文件")
            os.chdir(config.base_path)
            return log_file_path
        else:
            log_dir, log_file_name = os.path.split(log_path)
            if not os.path.exists(log_dir):
                os.mkdir(log_dir)
            os.chdir(log_dir)
            if not os.path.exists(log_path):
                result = os.system("touch {}".format(log_file_name))
                if result != 0:
                    print("当前环境不能创建日志文件")
            return log_path


def get_logger(log_file_path=None):
    """获取字典配置-日志记录器"""
    if log_file_path is None:
        log_file_name = create_log_file()
    else:
        log_file_name = create_log_file(log_path=log_file_path)
    # 日志配置
    log_config = {
        'version': 1,
        'formatters': {
            'simple': {
                'format': '%(asctime)s %(name)s %(levelname)s %(pathname)s  %(funcName)s line:%(lineno)d  %(message)s',
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'INFO',
                'formatter': 'simple',
                'stream': 'ext://sys.stdout'
            },
            'console_err': {
                'class': 'logging.StreamHandler',
                'level': 'ERROR',
                'formatter': 'simple',
                'stream': 'ext://sys.stderr'
            },
            # 按文件大小分割
            'file': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动按大小分割
                'filename': log_file_name,  # 日志文件
                'maxBytes': 1024 * 1024 * 300,  # 日志大小300M，
                'backupCount': 3,  # 最多备份3个日志文件
                'formatter': 'simple',
                'encoding': 'utf8',
            }
        },
        'loggers': {
            'root': {
                # 既有 console Handler，还有 file Handler
                'handlers': ['console', 'console_err', 'file'],
                'level': 'DEBUG',
                # 'propagate': True,
            }
        }
    }
    logging.config.dictConfig(log_config)
    root_logger = logging.getLogger("root")
    return root_logger


if __name__ != "__main__":
    logger = get_logger()

