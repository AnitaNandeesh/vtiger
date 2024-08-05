from utilities.lib import Selenium_wrapper
from utilities.libExcel import attach_elements
from selenium.webdriver.common.action_chains import ActionChains

@attach_elements("homepage")
class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wrapper = Selenium_wrapper(self.driver)

    def hover_more(self):
        actions = ActionChains(self.driver)
        more = self.driver.find_element(*(self.lnk_more))
        actions.move_to_element(more).perform()

    def click_campaign(self):
        self.wrapper.click_element(self.lnk_campaign)

    def click_lead(self):
        self.wrapper.click_element(self.lnk_leads)

    def click_organization(self):
        self.wrapper.click_element(self.lnk_organization)