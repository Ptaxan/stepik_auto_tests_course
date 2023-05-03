import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

firstname = browser.find_element(By.XPATH, "//input[contains(@name, 'firstname')]")
firstname.send_keys("Ivan")
lastname = browser.find_element(By.XPATH, "//input[contains(@name, 'lastname')]")
lastname.send_keys("Petrov")
email = browser.find_element(By.XPATH, "//input[contains(@name, 'email')]")
email.send_keys("email")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "file.txt")
file_button = browser.find_element(By.ID, "file")
file_button.send_keys(file_path)

submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
submit_button.click()
time.sleep(5)

browser.quit()
