from selenium.webdriver.firefox.webdriver import WebDriver
from xlrd import open_workbook
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
def _wait(func):
    def wrapper(instance,locator,**kwargs):
        wait = WebDriverWait(instance.driver,10)
        v = visibility_of_element_located(locator)
        wait.until(v)
        return func(instance,locator,**kwargs)
    return wrapper

def __wait(cls):
    for key,value in cls.__dict__.items():
        if callable(value) and key != '__init__':
            setattr(cls,key,_wait(value))
    return cls

@__wait
class Selenium_wrapper:

    def __init__(self,driver):
        self.driver = driver

    def click_element(self,locator:tuple[str,str]):
        self.driver.find_element(*locator).click()

    def enter_text(self,locator,value):
        self.driver.find_element(*locator).send_keys(value)

