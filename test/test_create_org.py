from pytest import mark
from utilities.libExcel import read_headers,read_data

headers = read_headers("smoke","test_login")
data = read_data("smoke","test_login")

_headers = read_headers("smoke","test_createorg")
_data = read_data("smoke","test_createorg")


@mark.parametrize(headers,data)
@mark.parametrize(_headers,_data)
def test_createorg(driver,pages,username,password,orgname,assignedto):
    pages.loginpage.login(username,password)
    pages.homepage.click_organization()
    pages.createorg.create_org(orgname,assignedto)