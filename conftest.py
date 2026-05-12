import os
import time
import pytest
import allure
from selenium import webdriver

# 从配置文件中导入被测系统地址
from config.config import BASE_URL


@pytest.fixture
def driver(request):
    """
    公共 fixture：统一管理浏览器的打开、关闭，以及失败截图

    用例执行前：
    1. 打开 Chrome 浏览器
    2. 最大化窗口
    3. 打开被测系统登录页

    用例执行后：
    1. 如果用例失败，保存当前页面截图
    2. 把失败截图附加到 Allure 报告中
    3. 关闭浏览器
    """

    # 1. 启动 Chrome 浏览器
    driver = webdriver.Chrome()

    # 2. 最大化浏览器窗口，避免元素被遮挡
    driver.maximize_window()

    # 3. 打开被测系统登录页面
    driver.get(BASE_URL)

    # 4. yield 前面是用例执行前的准备工作
    yield driver

    # 5. 判断当前用例是否执行失败
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:

        # 如果 screenshots 文件夹不存在，就自动创建
        os.makedirs("screenshots", exist_ok=True)

        # 获取当前测试用例名称
        case_name = request.node.name

        # 获取当前时间，避免截图文件重名
        current_time = time.strftime("%Y%m%d_%H%M%S")

        # 拼接截图保存路径
        screenshot_path = f"screenshots/{case_name}_{current_time}.png"

        # 保存当前浏览器页面截图到本地
        driver.save_screenshot(screenshot_path)

        # 把截图附加到 Allure 报告里
        allure.attach.file(
            screenshot_path,
            name="失败页面截图",
            attachment_type=allure.attachment_type.PNG
        )

        print(f"用例失败，已保存截图并附加到 Allure：{screenshot_path}")

    # 6. 关闭浏览器
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    pytest 钩子函数：获取每条用例的执行结果

    作用：
    让 fixture 里面可以通过 request.node.rep_call 判断用例是否失败
    """

    # 执行测试用例，并获取结果
    outcome = yield

    # 获取测试报告对象
    report = outcome.get_result()

    # 把执行结果保存到 item 上
    # setup：前置阶段
    # call：测试用例执行阶段
    # teardown：后置阶段
    setattr(item, "rep_" + report.when, report)