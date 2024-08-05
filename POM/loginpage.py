from utilities.lib import Selenium_wrapper
from utilities.libExcel import attach_elements

@attach_elements('loginpage')
class LoginPage:

    def __init__(self,driver):
        self.driver = driver
        self.wrapper = Selenium_wrapper(self.driver)

    def login(self,username,password):
        self.wrapper.enter_text(self.txt_username,value=username)
        self.wrapper.enter_text(self.txt_password,value=password)
        self.wrapper.click_element(self.btn_login)
