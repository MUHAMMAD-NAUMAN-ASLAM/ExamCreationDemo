import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

name = "nauman"
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

radioButtons  = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radioButtons[2].click()
assert  radioButtons[2].is_selected()

driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()

alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept()
time.sleep(5)