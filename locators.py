from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Rana")
driver.find_element(By.NAME, "email").send_keys("nauman.aslam2@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
messgae1 = driver.find_element(By.CLASS_NAME, "alert-success").text
print(messgae1)
assert "Success" in messgae1
driver.find_element(By.CSS_SELECTOR, "input[id='inlineRadio1']").click()
driver.find_element(By.XPATH,"(//input[@name='name'])[2]").send_keys("Hellow again")





