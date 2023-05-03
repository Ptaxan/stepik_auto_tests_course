import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/get_attribute.html"


def calc(a):
    return str(math.log(abs(12*math.sin(int(a)))))


browser.get(link)

chest = browser.find_element(By.ID, "treasure")
x = chest.get_attribute("valuex")
y = calc(x)

answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
answer_input.send_keys(y)

robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
robot_checkbox.click()

robots_radio_button = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
robots_radio_button.click()

submit_button = browser.find_element(By.TAG_NAME, "button")
submit_button.click()

time.sleep(1)

browser.quit()
