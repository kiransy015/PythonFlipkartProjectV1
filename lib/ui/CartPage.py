from lib.utils import timeouthandlers

class CartPage:
    def __init__(self,driver):
        self.driver = driver

    def waitforpageload(self):
        timeouthandlers.wait_for_element_visibility(self.driver.find_element_by_xpath("//div[contains(text(),'My Cart')]"))

    def getRemoveLink(self):
        try:
            return self.driver.find_element_by_xpath("//div[@class='_3dsJAO' and text()='Remove']")
        except:
            return None

    def getRemoveBtn(self):
        try:
            return self.driver.find_element_by_xpath("//div[@class='_3dsJAO _24d-qY FhkMJZ'and text()='Remove']")
        except:
            return None

    def getItemRemoveSuccessMsg(self):
        try:
            return self.driver.find_element_by_xpath("//div[contains(text(),'Successfully removed')]")
        except:
            return None







