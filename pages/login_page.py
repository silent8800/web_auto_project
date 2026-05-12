from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    登录页面对象类

    作用：
    1. 管理登录页面的元素定位
    2. 封装登录页面的操作方法
    3. 让测试用例不直接关心元素怎么定位
    """

    def __init__(self, driver):
        """
        初始化方法

        参数：
        driver：浏览器驱动对象，由 conftest.py 中的 fixture 传入
        """

        # 保存 driver，后面页面操作都通过 self.driver 完成
        self.driver = driver

        # 创建显式等待对象，最多等待 10 秒
        self.wait = WebDriverWait(driver, 10)

    def input_username(self, username):
        """
        输入用户名
        """

        # 等待用户名输入框可见，然后输入用户名
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys(username)

    def input_password(self, password):
        """
        输入密码
        """

        # 等待密码输入框可见，然后输入密码
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "password"))
        ).send_keys(password)

    def click_login_button(self):
        """
        点击登录按钮
        """

        # 等待登录按钮可点击，然后点击
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        ).click()

    def login(self, username, password):
        """
        登录公共方法

        作用：
        把输入用户名、输入密码、点击登录三个动作封装到一起
        """

        self.input_username(username)
        self.input_password(password)
        self.click_login_button()

    def get_error_message(self):
        """
        获取登录失败后的错误提示文本
        """

        # 等待错误提示元素可见
        error_element = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="error"]'))
        )

        # 返回错误提示文本
        return error_element.text
