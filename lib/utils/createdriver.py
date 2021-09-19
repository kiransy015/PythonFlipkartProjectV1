from selenium.webdriver import Chrome,Firefox,Ie
import pytest

def getbrowserinstance():
    # browserinfo = pytest.config.option.browser
    # urlinfo = pytest.config.option.url

    browserinfo = "chrome"
    urlinfo = "test"

    if browserinfo.lower()=="chrome":
        driver = Chrome("G:\\Kiran\\Python\\gitWorkspace\\Python-Frameworks\\PythonFlipkartProjectV1\\BrowserServers\\chromedriver.exe")
    elif browserinfo.lower()=="firefox":
        driver = Firefox(
            executable_path='G:\\Kiran\\Python\\gitWorkspace\\Python-Frameworks\\PythonFlipkartProjectV1\\Browser_Servers\\geckodriver.exe')
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





