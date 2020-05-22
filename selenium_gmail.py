import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as pg

FULLFILEPATH = r"C:\Users\lakshya\Desktop\myEnvs\autopy\PythonImage.png"
FILENAME = "PythonImage.png"
USERNAME = "YOUR_EMAIL@gmail.com"
PASSWORD = "YOUR_PASSWORD"
RECEIVER_MAIL = "RECEIVER_MAIL@gmail.com"
SUBJECT = "WEB AUTOMATION"
MESSAGE = "This is an auto-generated mail"

IMAGES_FOR_RECOGNITION = ["open.png","open2.png"]

#Starting Chrome and Opening Stackoverflow
driver= webdriver.Chrome()
driver.get("https://stackoverflow.com/users/login")

#Signing in to google from Stack Overflow because google does not allow chromedriver to log in to google directly because of security reasons
signin_google = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.XPATH, '//*[@id="openid-buttons"]/button[1]')))
signin_google.click()

#filling in username field and clicking the next button
email_field = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.XPATH, '//input[@type="email"]')))
email_field = WebDriverWait(driver, 500).until(EC.element_to_be_clickable((By.XPATH, '//input[@type="email"]')))
email_field.send_keys(USERNAME)
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()

#filling in password field and press the signin button
pw_field = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
pw_field = WebDriverWait(driver, 500).until(EC.element_to_be_clickable((By.XPATH, '//input[@type="password"]')))
pw_field.send_keys(PASSWORD)
driver.find_element_by_xpath('//*[@id="passwordNext"]').click()

#opening new window, switching to it and opening gmail in it
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.get('https://gmail.com')

#pressing compose button
compose_button = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[gh='cm']")))
compose_button.click()

#filling in to, subject and message fields and pressing the attach button
to_field = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.XPATH, ".//textarea[contains(@aria-label, 'To')]")))
to_field.click()
to_field.send_keys(RECEIVER_MAIL)
pg.typewrite('\n')

subject_field = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.NAME, "subjectbox")))
subject_field = WebDriverWait(driver, 500).until(EC.element_to_be_clickable((By.NAME, "subjectbox")))
subject_field.click()
subject_field.send_keys(SUBJECT)

message_field = driver.find_element_by_xpath("(.//*[@aria-label='Message Body'])[2]")
message_field.click()
message_field.send_keys(MESSAGE)

attach_button = driver.find_element_by_xpath("//div[contains(@aria-label,'Attach files')]")
attach_button.click()
pg.moveTo(5,5,duration = 0.25)

#Wait for the select file to upload window using image recognition of open button, and add file path 
while True:
    if pg.locateOnScreen(IMAGES_FOR_RECOGNITION[0]) != None or pg.locateOnScreen(IMAGES_FOR_RECOGNITION[1]) != None:
        break
pg.typewrite(FULLFILEPATH)
pg.typewrite('\n')

#Wait for the file to get uploaded
alabel = 'Attachment: '+ FILENAME +'. Press enter to view the attachment and delete to remove it'
wait_for_upload = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.XPATH, "//div[ contains(@aria-label,'"+alabel+"')]")))

#send mail using Ctrl + Enter
driver.find_element_by_xpath("(.//*[@aria-label='Message Body'])[2]").send_keys(Keys.CONTROL + Keys.ENTER)
