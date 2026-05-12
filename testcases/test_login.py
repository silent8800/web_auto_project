import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    """
    fixture：管理浏览器的打开和关闭

    用例执行前：
    1. 打开 Chrome 浏览器
    2. 最大化窗口
    3. 打开登录页面

    用例执行后：
    1. 关闭浏览器
    """

    # 1. 打开 Chrome 浏览器
    driver = webdriver.Chrome()

    # 2. 最大化浏览器窗口，避免元素被遮挡
    driver.maximize_window()

    # 3. 打开被测系统登录页
    driver.get("https://www.saucedemo.com/")

    # 4. yield 前面的代码，相当于用例执行前的准备工作
    yield driver

    # 5. yield 后面的代码，相当于用例执行后的清理工作
    driver.quit()


def test_login_success(driver):
    """
    测试场景：登录成功
    """

    # 1. 创建显式等待对象
    wait = WebDriverWait(driver, 10)

    # 2. 输入正确用户名
    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")

    # 3. 输入正确密码
    wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    ).send_keys("secret_sauce")

    # 4. 点击登录按钮
    wait.until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    ).click()

    # 5. 等待登录成功后的 Products 标题可见
    title_element = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    # 6. 断言页面标题是否正确
    assert title_element.text == "Products"


def test_login_fail_wrong_password(driver):
    """
    测试场景：登录失败：正确用户名 + 错误密码
    """

    # 1. 创建显式等待对象
    wait = WebDriverWait(driver, 10)

    # 2. 输入正确用户名
    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")

    # 3. 输入错误密码
    wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    ).send_keys("wrong_password")

    # 4. 点击登录按钮
    wait.until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    ).click()

    # 5. 等待错误提示信息可见
    error_message = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="error"]'))
    )

    # 6. 断言错误提示是否正确
    assert "Username and password do not match" in error_message.text