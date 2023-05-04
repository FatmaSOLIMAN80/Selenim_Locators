# selenium 4

import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/login?returnUrl=%2F")
driver.find_element(By.ID, "Email").send_keys("test@test.com")
driver.find_element(By.ID, "Password").send_keys("test123")
driver.find_element(By.CLASS_NAME,"login-button").click()
driver.find_element(By.CLASS_NAME,"validation-summary-errors").is_displayed()
msg_erreur=driver.find_element(By.CLASS_NAME,"validation-summary-errors").text
#assert "Login Fatma was unsuccessful." in msg_erreur
assert msg_erreur=="""Login was unsuccessful. Please correct the errors and try again.
No customer account found"""
print(msg_erreur)
time.sleep(3)
driver.close()
