import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
Select(driver.find_element())
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
#index = dropdown.select_by_index(0)
index = dropdown.select_by_visible_text("Female")
print(index)
time.sleep(10)

