# from selenium.webdriver.firefox.webdriver import WebDriver
# from utilities.lib import Selenium_wrapper
# from utilities.excel_lib import locators
import allure

from POM.loginpage import LoginPage
from pytest import mark
from utilities.libExcel import read_headers,read_data

headers = read_headers("smoke","test_login")
data = read_data("smoke","test_login")


@mark.order(1)
# @mark.dependency(name='login')
# @mark.skip("test case working fine")
@mark.parametrize(headers,data)
def test_login(driver,pages,username,password):
    pages.loginpage.login(username,password)
