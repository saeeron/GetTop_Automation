from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import Page


class CartPage(Page):
    EMPTY_CART = (By.CSS_SELECTOR, ".cart-empty")
    REMOVE_FROM_CART = (By.CSS_SELECTOR, ".remove")
    EMPTY_CART_TEXT = (By.XPATH, "//p[text() = 'Your cart is currently empty.']")

    def open(self):
        super().open_page("cart/")

    def is_cart_empty(self):
        assert len(super().find_elements(self.EMPTY_CART)) != 0, "Expected added item, but nothing int the cart"

    def empty_cart(self):
        remove_elem = super().find_elements(self.REMOVE_FROM_CART)
        for i in range(len(remove_elem)):
            remove_elem[i].click()

    def is_empty_cart_page(self):
        super().wait_until_appearance(self.EMPTY_CART_TEXT)




