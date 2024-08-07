import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

with open('./challenge_csv.csv','r') as f:
    csv_reader = csv.reader(f)
    
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('https://rpachallenge.com/')
    time.sleep(5)
    start = driver.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button')
    start.click()

    
    csv_reader = list(csv_reader)
    for line in csv_reader[1:]:
        time.sleep(2)

        first_name = driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelFirstName"]')
        first_name.send_keys(line[0])

        last_name = driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelLastName"]')
        last_name.send_keys(line[1])

        company_name = driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelCompanyName"]')
        company_name.send_keys(line[2])

        role = driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelRole"]')
        role.send_keys(line[3])

        name = driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelAddress"]')
        name.send_keys(line[4])

        email = driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelEmail"]')
        email.send_keys(line[5])

        phone = driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelPhone"]')
        phone.send_keys(line[6])

        submit = driver.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input')
        submit.click()
