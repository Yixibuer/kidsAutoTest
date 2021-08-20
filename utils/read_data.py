import yaml
import os
import codecs
from utils import common


class Data:
    """读取yaml数据

    根据不同环境配置读取不同的测试数据
    """

    def __init__(self):
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        env = common.get_env_var('env')
        if env == 'test':
            test_data_path = os.path.join(self.base_path, 'data', 'test_data.yml')
        elif env == 'staging':
            test_data_path = os.path.join(self.base_path, 'data', 'staging_data.yml')
        elif env == 'prod':
            test_data_path = os.path.join(self.base_path, 'data', 'pro_data.yml')
        else:
            raise ValueError("请输入有效的环境，如：'test', 'staging', 'prod'")

        yml_obj = codecs.open(test_data_path, 'r', "utf-8")
        self.yml_data = yaml.safe_load(yml_obj)

        # 登录账号
        invalid_login_data = self.yml_data["invalid_login_data"]
        valid_login_data = self.yml_data["valid_login_data"]

        # 转换为数组
        invalid_login_data = list(invalid_login_data.values())
        self.invalid_login_data = list(zip(*invalid_login_data))
        # 有效登录账号数据
        self.valid_tel_pwd = valid_login_data['tel_pwd']


if __name__ != "__main__":
    data = Data()
