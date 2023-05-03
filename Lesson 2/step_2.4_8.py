import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(a):
    return str(math.log(abs(12*math.sin(int(a)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button = browser.find_element(By.ID, "book")
button.click()

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)

answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
answer_input.send_keys(y)

submit_button = browser.find_element(By.ID, "solve")
submit_button.click()

alert = browser.switch_to.alert
print(alert.text)
alert.accept()

browser.quit()
