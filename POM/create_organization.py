# createorg-->sheetname
from utilities.lib import Selenium_wrapper
from utilities.libExcel import attach_elements

@attach_elements("createorg")
class CreateOrg:

    def __init__(self,driver):
        self.driver = driver
        self.wrapper = Selenium_wrapper(self.driver)

    def create_org(self,orgname,assignedto):
        self.wrapper.click_element(self.icon_createorg)
        self.wrapper.enter_text(self.txt_orgname,value=orgname)
        if assignedto=='user':
            self.wrapper.click_element(self.rdo_user)
        elif assignedto=='group':
            self.wrapper.click_element(self.rdo_group)
        self.wrapper.click_element(self.btn_save)