# this is for scratch codes
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait

# setting up driver as chrome_driver and waits
driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.wait = WebDriverWait(driver, 10)   # explicitly waiting

driver.get("https://gettop.us/product-category/accessories/")

print(driver.find_element(By.CSS_SELECTOR, ".product-small .box").find_element(By.XPATH, "//a[contains(@href , 'gettop')]").text)


sleep(5)

driver.quit()


