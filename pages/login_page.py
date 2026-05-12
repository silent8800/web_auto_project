from selenium.webdriver.common.by import By
from common.base_page import BasePage


class LoginPage(BasePage):
    """
    登录页面类：封装登录页面的元素和操作
    """

    # 用户名输入框
    username_input = (By.ID, "user-name")

    # 密码输入框
    password_input = (By.ID, "password")

    # 登录按钮
    login_button = (By.ID, "login-button")

    # 登录失败错误提示
    error_message = (By.CSS_SELECTOR, "[data-test='error']")

    def login(self, username, password):
        """
        登录操作
        """
        self.input_text(self.username_input, username)
        self.input_text(self.password_input, password)
        self.click(self.login_button)

    def get_error_message(self):
        """
        获取登录失败提示信息
        """
        return self.get_text(self.error_message)
