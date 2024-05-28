import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
username = "oa_kingfaisal"
password = "Asdfgh@098"
browserSortedVeggies = []
driver.get("https://staging-exams.innotech-sa.com/UserManager/Login")
time.sleep(5)
driver.find_element(By.ID,"txtUsername").send_keys(username)

driver.find_element(By.ID,"txtPassword").send_keys(password)
driver.find_element(By.ID,"btnAuthenticate").click()
assert driver.find_element(By.ID, "btnAuthenticate").text == "LOGIN"
time.sleep(5)
ExamManagement = driver.find_element(By.XPATH, "//div[@class='row']/div[@class='col-md col-12']/ul[@id='megamenus']/li[3]")
ManageExam = driver.find_element(By.XPATH, "//span[normalize-space()='List of Courses']")
# actions.move_to_element(Cources).move_to_element(ListOfCources).click().perform()
actions = ActionChains(driver)
actions.move_to_element(ExamManagement).move_to_element(ManageExam).click().perform()

#driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
courcesWebElements  = driver.find_elements(By.XPATH,"//thead/tr/th[5]")
for ele in courcesWebElements:
    browserSortedVeggies.append(ele.text)
OriginalbrowserSortedVeggies = browserSortedVeggies.copy()
browserSortedVeggies.sort()
#newSortedList = browserSortedVeggies.sort()

assert OriginalbrowserSortedVeggies == browserSortedVeggies
driver.quit()


# =============================================================




