from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

# Создание экземпляра веб-драйвера для браузера, например, Chrome
driver = webdriver.Chrome()

# Открытие веб-страницы
url = 'https://santegra.com/catalog/category/view/s/katalog/id/3/'  # Укажите здесь URL веб-страницы
driver.get(url)

# Найдите элемент кнопки на странице
button = driver.find_element(By.ID, 'store.menu')

# Эмуляция перемещения мыши к кнопке
actions = ActionChains(driver)
actions.move_to_element(button).perform()
time.sleep(random.uniform(1, 3))

# Эмуляция нажатия на кнопку
button.click()
time.sleep(random.uniform(1, 3))

# Закрытие браузера
driver.quit()
