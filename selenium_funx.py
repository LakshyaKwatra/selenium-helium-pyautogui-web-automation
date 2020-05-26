import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as pg
from selenium.common.exceptions import NoSuchElementException
import requests
from getpass import getpass
#https://testguild.com/selenium-webdriver-fix-for-3-common-ie-errors/


def download(url,file_download_path):
    print('\nDownloading the file from ' + url + '\n')
    myfile = requests.get(url)
    open(file_download_path, 'wb').write(myfile.content)

def check_exists_by_xpath(driver,xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def gmail_login(driver,USERNAME,PASSWORD):
    driver.get("https://mail.google.com/")
    while True:
        if check_exists_by_xpath(driver,"//div[contains(text(),'Choose an account')]") or check_exists_by_xpath(driver,'//input[@type="email"]'):
            break
    if check_exists_by_xpath(driver,"//div[contains(text(),'Use another account')]"):
        driver.find_element_by_xpath("//div[contains(text(),'Use another account')]").click()
    email_field = WebDriverWait(driver, 500).until(EC.element_to_be_clickable((By.XPATH, '//input[@type="email"]')))
    email_field.send_keys(USERNAME+'\n')
    pw_field = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
    pw_field = WebDriverWait(driver, 500).until(EC.element_to_be_clickable((By.XPATH, '//input[@type="password"]')))
    pw_field.send_keys(PASSWORD)
    driver.find_element_by_xpath('//*[@id="passwordNext"]').click()


def compose_mail(driver):
    compose_button = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[gh='cm']")))
    compose_button.click()

def add_recepient(driver,RECEIVER_MAIL):
    while True:
        if check_exists_by_xpath(driver,".//textarea[contains(@aria-label, 'To')]"):
            break
    to_field = driver.find_element_by_xpath(".//textarea[contains(@aria-label, 'To')]")
    to_field.click()
    to_field.send_keys(RECEIVER_MAIL+'\n')

def add_subject(driver, SUBJECT):
    subject_field = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.NAME, "subjectbox")))
    subject_field = WebDriverWait(driver, 500).until(EC.element_to_be_clickable((By.NAME, "subjectbox")))
    subject_field.click()
    subject_field.send_keys(SUBJECT)

def add_message(driver, MESSAGE):
    message_field = driver.find_element_by_xpath("(.//*[@aria-label='Message Body'])[2]")
    message_field.click()
    message_field.send_keys(MESSAGE)
    

def attach_file(driver, FILEPATH, FILENAME):
    driver.find_element_by_xpath('//input[@type="file"]').send_keys(FILEPATH)
    alabel = 'Uploading attachment: '+ FILENAME + '. Press delete to cancel'
    #alabel = 'Attachment: '+ FILENAME +'. Press enter to view the attachment and delete to remove it'
    #wait_for_upload = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.XPATH, "//div[ contains(@aria-label,'"+alabel+"')]")))
    while True:
        if not check_exists_by_xpath(driver,"//div[ contains(@aria-label,'"+alabel+"')]"):
            break
            
def send_mail(driver):
    driver.find_element_by_xpath("(//div[@class='T-I J-J5-Ji aoO v7 T-I-atl L3'])").click()

def log_out(driver):
    dropdown = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.XPATH,"//span[@class = 'gb_Ia gbii']")))
    subject_field = WebDriverWait(driver, 500).until(EC.element_to_be_clickable((By.XPATH, "//span[@class = 'gb_Ia gbii']")))
    dropdown.click()
    Logout = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.ID,"gb_71")))
    Logout.click()

