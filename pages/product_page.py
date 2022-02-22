from selenium.webdriver.common.by import By

from pages.base_page import Page


class ProductPage(Page):

    ICON = (By.CSS_SELECTOR, "a[href='https://gettop.us/']")
    PRICE = (By.CSS_SELECTOR, ".product-info .woocommerce-Price-amount")
    QUANTITY_BOX = (By.CSS_SELECTOR, ".input-text[min = '1']")
    ADD_TO_CART = (By.CSS_SELECTOR, "button[name = 'add-to-cart']")
    unit_price = None
    quantity = None

    def click_on_homepage(self):
        super().find_element(self.ICON).click()

    def _read_current_price_text(self):
        elems = super().find_elements(self.PRICE)
        self.unit_price = elems[-1].text
        print(self.unit_price)

    def set_quantity(self, num):
        super().find_element(self.QUANTITY_BOX).clear()
        super().find_element(self.QUANTITY_BOX).send_keys(num)
        self.quantity = num
        print(self.quantity)

    def push_add_to_cart(self):
        self._read_current_price_text()
        self.find_element(self.ADD_TO_CART).click()

