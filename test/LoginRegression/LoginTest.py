import unittest

from _pytest import python
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from lib.utils import timeouthandlers,createdriver
from lib.ui.LoginPage import LoginPage
from lib.ui.HomePage import HomePage
from lib.ui.CartPage import CartPage
import json
import time

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = createdriver.getbrowserinstance()
        self.login = LoginPage(self.driver)
        self.home = HomePage(self.driver)
        self.cart = CartPage(self.driver)
        file = open(".\\test\\LoginRegression\\testdata\\testdata.json")
        self.testdata = json.load(file)

    def testInvalidFlipkartlogin(self):
        self.login.waitforloginpagetoload()
        assert self.driver.title.__contains__(self.testdata['title'])
        self.login.getUsernameTextBox().send_keys(self.testdata['Invalid']['username'])
        self.login.getPasswordTextbox().send_keys(self.testdata['Invalid']['password'])
        self.login.getLoginBtn().click()
        assert self.login.getLoginErrMsgTxt().text==self.testdata['LoginErrMsg']

    def testCreateNewAcc(self):
        self.login.waitforloginpagetoload()
        assert self.driver.title.__contains__(self.testdata['title'])
        self.login.getCreateAccLink().click()
        self.login.getMobilNoTextbox().send_keys('9721675389')
        self.login.getContinueBtn().click()
        time.sleep(30)

    def testValidFlipkartlogin(self):
        self.login.waitforloginpagetoload()
        assert self.driver.title.__contains__(self.testdata['title'])
        self.login.getUsernameTextBox().send_keys(self.testdata['Valid']['username'])
        self.login.getPasswordTextbox().send_keys(self.testdata['Valid']['password'])
        self.login.getLoginBtn().click()
        timeouthandlers.wait_for_element_visibility(self.driver, self.home.getSearchProductsTextBox())
        time.sleep(10)
        self.home.getSearchProductsTextBox().send_keys(self.testdata['search']['item1'])
        time.sleep(10)
        itemlist = self.home.getSearchItems()

        for item in itemlist:
            time.sleep(2)
            print(item.text)
            act = ActionChains(self.driver)
            act.move_to_element(item).perform()
            if item.text.lower()==self.testdata['search']['item1'].lower():
                try:
                    act.click(item).perform()
                    break
                except Exception as e:
                    self.home.getSearchIcon().click()
        time.sleep(10)

    def testMouseOperation(self):
        self.login.waitforloginpagetoload()
        assert self.driver.title.__contains__(self.testdata['title'])
        self.login.getUsernameTextBox().send_keys(self.testdata['Valid']['username'])
        self.login.getPasswordTextbox().send_keys(self.testdata['Valid']['password'])
        self.login.getLoginBtn().click()
        timeouthandlers.wait_for_element_visibility(self.driver, self.home.getSearchProductsTextBox())

        time.sleep(10)
        act = ActionChains(self.driver)
        act.move_to_element(self.home.getFashionLink()).perform()
        itemlist = self.home.getAllFasshionItems()

        for item in itemlist:
            time.sleep(5)
            try:
                if item.text==self.testdata['search']['item2']:
                    act.move_to_element(item).perform()
                    subitemlist = self.home.getAllFasshionItems()
                    for subitem in subitemlist:
                        if subitem.text==self.testdata['subsearch']['subitem1']:
                            act.click(subitem).perform()
                            break
            except Exception as e:
                print(e)

        time.sleep(5)



    def testSelectionOperation(self):
        self.login.waitforloginpagetoload()
        assert self.driver.title.__contains__(self.testdata['title'])
        self.login.getUsernameTextBox().send_keys(self.testdata['Valid']['username'])
        self.login.getPasswordTextbox().send_keys(self.testdata['Valid']['password'])
        self.login.getLoginBtn().click()
        timeouthandlers.wait_for_element_visibility(self.driver, self.home.getSearchProductsTextBox())

        time.sleep(10)
        self.home.getSearchProductsTextBox().send_keys(self.testdata['search']['item3'])
        self.home.getSearchIcon().click()
        sel = Select(self.home.getPriceSelect())
        sel.select_by_value('20000')
        timeouthandlers.wait_for_element_clickable(self.driver,self.home.get6GBRamCheckBox())
        time.sleep(5)
        self.home.get6GBRamCheckBox().click()
        timeouthandlers.wait_for_element_clickable(self.driver,self.home.getSamsungCheckbox())
        time.sleep(5)
        self.home.getSamsungCheckbox().click()
        timeouthandlers.wait_for_element_clickable(self.driver,self.home.getOSOption())
        time.sleep(5)
        self.home.getOSOption().click()
        timeouthandlers.wait_for_element_clickable(self.driver,self.home.getAndroidOSCheckbox())
        time.sleep(5)
        self.home.getAndroidOSCheckbox().click()
        time.sleep(5)
        filteredItems = self.home.getfilteredItems()

        for item in filteredItems:
            time.sleep(2)
            print(item.text)
            if item.text.__contains__(self.testdata['subsearch']['subitem2']):
                item.click()
                break

        windows = self.driver.window_handles
        parendtid = windows[0]
        childid = windows[1]

        self.driver.switch_to_window(childid)
        timeouthandlers.wait_for_element_clickable(self.driver,self.home.getAddToCart())
        time.sleep(5)
        self.home.getAddToCart().click()
        time.sleep(5)
        self.driver.close()

        self.driver.switch_to_window(parendtid)
        self.driver.refresh()

        timeouthandlers.wait_for_element_clickable(self.driver,self.home.getCartIcon())
        self.home.getCartIcon().click()
        time.sleep(5)
        timeouthandlers.wait_for_element_clickable(self.driver,self.cart.getRemoveLink())
        self.cart.getRemoveLink().click()
        timeouthandlers.wait_for_element_clickable(self.driver,self.cart.getRemoveBtn())
        self.cart.getRemoveBtn().click()
        timeouthandlers.wait_for_element_visibility(self.driver,self.cart.getItemRemoveSuccessMsg())
        assert self.cart.getItemRemoveSuccessMsg().is_displayed()
        time.sleep(5)


    def testHandlingFrame(self):
        self.driver.get("https://timesofindia.indiatimes.com/")
        time.sleep(5)
        self.driver.switch_to_frame('cardembed-data-tickertable-5-1-335-853-')
        self.driver.find_element_by_xpath("//div[text()='Cryptocurrency']").click()
        time.sleep(5)


    def testGetCSSValues(self):
        time.sleep(5)
        print('Color :',self.login.getLoginBtn().value_of_css_property(self.testdata['css']['color']))
        print('Font-Family :',self.login.getLoginBtn().value_of_css_property(self.testdata['css']['fontfamily']))


    def tearDown(self):
        self.driver.close()
