from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

filepath = sys.argv[1]
with open(filepath) as fp:
    line = fp.readline()
input_problem = line[2:]

print("submitting problem {}".format(input_problem))

driver = webdriver.Chrome('/pathtochromedriver')
driver.get('https://codeforces.com/problemset/problem/{}'.format(input_problem))

enter = driver.find_element_by_xpath("//a[contains(@href, '/enter?back=')]")
enter.click()

try:
    user = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'handleOrEmail'))
    )
finally:
    user_name = driver.find_element_by_id('handleOrEmail')

user_name.send_keys("saussage")
password = driver.find_element_by_id('password')
password.send_keys("********")
submit = driver.find_element_by_class_name('submit')
submit.click()

try:
    submission = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'second-level-menu'))
    )
finally:
    submit = driver.find_element_by_xpath("//a[contains(@href, '/problemset/submit')]")

submit.click()

try:
    load = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'programTypeId'))
    )
finally:
    language = driver.find_element_by_name('programTypeId')

language.send_keys('GNU G++14 6.4.0')

try:
    load_chck = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'toggleEditorCheckbox'))
    )
finally:
    toggleEditor = driver.find_element_by_id('toggleEditorCheckbox')

toggleEditor.click()

try:
    problemInput = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'sourceCodeTextarea'))
    )
finally:
    code = driver.find_element_by_id('sourceCodeTextarea')

with open(filepath) as fp:
    line = fp.readline()
    while line:
        code.send_keys(line)
        line = fp.readline()

submit = driver.find_element_by_class_name('submit')
#submit.click()
