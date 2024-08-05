from pytest import fixture
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
from POM.loginpage import LoginPage
from POM.homepage import HomePage
from POM.create_campaign import CreateCampaign
from POM.create_lead import CreateLead
from POM.create_organization import CreateOrg

@fixture
def driver():
    _driver = Firefox()
    _driver.get("http://49.249.28.218:8888/")
    yield _driver
    _driver.quit()

@fixture
def pages(driver):
    class Pages:
        loginpage = LoginPage(driver)
        homepage = HomePage(driver)
        createcampaign = CreateCampaign(driver)
        createlead = CreateLead(driver)
        createorg = CreateOrg(driver)
    return Pages()
