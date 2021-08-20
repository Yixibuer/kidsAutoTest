import sys, os
import argparse
import time
import shutil
from utils import logger

project_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_path)


def mk_report_dir():
    """创建测试报告目录

    创建allure xml临时目录和allure报告路径

    """
    # 按日期存放报告路径
    report_path = os.path.join(project_path, "report")
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    report_dir_path = os.path.abspath('{0}/{1}'.format(report_path, time.strftime("%Y-%m-%d", time.localtime())))
    if not os.path.exists(report_dir_path):
        os.mkdir(report_dir_path)
    # allure生成xml临时目录
    xml_tmp_path = os.path.join(report_dir_path, "xml_tmp_dir")
    if not os.path.exists(xml_tmp_path):
        os.mkdir(xml_tmp_path)
    # allure报告路径
    now_time = time.strftime("%H%M%S", time.localtime())
    allure_report_path = os.path.join(report_dir_path, "AllureReport{}".format(now_time))
    if not os.path.exists(allure_report_path):
        os.mkdir(allure_report_path)
    return xml_tmp_path, allure_report_path


def mk_allure_report(test_report_path, xml_tmp_path):
    """生成allure测试报告

    """
    # 生成测试报告
    logger.info("开始生成allure测试报告")
    os.system(f"allure generate {xml_tmp_path} -o {test_report_path} -c")
    logger.info(f"生成allure报告完毕，报告路径：{test_report_path}")
    # 删除xml文件目录
    shutil.rmtree(xml_tmp_path)
    logger.info("删除临时xml文件完成")
    logger.info("打开测试报告")
    os.system(f'allure open {test_report_path}')


def exe_command(case_path, xml_tmp_path, cpu_count=1, fail_run_times=0):
    """拼接执行pytest 命令

    :Args:
         - case_path - 用例路径，多个路径则用空格分割
         - xml_tmp_path - allure xml临时文件目录
         - cpu_count - 进程数，默认为1
    """
    if isinstance(case_path, str):
        exec_command = f"python3 -m pytest {case_path} --alluredir={xml_tmp_path} -n={cpu_count} --reruns={fail_run_times}"
        logger.debug("pytest拼接的命令：{}".format(exec_command))
        os.system(exec_command)
    else:
        exec_command = f"python3 -m pytest {'{} ' * len(case_path)} --alluredir={xml_tmp_path} -n={cpu_count} --reruns={fail_run_times}"
        exec_command = exec_command.format(*case_path)
        logger.debug("多个文件路径，pytest拼接的命令：{}".format(exec_command))
        os.system(exec_command)


def pytest_main(case_path, cpu_count=1):
    """执行用例，生成测试报告"""
    # 创建测试报告目录
    xml_tmp_path, allure_report_path = mk_report_dir()
    # 执行命令
    exe_command(case_path, xml_tmp_path, cpu_count)
    # xml_tmp_path不为空，则生成报告
    if os.listdir(xml_tmp_path):
        # 生成allure测试报告
        mk_allure_report(allure_report_path, xml_tmp_path)


def main():
    """解析命令行参数

    拼接pytest命令，执行测试用例
    """
    parser = argparse.ArgumentParser(description="自动化运行参数")
    # 测试用例路径
    parser.add_argument('--case-path', '-c', nargs='+', help="用例路径，多个路径空格分割", type=str)
    parser.add_argument('--cpu-count', '-n', help="进程数", type=int)
    parser.add_argument('--env', '-e', help="运行环境", type=str)
    parser.add_argument('--browser', '-b', help="运行的浏览器，支持chrome、firefox", type=str)
    # 无头模式
    parser.add_argument('--headless', '-m', nargs='?', help="无头模式", type=str, const="True")
    # 不同驱动
    parser.add_argument('--platform', '-p', help="驱动模式，支持web、android、ios、grid ", type=str)
    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    # 平台参数
    platform = args.platform
    # 运行的浏览器
    browser = args.browser
    # 环境
    env = args.env
    # 无头模式，命令行中不用加参数，直接--headless即可
    headless = args.headless
    if platform:
        if platform not in ('web', 'android', 'ios', 'grid'):
            raise ValueError('可选值：web、android、ios、grid')
        # 设置环境变量
        else:
            os.environ['platform'] = platform
            # web端设置浏览器和无头模式
            if platform in ('web', 'grid'):
                if browser:
                    if browser not in ('chrome', 'firefox'):
                        raise ValueError('可选值：chrome、firefox')
                    os.environ['browser'] = browser
                if headless:
                    os.environ['headless'] = headless
    # 运行环境
    if env is not None:
        if env not in ('test', 'staging', 'prod'):
            raise ValueError('环境请输入test、staging、prod')
        os.environ['env'] = env
    # 用例路径
    case_path = args.case_path
    if not case_path:
        raise ValueError('请输入用例路径')
    # 进程数
    cpu_count = args.cpu_count
    if not cpu_count:
        pytest_main(case_path)
    else:
        pytest_main(case_path, cpu_count=cpu_count)


if __name__ == "__main__":
    """命令行示例

    使用默认配置运行测试用例（默认配置要和运行的用例匹配）
    python main.py --case-path testcase/ios
    python main.py -c testcase/ios

    选择运行平台，测试环境，执行测试用例
    python main.py -c testcase/ios -p ios -e test 

    选择运行平台，测试环境，浏览器，执行测试用例
    python main.py --case-path testcase/web --platform web -env test -browser chrome
    """
    main()
