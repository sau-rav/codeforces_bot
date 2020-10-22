from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

input_problem = '1288/C'
driver = webdriver.Chrome('/home/saurav/Downloads/chromedriver')
driver.get('https://codeforces.com/enter?back=%2F')
user_name = driver.find_element_by_id('handleOrEmail')
user_name.send_keys("saussage")
password = driver.find_element_by_id('password')
password.send_keys("*********")
submit = driver.find_element_by_class_name('submit')
submit.click()
try:
    user = WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'header-bell'))
    )
finally:
    driver.get('https://codeforces.com/problemset/submit')

problem = driver.find_element_by_name('submittedProblemCode')
try:
    problemInput = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.NAME, 'submittedProblemCode'))
    )
finally:
    problem.send_keys(input_problem)

language = driver.find_element_by_name('programTypeId')
language.send_keys('GNU G++14 6.4.0')

toggleEditor = driver.find_element_by_id('toggleEditorCheckbox')
toggleEditor.click()

try:
    problemInput = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'sourceCodeTextarea'))
    )
finally:
    code = driver.find_element_by_id('sourceCodeTextarea')

filepath = 'code.cpp'
with open(filepath) as fp:
    line = fp.readline()
    while line:
        code.send_keys(line)
        line = fp.readline()

time.sleep(3)
submit = driver.find_element_by_class_name('submit')
submit.click()
