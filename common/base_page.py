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
        查找单个可见元素

        locator：元素定位方式，例如 (By.ID, "user-name")
        timeout：最长等待时间，默认 10 秒
        """
        # 等待元素可见，而不是只等待元素存在于 DOM 中
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def find_clickable_element(self, locator, timeout=10):
        """
        查找单个可点击元素

        适用于点击按钮、链接等需要交互的元素
        """
        # 等待元素既可见又可点击，减少页面未加载完成导致的点击失败
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator):
        """
        点击元素
        """
        element = self.find_clickable_element(locator)
        element.click()

    def input_text(self, locator, text):
        """
        输入文本

        先清空输入框，再输入内容
        """
        # 输入框需要可交互后再执行 clear 和 send_keys
        element = self.find_clickable_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """
        获取元素文本
        """
        # 获取文本前等待元素可见，避免拿到空文本或隐藏元素文本
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
