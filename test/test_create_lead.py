from pytest import mark
from utilities.libExcel import read_headers,read_data
from time import sleep
headers = read_headers("smoke","test_login")
data = read_data("smoke","test_login")

# @mark.parametrize(headers,data)
# def test_login(driver,pages,username,password):
#     pages.loginpage.login(username,password)

_headers = read_headers("smoke","test_createlead")
_data = read_data("smoke","test_createlead")


@mark.parametrize(headers,data)
@mark.parametrize(_headers,_data)
def test_create_lead(driver,pages,firstname,lastname,company,assignedto,username, password):
    pages.loginpage.login(username, password)
    pages.homepage.click_lead()
    pages.createlead.create_lead(firstname,lastname,company,assignedto)
    sleep(3)