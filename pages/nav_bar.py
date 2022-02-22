from selenium.webdriver.common.by import By

from pages.base_page import Page


class NavBarPage(Page):

    SUBTOTAL = (By.CSS_SELECTOR, "#masthead .woocommerce-Price-amount")
    QUANTITY = (By.CSS_SELECTOR, "#masthead .hide-for-medium .image-icon strong")
    PRODUCT = (By.CSS_SELECTOR, ".mini_cart_item a")
    VIEW_CART = (By.XPATH, "//div[contains(@class, 'hide-for-medium')]//a[contains(@class , 'button') and text() = "
                           "'View cart'  ]")

    CHECKOUT = (By.XPATH, "//div[contains(@class, 'hide-for-medium')]//a[contains(@class , 'button') and text() = "
                          "'Checkout'  ]")
    CLOSE_BTN = (By.CSS_SELECTOR, ".hide-for-medium .remove")

    subtotal = None
    quantity = None
    product = None

    def read_subtotal(self):
        self.subtotal = super().find_element(self.SUBTOTAL).text
        print(self.subtotal)

    def read_quantity(self):
        self.quantity = super().find_element(self.QUANTITY).text

    def read_product(self):
        self.product = super().find_elements(self.PRODUCT)[1].text

    def view_cart_is_present(self):
        super().wait_until_appearance(self.VIEW_CART)

    def click_on_view_cart(self):
        super().wait_until_clickable(self.VIEW_CART).click()

    def checkout_is_present(self):
        super().wait_until_appearance(self.CHECKOUT)

    def click_on_checkout(self):
        super().wait_until_clickable(self.CHECKOUT).click()

    def click_on_remove_item(self):
        super().mouse_on_click(self.CLOSE_BTN)



