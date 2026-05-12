import pytest
import allure

from pages.login_page import LoginPage
from pages.product_page import ProductPage


@allure.feature("登录模块")
@allure.story("登录成功")
def test_login_success(driver):
    """
    测试场景：登录成功
    预期结果：登录后进入商品列表页，并显示 Products 标题
    """

    # 1. 创建登录页对象
    login_page = LoginPage(driver)

    # 2. 创建商品页对象
    product_page = ProductPage(driver)

    # 3. 输入正确用户名和正确密码，执行登录
    login_page.login("standard_user", "secret_sauce")

    # 4. 获取商品页标题
    title_text = product_page.get_page_title()

    # 5. 断言商品页标题是否正确
    assert title_text == "Products"


@allure.feature("登录模块")
@allure.story("登录失败")
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        # 场景1：正确用户名 + 错误密码
        ("standard_user", "wrong_password", "Username and password do not match"),

        # 场景2：错误用户名 + 正确密码
        ("wrong_user", "secret_sauce", "Username and password do not match"),

        # 场景3：用户名为空 + 正确密码
        ("", "secret_sauce", "Username is required"),

        # 场景4：正确用户名 + 密码为空
        ("standard_user", "", "Password is required"),

        # 场景5：用户名和密码都为空
        ("", "", "Username is required"),
    ]
)
def test_login_fail(driver, username, password, expected_error):
    """
    测试场景：登录失败数据驱动
    预期结果：页面展示对应错误提示
    """

    # 1. 创建登录页对象
    login_page = LoginPage(driver)

    # 2. 使用参数化数据执行登录
    login_page.login(username, password)

    # 3. 获取错误提示文本
    error_text = login_page.get_error_message()

    # 4. 断言错误提示是否正确
    assert expected_error in error_text