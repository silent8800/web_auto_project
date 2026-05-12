from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    页面基础类：封装 Web 自动化中常用的公共操作

    作用：
    1. 统一封装元素查找
    2. 统一封装点击、输入、获取文本等操作
    3. 加入显式等待，提高用例稳定性
    """

    def __init__(self, driver):
        # 接收浏览器驱动对象
        self.driver = driver

    def find_element(self, locator, timeout=10):
        """
        查找单个元素

        locator：元素定位方式，例如 (By.ID, "user-name")
        timeout：最长等待时间，默认 10 秒
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator):
        """
        点击元素
        """
        self.find_element(locator).click()

    def input_text(self, locator, text):
        """
        输入文本

        先清空输入框，再输入内容
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """
        获取元素文本
        """
        return self.find_element(locator).text

    def get_title(self):
        """
        获取页面标题
        """
        return self.driver.title

    def get_current_url(self):
        """
        获取当前页面 URL
        """
        return self.driver.current_url