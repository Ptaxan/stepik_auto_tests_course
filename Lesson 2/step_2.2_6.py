import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(a):
    return str(math.log(abs(12*math.sin(int(a)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)

answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
answer_input.send_keys(y)

robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
robot_checkbox.click()

robots_radio_button = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
robots_radio_button.click()

submit_button = browser.find_element(By.TAG_NAME, "button")
submit_button.click()
time.sleep(5)

browser.quit()
