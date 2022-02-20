from selenium.webdriver.common.by import By

from pages.base_page import Page


class ProductPage(Page):

    ICON = (By.CSS_SELECTOR, "a[href='https://gettop.us/' ]")

    def click_on_homepage(self):
        super().find_element(self.ICON).click()
