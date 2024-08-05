from utilities.lib import Selenium_wrapper
from utilities.libExcel import attach_elements


@attach_elements("createcampaign")
class CreateCampaign:
    def __init__(self,driver):
        self.driver = driver
        self.wrapper = Selenium_wrapper(self.driver)

    def create_campaign(self,campaignname,assignedto,expclosedate):
        self.wrapper.click_element(self.lnk_createCampaign)
        self.wrapper.enter_text(self.txt_campaignname,value=campaignname)
        if assignedto.lower()=='user':
            self.wrapper.click_element(self.rdo_user)
        elif assignedto.lower()=='group':
            self.wrapper.click_element(self.rdo_group)
        self.wrapper.enter_text(self.txt_expclosedata,value=expclosedate)
        self.wrapper.click_element(self.btn_save)