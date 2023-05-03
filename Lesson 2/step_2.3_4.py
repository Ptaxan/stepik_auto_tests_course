import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(a):
    return str(math.log(abs(12*math.sin(int(a)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

journey_button = browser.find_element(By.TAG_NAME, "button")
journey_button.click()

confirm = browser.switch_to.alert
confirm.accept()

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

answer_input = browser.find_element(By.ID, "answer")
answer_input.send_keys(y)

submit_button = browser.find_element(By.TAG_NAME, "button")
submit_button.click()

time.sleep(5)
browser.quit()
