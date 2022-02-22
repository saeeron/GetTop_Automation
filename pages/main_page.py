from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):

    SEARCH_BOX = (By.ID, "woocommerce-product-search-field-0")
    SEARCH_ICON = (By.CSS_SELECTOR, "a i.icon-search")
    ACCOUNT_ICON = (By.CSS_SELECTOR, "a.nav-top-link[data-open *= 'login']")
    LOGIN_MFP = (By.XPATH, "//h3[text() = 'Login']")
    CART_ICON = (By.CSS_SELECTOR, ".cart-icon strong")
    EMPTY_CART_ICON_TEXT = (By.XPATH, "//li/div/p[text() = 'No products in the cart.']")

    def _cat_css_selector(self, cat_label):
        return (By.CSS_SELECTOR, f"img[alt = '{cat_label}']")

    def _nav_css_selector(self, nav_item):
        return (By.CSS_SELECTOR, f"a[href *= '{nav_item.lower()}'].nav-top-link")

    def open(self):
        super().open_page("")

    def select_category(self, category_label):
        super().click(self._cat_css_selector(category_label))

    def navigate_to_nav_bar_item(self, nav_name):
        css_selector = self._nav_css_selector(nav_name)
        super().find_element(css_selector).click()

    def is_home_page(self):
        assert self.driver.current_url == "https://gettop.us/" , "ERROR, we are not at home page"

    def search_item(self, item_title):
        actions = ActionChains(self.driver)
        actions.move_to_element(super().find_element(self.SEARCH_ICON))
        actions.perform()
        super().wait_until_appearance(self.SEARCH_BOX).send_keys(item_title, Keys.RETURN)

    def click_on_account(self):
        super().find_element(self.ACCOUNT_ICON).click()

    def wait_until_appearance_login(self):
        super().wait_until_appearance(self.LOGIN_MFP)

    def click_on_cart(self):
        super().find_element(self.CART_ICON).click()

    def mouse_on_cart_icon(self):
        super().mouse_on(self.CART_ICON)

    def presence_of_empty_cart_text(self):
        super().wait_until_appearance(self.EMPTY_CART_ICON_TEXT)

