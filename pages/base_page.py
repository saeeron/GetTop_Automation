import random

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.gettop_main_url = "https://www.gettop.us/"

    def input_text(self, text, locator):
        self.driver.find_element(*locator).send_keys(text)

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def push_enter(self, locator):
        self.driver.find_element(*locator).send_keys(Keys.RETURN)

    def input_text_push_enter(self, text, locator):
        self.input_text(text, locator)
        self.push_enter(locator)

    def open_page(self, postfix_url: str) -> None:
        self.driver.get(self.gettop_main_url + postfix_url)

    def verify_include_text(self, text, locator):
        actual = self.driver.find_element(*locator).text
        assert text in actual, f"ERROR, {text} is not observed in {actual}"

    def verify_exact_text(self, text, locator):
        actual = self.driver.find_element(*locator).text
        assert text == actual, f"ERROR, expected {text} but observed {actual}"

    def verify_equal_integer(self, int_num, locator):
        actual = int(self.driver.find_element(*locator).text)
        assert actual == int_num, f"ERROR, expected {int_num} but observed {actual}"

    def click_randomly(self, locator):
        elements = self.driver.find_elements(*locator)
        element = elements[random.randint(0, len(elements) + 1)]
        element.click()

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def num_of_elem(self, locator):
        return len(self.driver.find_elements(*locator))

    def wait_until_appearance(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_until_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def mouse_on(self, locator):
        action = ActionChains(self.driver)
        action.move_to_element(self.find_element(locator))
        action.perform()

    def mouse_on_click(self, locator):
        action = ActionChains(self.driver)
        action.move_to_element(self.find_element(locator))
        action.click(self.find_element(locator))
        action.perform()
