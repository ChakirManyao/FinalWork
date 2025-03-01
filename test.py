from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Автоматическая установка ChromeDriver
service = Service(ChromeDriverManager().install())

# Создание экземпляра Chrome
driver = webdriver.Chrome(service=service)

# Открытие страницы
driver.get("https://www.google.com")

# Закрытие браузера
driver.quit()