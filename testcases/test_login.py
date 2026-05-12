import pytest
import allure
from pages.login_page import LoginPage
from pages.product_page import ProductPage


@allure.feature("登录模块")
class TestLogin:

    @allure.story("正常登录")
    def test_login_success(self, driver):
        login_page = LoginPage(driver)
        product_page = ProductPage(driver)

        login_page.login("standard_user", "secret_sauce")

        assert product_page.get_product_title() == "Products"

    @allure.story("异常登录")
    @pytest.mark.parametrize("username,password,expected_msg", [
        ("wrong_user", "wrong_password", "Username and password do not match"),
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
        ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out"),
    ])
    def test_login_fail(self, driver, username, password, expected_msg):
        login_page = LoginPage(driver)

        login_page.login(username, password)

        assert expected_msg in login_page.get_error_message()