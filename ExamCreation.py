import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
username = "oa_kingfaisal"
password = "Asdfg098@"

driver.get("https://dev2.innotech-sa.com/AssessmentSystemV2/Master/System/UserManager/Login")
time.sleep(2)

driver.find_element(By.ID,"txtUsername").send_keys(username)
driver.find_element(By.ID,"txtPassword").send_keys(password)
driver.find_element(By.ID,"btnAuthenticate").click()

assert driver.find_element(By.ID, "btnAuthenticate").text == "LOGIN"
time.sleep(5)

ExamManagement = driver.find_element(By.XPATH, "//div[@class='row']/div[@class='col-md col-12']/ul[@id='megamenus']/li[5]")
ManageExam = driver.find_element(By.XPATH, "//span[normalize-space()='List of Courses']")
time.sleep(5)
actions = ActionChains(driver)
actions.move_to_element(ExamManagement).move_to_element(ManageExam).click().perform()

# Element ko find karo
element = driver.find_element(By.XPATH, "//div[@class='modal-dialog modal-lg model_ExamResultCompilationExams_PopUP']//button[@aria-label='Close']")

# Agar element mojood hai
if element.is_displayed():
    element.click()
    driver.find_element(By.CLASS_NAME, "btnAddNewSessionMain").click()
    driver.find_element(By.XPATH,"//a[normalize-space()='Single Exam']").click()
    time.sleep(3)
    driver.find_element(By.ID,"txtCourseTitle").send_keys("Data")
    driver.find_element(By.ID, "btnSearchCourse").click()
    time.sleep(3)

    courseName = "DS-101_3_2"
    courseName_xpath = f"//*[@id='CoursesDataGrid']/div/table/tbody/tr/td[text()='{courseName}']"
    element_to_hover_over = driver.find_element(By.XPATH, courseName_xpath + "/following-sibling::td[4]/div/a").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[normalize-space()='Standard Exam (Summative/Formative)']").click()
    time.sleep(10)

    ExamName =  "Exam(3 / 3 / 2024)"
    driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div/div/div/div[1]/div[4]/div[1]/div/div[5]/div[1]/div[1]/div/input").send_keys(ExamName)
    driver.find_element(By.XPATH,"//input[@value='11']").click()

    Instruction = "Must attempt all Question"
    driver.find_element(By.XPATH,"//div[@id='txtStudentInstruction']").send_keys(Instruction)

    driver.find_element(By.XPATH, "//input[@class='form-control w-100 m-0 txtTitleSession']").click()
else:
    print("Element nahi mojood hai.")
    driver.find_element(By.CLASS_NAME, "btnAddNewSessionMain").click()

time.sleep(5)

