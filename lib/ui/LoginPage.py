from lib.utils import timeouthandlers

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def waitforloginpagetoload(self):
        timeouthandlers.wait_for_title(self.driver,'Online Shopping Site')

    def getUsernameTextBox(self):
        try:
            return self.driver.find_element_by_xpath("//input[@class='_2IX_2- VJZDxU']")
        except:
            return None

    def getPasswordTextbox(self):
        try:
            return self.driver.find_element_by_xpath("//input[@class='_2IX_2- _3mctLh VJZDxU']")
        except:
            return None

    def getLoginBtn(self):
        try:
            return self.driver.find_element_by_xpath("//button[@class='_2KpZ6l _2HKlqd _3AWRsL']")
        except:
            return None

    def getLoginErrMsgTxt(self):
        try:
            return self.driver.find_element_by_xpath("//span[text()='Please enter valid Email ID/Mobile number']")
        except:
            return None

    def getCreateAccLink(self):
        try:
            return self.driver.find_element_by_xpath("//a[contains(text(),'Create an account')]")
        except:
            return None

    def getMobilNoTextbox(self):
        try:
            return self.driver.find_element_by_xpath("//input[@class='_2IX_2- VJZDxU']")
        except:
            return None

    def getContinueBtn(self):
        try:
            return self.driver.find_element_by_xpath("//button[@class='_2KpZ6l _2HKlqd _3AWRsL']")
        except:
            return None

















