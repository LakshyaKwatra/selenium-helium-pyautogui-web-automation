# selenium-pyautogui-web-automation

I am doing this project as a part of my internship at Samsung R&D Institute, Delhi. This project specifically aims at automating features like downloading files and sending emails with attachments without the use of smtplib.
Libraries and modules that I have used are: Selenium, Helium and pyautogui.

# File Description

selenium_funx.py: contains browser-independent functions created with selenium for web automation.

execute.py: This file uses the functions present in selenium funx.py for downloading a file and mailing it as an attachment.

download_and_mail.py: contains Helium implementation of downloading a file and mailing it as an attachment.

helium_gmail.py: contains Helium implementation of sending a pre-downloaded file as an attachment.

selenium_gmail.py: contains Selenium implementation of sending a pre-downloaded file as an attachment using pyautogui image recognition for dealing with external windows.

# Prerequisites

Browser webdriver needs to be installed for your browser. Download the 32-bit version:

For Chrome:	https://sites.google.com/a/chromium.org/chromedriver/downloads

For Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

For Firefox:	https://github.com/mozilla/geckodriver/releases

For Safari:	https://webkit.org/blog/6900/webdriver-support-in-safari-10/

Run the following commands in the command line:

> pip install selenium

> pip install pyautogui

> pip install helium
