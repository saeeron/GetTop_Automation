from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page


class CatPage(Page):
    PRODUCT_BOX = (By.CSS_SELECTOR, ".box-text.box-text-products")
    PRODUCT_BOX_IMAGE = (By.CSS_SELECTOR, ".product-small.box")
    LABEL = (By.CSS_SELECTOR, ".product-small.box p.category")
    COUNT_TEXT_PARAGRAPH = (By.XPATH, "//p[contains(text(), 'Showing')]")

    QUICK_VIEW = (By.CSS_SELECTOR, ".quick-view")
    QV_CLOSE_BTN = (By.CSS_SELECTOR, "button.mfp-close")

    ADD_TO_CART = (By.CSS_SELECTOR, "button[name = 'add-to-cart']")

    CART_ICON = (By.CSS_SELECTOR, ".cart-icon strong")

    REMOVE_BTN = (By.CSS_SELECTOR, "a.remove")

    PRICE = (By.CSS_SELECTOR, "p.category")
    TITLE = (By.CSS_SELECTOR, "a[href]")
    NAME = (By.CSS_SELECTOR, "span.amount")

    def check_text_labels(self, cat_label):
        all_items = super().find_elements(self.LABEL)
        assert all([elem.text.upper() == cat_label.upper() for elem in all_items]), \
            f"ERROR, one or more items do(es) not have expected label {cat_label} "

    def check_count(self, cat_label):
        count_of_items = len(super().find_elements(self.LABEL))
        expected_str = f"Showing all {count_of_items} results"
        actual_str = super().find_element(self.COUNT_TEXT_PARAGRAPH).text
        assert expected_str == actual_str, \
            f"ERROR, expected  {expected_str}, but observing {actual_str} on the page"

    def count_name_price_title(self):
        all_items = super().find_elements(self.PRODUCT_BOX)
        names = []
        prices = []
        titles = []
        for elem in all_items:
            if elem.find_element(*self.PRICE).text.strip() != '':
                prices.append(elem.find_element(*self.PRICE).text)
            if elem.find_element(*self.NAME).text.strip() != '':
                names.append(elem.find_element(*self.NAME).text)
            if elem.find_element(*self.TITLE).text.strip() != '':
                titles.append(elem.find_element(*self.TITLE).text)

        assert len(names) == len(prices) == len(titles) > 0, "some names, titles, or prices are missing"

    def open_and_close_quick_view(self):

        elements = super().find_elements(self.PRODUCT_BOX_IMAGE)

        for i in range(len(elements)):
            actions = ActionChains(self.driver)
            elements_ = super().find_elements(self.PRODUCT_BOX)
            actions.move_to_element(elements_[i])
            elements_qv = super().find_elements(self.QUICK_VIEW)
            actions.click(elements_qv[i])
            actions.perform()
            actions.reset_actions()
            super().wait_until_clickable(self.QV_CLOSE_BTN).click()

    def add_to_cart(self):

        elements = super().find_elements(self.PRODUCT_BOX_IMAGE)

        num_added_items = 0
        for i in range(len(elements)):
            actions = ActionChains(self.driver)
            elements_icon = super().find_elements(self.PRODUCT_BOX_IMAGE)
            elements_box = super().find_elements(self.PRODUCT_BOX)
            if len(elements_icon[i].find_elements(By.CSS_SELECTOR, ".out-of-stock-label")) == 1:
                print("this product has been sold out")
                continue

            actions.move_to_element(elements_box[i])
            elements_qv = super().find_elements(self.QUICK_VIEW)
            actions.click(elements_qv[i])
            actions.perform()
            actions.reset_actions()
            super().wait_until_clickable(self.ADD_TO_CART).click()
            num_added_items += 1

        self.cart_is_not_empty(num_added_items)

    def cart_is_not_empty(self, num_added_items):
        elem = super().find_elements(self.CART_ICON)
        assert elem[0].text != f"\"{num_added_items}\"", f"ERROR, expected {num_added_items} item in the cart," \
                                                         f" but it shows {elem[0].text} item"
