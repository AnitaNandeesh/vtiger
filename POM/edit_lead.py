from utilities.lib import Selenium_wrapper
from utilities.libExcel import attach_elements

class EditLead:
    def __init__(self,driver):
        self.driver = driver
        self.wrapper = Selenium_wrapper(self.driver)

    def editlead(self):
        pass