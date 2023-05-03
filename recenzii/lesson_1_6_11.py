from selenium import webdriver
from selenium.webdriver.common.by import By
import time

value1 = "//input[@placeholder='Input your first name']"
value2 = "//input[@placeholder='Input your last name']"
value3 = "//input[@placeholder='Input your email']"

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, value3)
    input3.send_keys("test@mail.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
