from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def wait_for_element_clickable(driver,element):
    try:
        wait = WebDriverWait(driver,30)
        wait.until(expected_conditions.element_to_be_clickable(element))
    except Exception as e:
        print(e)

def wait_for_element_visibility(driver,element):
    try:
        wait = WebDriverWait(driver,30)
        wait.until(expected_conditions.visibility_of(element))
    except Exception as e:
        print(e)

def wait_for_title(driver,title):
    try:
        wait = WebDriverWait(driver,30)
        wait.until(expected_conditions.title_contains(title))
    except Exception as e:
        print(e)

def wait_for_alert_popup(driver,element):
    try:
        wait = WebDriverWait(driver,30)
        wait.until(expected_conditions.alert_is_present(element))
    except Exception as e:
        print(e)


