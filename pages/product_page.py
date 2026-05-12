from selenium.webdriver.common.by import By
from common.base_page import BasePage


class ProductPage(BasePage):
    """
    商品页面类：封装商品页面相关操作
    """

    # 商品页页面标题元素：Products
    product_title = (By.CLASS_NAME, "title")

    def get_product_title(self):
        """
        获取商品页面标题文字
        """
        return self.get_text(self.product_title)