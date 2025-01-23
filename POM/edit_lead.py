from utilities.lib import Selenium_wrapper
from utilities.libExcel import attach_elements
from POM.create_lead import CreateLead

@attach_elements('createlead')
@attach_elements('editlead')
class EditLead(CreateLead):
    def __init__(self,driver):
        self.driver = driver
        self.wrapper = Selenium_wrapper(self.driver)
        super().__init__(driver)

    def create_lead(self,firstname,lastname,company,assignedto):
        super().create_lead(firstname,lastname,company,assignedto)

    def editlead(self,firstname,lastname,company,assignedto,title):
        pass