from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import Page


class MainPage(Page):

    CART = (By.ID, "nav-cart-count-container")
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    DEPARTMENT_DROPDOWN = (By.ID, "searchDropdownBox")

    def _cat_css_selector(self, cat_label):
        return (By.CSS_SELECTOR, f"img[alt = '{cat_label}']")

    def open(self):
        super().open_page("")

    def select_category(self, category_label):
        super().click(self._cat_css_selector(category_label))

    def click_on_cart(self):
        super().click(self.CART)

    def search_item(self, item_name):
        super().input_text_push_enter(item_name, self.SEARCH_BOX)
