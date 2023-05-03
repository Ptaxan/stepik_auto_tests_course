import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'http://suninjuly.github.io/registration1.html'

try:
    browser = webdriver.Chrome()
    browser.get(URL)

    input1 = browser.find_element(By.CLASS_NAME, 'first_block .first')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CLASS_NAME, 'first_block .second')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'first_block .third')
    input3.send_keys("example@gmail.com")
    input4 = browser.find_element(By.CLASS_NAME, 'second_block .first')
    input4.send_keys("1950876432")
    input5 = browser.find_element(By.CLASS_NAME, 'second_block .second')
    input5.send_keys("Russia")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(30)
    browser.quit()
