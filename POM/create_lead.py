from utilities.lib import Selenium_wrapper
from utilities.libExcel import attach_elements

@attach_elements("createlead")
class CreateLead:

    def __init__(self,driver):
        self.driver = driver;
        self.wrapper = Selenium_wrapper(self.driver)

    def create_lead(self,firstname,lastname,company,assignedto):
        self.wrapper.click_element(self.icon_createlead)
        self.wrapper.enter_text(self.txt_firstname,value=firstname)
        self.wrapper.enter_text(self.txt_lastname,value=lastname)
        self.wrapper.enter_text(self.txt_company,value=company)
        if assignedto=='user':
            self.wrapper.click_element(self.rdo_user)
        elif assignedto=='group':
            self.wrapper.click_element(self.rdo_group)
        self.wrapper.click_element(self.btn_save)

