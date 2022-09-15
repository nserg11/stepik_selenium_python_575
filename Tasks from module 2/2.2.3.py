from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1_element = browser.find_element(By.ID, "num1")
    num1 = num1_element.text
    num2_element = browser.find_element(By.ID, "num2")
    num2 = num2_element.text

    # print(type(num1))

    summa = str(int(num1) + int(num2))

    select1 = Select(browser.find_element(By.TAG_NAME, "select"))
    select1.select_by_value(summa)  # ищем элемент с текстом summa

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
