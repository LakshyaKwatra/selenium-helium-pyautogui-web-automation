from selenium_funx import *

DOWNLOAD_URL = r'https://www.unleashed-technologies.com/sites/default/files/blog/image_url_drupal_blog_post_large.jpg'
PATH_TO_DOWNLOAD_DIRECTORY = r'C:\Users\lakshya\Desktop\myEnvs\autopy'
FILENAME = r"FILENAME"
FILE_EXTENSION = DOWNLOAD_URL[-3:]
FILE = FILENAME+ '.' +FILE_EXTENSION 
FILEPATH = PATH_TO_DOWNLOAD_DIRECTORY + f'\{FILE}'

BROWSERS = ['Chrome','IE','Firefox']
SELECTED_BROWSER = BROWSERS[1]

USERNAME = "YOUR_EMAIL@gmail.com"
PASSWORD = "YOUR_PASSWORD"
RECEIVER_MAIL = "RECEIVERS_MAIL@gmail.com"
SUBJECT = "WEB AUTOMATION"
MESSAGE = "This is an auto-generated mail"

download(DOWNLOAD_URL,FILEPATH)

if SELECTED_BROWSER == BROWSERS[0]:
    driver = webdriver.Chrome()
elif SELECTED_BROWSER == BROWSERS[1]:
    driver = webdriver.Ie()
else:
    driver = webdriver.Firefox()

gmail_login(driver,USERNAME,PASSWORD)
compose_mail(driver)
add_recepient(driver,RECEIVER_MAIL)
add_subject(driver, SUBJECT)
add_message(driver, MESSAGE)
attach_file(driver, FILEPATH, FILENAME)
send_mail(driver)
log_out(driver)
driver.close()


