- 前置条件
> 移动端需要安装Appium环境，参见移动端环境搭建文档[https://shimo.im/docs/Ee32M7or25C8Z6A2][https://shimo.im/docs/Ee32M7or25C8Z6A2]

- 项目克隆
> git clone https://gitlab.codemao.cn/testing/creation-tools/nemo_ui_ios.git -b dev

- 安装依赖库
> pip install -r requirement.txt 

- 运行用例-生成报告-命令行示例
```
使用默认配置运行测试用例（默认配置要和运行的用例匹配）
python main.py --case-path testcase/ios
python main.py -c testcase/ios

选择运行平台，测试环境，执行测试用例
python main.py -c testcase/ios -p ios -e test 

选择运行平台，测试环境，浏览器，执行测试用例
python main.py --case-path testcase/web --platform web -env test -browser chrome
```

[https://shimo.im/docs/Ee32M7or25C8Z6A2]: https://shimo.im/docs/Ee32M7or25C8Z6A2