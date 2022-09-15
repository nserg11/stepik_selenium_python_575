from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

# говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/cats.html")

button = browser.find_element(By.ID, "button")
#assert "successful" in message.text

time.sleep(5)
# закрываем браузер после всех манипуляций
browser.quit()
