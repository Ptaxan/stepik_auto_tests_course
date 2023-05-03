import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/math.html"


def calc(a):
    return str(math.log(abs(12*math.sin(int(a)))))


browser.get(link)
# formula = browser.find_element()
x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)

answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
answer_input.send_keys(y)

robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
robot_checkbox.click()

people_radio = browser.find_element(By.ID, "peopleRule")
people_checked = people_radio.get_attribute("checked")
assert people_checked == "true", "People radio is not selected by default"

robots_radio = browser.find_element(By.ID, "robotsRule")
robots_checked = robots_radio.get_attribute("checked")
assert robots_checked is None

browser.quit()
