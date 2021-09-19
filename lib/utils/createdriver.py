from selenium.webdriver import Chrome,Firefox,Ie
from selenium.webdriver.chrome.options import Options
import os
import pytest

def getbrowserinstance():
    # browserinfo = pytest.config.option.browser
    # urlinfo = pytest.config.option.url

    browserinfo = "chrome"
    urlinfo = "test"

    if browserinfo.lower()=="chrome":
        options = Options()
        options.binary_location = "C:/Users/DELL/AppData/Local/Google/Chrome/Application/chrome.exe"
        chromedriverpath = os.path
        print("./")

        driver = Chrome(options=options,
                                  executable_path=".\\Browser_Servers\\chromedriver.exe", )
    elif browserinfo.lower()=="firefox":
        driver = Firefox(
            executable_path='.\\Browser_Servers\\geckodriver.exe')
    else:
        print('Invalid browser info!!!')
        return None

    driver.maximize_window()
    driver.implicitly_wait(30)

    if urlinfo.lower()=="test":
        driver.get('https://www.flipkart.com/')
    elif urlinfo.lower()=="dev":
        driver.get('https://www.flipkart.com/')
    else:
        print("Invalid url info!!!")

    return driver





