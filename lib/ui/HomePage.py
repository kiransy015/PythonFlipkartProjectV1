from lib.utils import createdriver,timeouthandlers

class HomePage:
    def __init__(self,driver):
        self.driver = driver

    def waitforhomepagetoload(self):
        timeouthandlers.wait_for_title(self.driver,'Online Shopping Site')

    def getSearchProductsTextBox(self):
        try:
            return self.driver.find_element_by_xpath("//input[contains(@placeholder,'Search for products')]")
        except:
            return None

    def getSearchItems(self):
        try:
            return self.driver.find_elements_by_xpath("//a[@class='_3izBDY']//div[contains(@class,'lrtEPN')]")
        except:
            return None

    def getSearchIcon(self):
        try:
            return self.driver.find_element_by_xpath("//button[@class='L0Z3Pu']")
        except:
            return None

    def getFashionLink(self):
        try:
            return self.driver.find_element_by_xpath("//div[@class='xtXmba' and contains(text(),'Fashion')]")
        except:
            return None

    def getAllFasshionItems(self):
        try:
            return self.driver.find_elements_by_xpath("//div[contains(@class,'_3pAV4E')]//a")
        except:
            return None

    def getPriceSelect(self):
        try:
            return self.driver.find_element_by_xpath("//select[@class='_2YxCDZ']")
        except:
            return None

    def get6GBRamCheckBox(self):
        try:
            return self.driver.find_element_by_xpath("//div[text()='6 GB & Above']/preceding-sibling::div[@class='_24_Dny']")
        except:
            return None

    def getSamsungCheckbox(self):
        try:
            return self.driver.find_element_by_xpath("//div[text()='SAMSUNG']/preceding-sibling::div[@class='_24_Dny']")
        except:
            return None

    def getOSOption(self):
        try:
            return self.driver.find_element_by_xpath("//div[@class='_2gmUFU _3V8rao' and text()='Operating System']")
        except:
            return None

    def getAndroidOSCheckbox(self):
        try:
            return self.driver.find_element_by_xpath("//div[text()='Android']/preceding-sibling::div[@class='_24_Dny']")
        except:
            return None

    def getfilteredItems(self):
        try:
            return self.driver.find_elements_by_xpath("//div[@class='_4rR01T']")
        except:
            return None

    def getAddToCart(self):
        try:
            return self.driver.find_element_by_xpath("//button[@class='_2KpZ6l _2U9uOA _3v1-ww']")
        except:
            return None

    def getCartIcon(self):
        try:
            return self.driver.find_element_by_xpath("//div[@class='KK-o3G']")
        except:
            return None



































