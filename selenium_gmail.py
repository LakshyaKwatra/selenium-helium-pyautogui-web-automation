import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as pg
from email import encoders

username = "YOUR EMAIL@gmail.com"
password = "YOUR_PASSWORD"

driver= webdriver.Chrome()
#driver= webdriver.Chrome("E:\QA\Resource\WEBDRIVER\chromedriverserver\chromedriver.exe")
driver.get("https://stackoverflow.com/users/login")
time.sleep(3)
signin_google=driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]')
signin_google.click()
driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
time.sleep(6)

field = driver.find_element_by_xpath('//input[@type="password"]')
field.send_keys(password)
driver.find_element_by_xpath('//*[@id="passwordNext"]').click()

driver.execute_script("window.open('');")
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
# Switch to the new window
driver.switch_to.window(driver.window_handles[1])
driver.get('https://gmail.com')
time.sleep(2)

driver.find_element_by_css_selector("[gh='cm']").click()
element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, ".//textarea[contains(@aria-label, 'To')]")))
element.click()
element.send_keys("RECEIVER_MAIL@gmail.com")

driver.find_element_by_xpath("(.//*[@aria-label='Message Body'])[2]").click()
driver.find_element_by_xpath("(.//*[@aria-label='Message Body'])[2]").send_keys("This is an auto-generated mail")
driver.find_element_by_xpath("//div[contains(@aria-label,'Attach files')]").click();
time.sleep(6)
pg.typewrite(r"C:\Users\lakshya\Desktop\myEnvs\autopy\PythonImage.png")            #PATH TO THE FILE TO BE SENT AS AN ATTACHMENT
pg.typewrite('\n')
time.sleep(15)
driver.find_element_by_xpath("(.//*[@aria-label='Message Body'])[2]").send_keys(Keys.CONTROL + Keys.ENTER)














#driver.find_element_by_css_selector("[gh='cm']").click()
#time.sleep(6)
##pg.typewrite(f"angelkwatra123@gmail.com\n")
#time.sleep(6)
#driver.find_element_by_xpath("//div[contains(@aria-label,'Attach files')]").click();
#time.sleep(6)
#pg.typewrite(r"C:\Users\lakshya\Desktop\myEnvs\autopy\PythonImage.png")
#pg.typewrite('\n')

#element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "myXpath")))



# You can use (Keys.CONTROL + 't') on other OSs
#driver.findElement(By.name("subjectbox")).click();
#driver.findElement(By.name("subjectbox")).sendKeys("efgh");


#driver.switch_to_frame('canvas_frame')
# Load a page

# Make the tests...

# close the tab
# (Keys.CONTROL + 'w') on other OSs.
#driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')


#driver.close()

#driver.get("https://mail.google.com/mail/")


# emailid=driver.find_element_by_id("Email")
# emailid.send_keys("username")
#
#
# passw=driver.find_element_by_id("Passwd")
# passw.send_keys("password")
#
#
# signin=driver.find_element_by_id("signIn")
# signin.click()
#
#
# time.sleep(10)
#
#
# driver.switch_to_frame('canvas_frame')
#
#
# sentmail= driver.find_element_by_link_text('Sent Mail')
# sentmail.click()
#
#
# time.sleep(10)
#
#
# sentmail= driver.find_element_by_link_text('Your Name')
# sentmail.click()
#
#
# lout= driver.find_element_by_link_text('Sign out')
# lout.click()


# from selenium import webdriver
# from time import sleep
#
# class Google:
#
#  def __init__(self,username,password):
#   self.driver=webdriver.Chrome()
#   self.driver.get('https://stackoverflow.com/users/signu...)
#   sleep(3)
#   self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
#   self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
#   self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
#   sleep(3)
#   self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
#   self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
#   sleep(2)
#   self.driver.get('https://youtube.com')
#   sleep(5)
#
# passw=open('New Text Document (2).txt',"r",encoding="utf-8")
# password=str(passw.read())
# user=open('New Text Document (3).txt',"r",encoding="utf-8")
# username=str(user.read())
# mylike= Google(username,password)
