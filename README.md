# selenium-pyautogui-web-automation
I am doing this project as a part of my internship at Samsung R&D Institute, Delhi. This project specifically aims at automating features like downloading files and sending emails with attachments without the use of smtplib.
Libraries and modules that I have used are: Selenium, Helium and pyautogui.
Python version used: 3.7.4

## File Description
selenium_funx.py: contains browser-independent functions created with selenium for web automation.

execute.py: This file uses the functions present in selenium funx.py for downloading a file and mailing it as an attachment.

download_and_mail.py: contains Helium implementation of downloading a file and mailing it as an attachment.

helium_gmail.py: contains Helium implementation of sending a pre-downloaded file as an attachment.

selenium_gmail.py: contains Selenium implementation of sending a pre-downloaded file as an attachment using pyautogui image recognition for dealing with external windows.

## Prerequisites
The following are the prerequisites and dependencies for running the code:

### Downloading Webdriver
Browser webdriver needs to be installed for your browser. Download the 32-bit version from the respective links and add the downloaded executable (.exe) file to your system's PATH:

For Chrome:	https://sites.google.com/a/chromium.org/chromedriver/downloads

For Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

For Firefox:	https://github.com/mozilla/geckodriver/releases

For Safari:	https://webkit.org/blog/6900/webdriver-support-in-safari-10/

For Internet Explorer: https://www.selenium.dev/downloads/

### Setting up Browser (Only for Internet Explorer):
1. Protected Mode settings should be same for all the zones:
   - Click on **Tools>Internet Options**.
   - Under Internet Options click on the **Security tab**.
   - In the **Select a zone to view area** click on the **Internet zone**.
   - In the **Security level for this zone** select the **Enable Protected Mode** checkbox. Do this for the remaining 3 zones viz. "Local intranet", "Trusted sites" and "Restricted sites".
   - After this, close the Internet Options and Restart Internet Explorer to get these changes reflected.
 
2. If your application is not starting or you are just getting one or multiple InternetExplorerDriver Listening on port window mesages
than your IE browser's zoom level might be set to something other than 100%. To fix this:
   - Go to **View>Zoom** and select **100%**.

3. Enhanced Protected Mode is a security feature that was introduced in Windows 8. By default, this feature is turned off in Internet Explorer on the Windows 8.1 desktop. This setting must be disabled. To disable this setting follow below steps:
   - Click on **Tools>Internet Options** and switch to **Advanced** Tab.
   - Scroll down to the **Security** section.
   - Remove the selection from the checkbox **Enable Enhanced Protected Mode***.

4. Set a registry entry on the target computer so that the driver can maintain a connection to the instance of Internet Explorer it creates. *(Required for IE 11 Only)*
   - Open the Registry editor by running "regedit" in the Run program.
   - Navigate to: 
    - For 32-bit Windows installations,
      - HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\Main\FeatureControl 
    - For 64-bit Windows installations,
      - HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Internet Explorer\Main\FeatureControl
   - Create key, **FEATURE_BFCACHE**, if not already present.
   - Inside this key, create a DWORD value named **iexplore.exe** with the value of 0. Even if QWORD is suggested for 64-bit machines, create a DWORD.

### Libraries Installation
To install all the required libraries and modules, run this command in the command line:

> pip install -r requirements.txt

### Setting up sender's Gmail account
Disable 2 factor authentication and allow access to less secure apps.
   - On your Android phone or tablet, open **Gmail app** and go to **Manage your Google Account>Security**.
   - Under **Signing in to Google** section, turn off **2-Step Verification** if it's turned on.
   - Under **Less secure app access** section, tap turn on if it's turned off.

## Instructions to run
Run this in the command line:
> python execute.py
