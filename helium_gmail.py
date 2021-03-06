from helium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EMAIL = "YOUR_EMAIL@gmail.com"
PASSWORD = "YOUR_PASSWORD"
RECEIVER_EMAIL = "RECEIVER_EMAIL@gmail.com"
SUBJECT = "WEB AUTOMATION"
MESSAGE = "This is an auto-generated mail"
FILEPATH = r"C:\Users\lakshya\Desktop\myEnvs\autopy\PythonImage.gif"
FILENAME = "PythonImage.gif"
IMAGE_EXTNS = ['png','jpg','gif']

driver = start_chrome('gmail.com')
write(EMAIL + '\n', into="Email or phone") 
wait_until(TextField('Enter your password').exists,timeout_secs = 500)
write(PASSWORD + '\n', into="Enter your password")
wait_until(Button('Compose').exists,timeout_secs = 500)
click(Button('Compose'))

to_field = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.XPATH, ".//textarea[contains(@aria-label, 'To')]")))
to_field.click()
to_field.send_keys(RECEIVER_EMAIL+'\n')
write(SUBJECT, into = 'Subject')
click(TextField('Subject').top_left + (0,50))
write(MESSAGE, into = '')
drag_file(FILEPATH, to="Drop files here")

#alabel = 'Attachment: '+ FILENAME +'. Press enter to view the attachment and delete to remove it'
if(FILENAME[-3:] in IMAGE_EXTNS):
    wait_for_upload = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.XPATH, '//img[@alt="'+FILENAME+'"]')))
else:
    alabel = 'Attachment: '+ FILENAME +'. Press enter to view the attachment and delete to remove it'
    wait_for_upload = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.XPATH, "//div[ contains(@aria-label,'"+alabel+"')]")))

click('Send')

#go_to('https://mail.google.com/mail/?logout')  
