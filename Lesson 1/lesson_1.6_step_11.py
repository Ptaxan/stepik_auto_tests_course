import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# link = "http://suninjuly.github.io/registration2.html"
link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
first_name.send_keys("Ivan")
last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")
last_name.send_keys("Petrov")
email = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
email.send_keys("ivanpetrov@sob.com")
button = browser.find_element(By.TAG_NAME, "button")
button.click()
time.sleep(1)

success = browser.find_element(By.TAG_NAME, "h1")
assert success.text == "Congratulations! You have successfully registered!"

time.sleep(10)
browser.quit()
