
from pages.cart_page import CartPage
from pages.category_page import CatPage
from pages.main_page import MainPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.category_page = CatPage(self.driver)


