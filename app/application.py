
from pages.cart_page import CartPage
from pages.category_page import CatPage
from pages.main_page import MainPage
from pages.nav_page import NavPage
from pages.product_page import ProductPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.category_page = CatPage(self.driver)
        self.nav_page = NavPage(self.driver)
        self.product_page = ProductPage(self.driver)



