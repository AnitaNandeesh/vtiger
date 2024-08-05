from pytest import mark
from utilities.libExcel import read_headers,read_data

headers = read_headers("smoke","test_login")
data = read_data("smoke","test_login")

_headers = read_headers("smoke","test_createcampaign")
_data = read_data("smoke","test_createcampaign")

@mark.parametrize(headers,data)
@mark.parametrize(_headers,_data)
def test_create_campaign(driver,pages,campaignname,assignedto,expclosedate,username, password):
    pages.loginpage.login(username, password)
    pages.homepage.hover_more()
    pages.homepage.click_campaign()
    pages.createcampaign.create_campaign(campaignname,assignedto,expclosedate)