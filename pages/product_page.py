from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 把登录成功后的商品页也封装成 Page Object。
class ProductPage:
    """
    商品列表页面对象类

    作用：
    1. 封装商品页的元素定位
    2. 封装商品页相关操作
    3. 给测试用例提供更清晰的方法
    """

    def __init__(self, driver):
        """
        初始化商品页对象

        参数：
        driver：浏览器驱动对象，由 conftest.py 传入
        """

        # 保存浏览器驱动对象
        self.driver = driver

        # 创建显式等待对象，最多等待 10 秒
        self.wait = WebDriverWait(driver, 10)

    def get_page_title(self):
        """
        获取商品页标题文本

        返回值：
        页面标题文字，比如 Products
        """

        # 等待 class="title" 的标题元素可见
        title_element = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "title"))
        )

        # 返回标题文本
        return title_element.text