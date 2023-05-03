import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
# link = "http://suninjuly.github.io/selects1.html"
link = "http://suninjuly.github.io/selects2.html"
browser.get(link)

num1 = browser.find_element(By.ID, "num1").text
num2 = browser.find_element(By.ID, "num2").text
summa = str(int(num1) + int(num2))

select = Select(browser.find_element(By.TAG_NAME, "select"))
# select.select_by_value(summa)
select.select_by_visible_text(summa)

button = browser.find_element(By.TAG_NAME, "button")
button.click()

time.sleep(5)

browser.quit()
