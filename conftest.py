from _pytest.config import hookimpl
from pytest import fixture
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
from selenium.webdriver.edge.webdriver import WebDriver as Edge
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from POM.loginpage import LoginPage
from POM.homepage import HomePage
from POM.create_lead import CreateLead
from POM.create_campaign import CreateCampaign
from POM.edit_lead import EditLead
from POM.create_organization import CreateOrg


def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default='chrome', dest='browser')
    parser.addoption("--env", action='store', default='Test', dest='env')
    parser.addoption("--headless", action='store_true', dest='headless', default=False)


@fixture
def _config(request):
    class TestConfigurations:
        url = "http://49.249.28.218:8888/"
        email = "admin"
        password = "admin"

    class StageConfigurations:
        url = "http://49.249.28.218:8888/"
        email = "admin"
        password = "admin"

    exe_env = request.config.option.env

    if exe_env.upper() == "TEST":
        print("Execution environment is TEST")
        return TestConfigurations()
    elif exe_env.upper() == "STAGE":
        print("Execution environment is STAGE")
        return StageConfigurations()
    else:
        raise Exception("Invalid execution environment")


@fixture
def driver(request,_config):
    browser_name = request.config.option.browser
    is_headless = request.config.option.headless
    options = None

    print("executing setup")
    if browser_name.upper() == "CHROME":
        if is_headless:
            options = ChromeOptions()
            options.add_argument("--headless=new")
        _driver = Chrome(options=options)
    elif browser_name.upper() == "FIREFOX":
        if is_headless:
            options = FirefoxOptions()
            options.add_argument("--headless")
        _driver = Firefox(options=options)
    elif browser_name.upper() == "EDGE":
        if is_headless:
            options = EdgeOptions()
            options.add_argument("--headless=new")
        _driver = Edge(options=options)
    else:
        raise Exception("Invalid browser")
    _driver.get(_config.url)
    _driver.maximize_window()
    yield _driver
    print("executing tear down")
    _driver.quit()

# The driver fixture uses a generator function because of the yield keyword.
# Before yield: Setup phase where the browser is launched, the WebDriver is initialized, and the page is opened.
# After yield: Teardown phase where the browser is closed and cleaned up.
# The yield allows the fixture to pause and return a value (in this case, the WebDriver) for the test function to use,
# and then resume execution after the test is finished for cleanup.

@fixture
def pages(driver):
    class Pages:
        loginpage = LoginPage(driver)
        homepage = HomePage(driver)
        createcampaign = CreateCampaign(driver)
        createlead = CreateLead(driver)
        createorg = CreateOrg(driver)
    return Pages()

def _capture_screenshot(driver):
    return driver.get_screenshot_as_base64()

@hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report,"extra",[])
    if report.when == "call":
        xfail = hasattr(report,"wasfail")
        # if report: #attaches screenshots for all steps
        if (report.skipped and report.fail) or (report.failed and not xfail):
            extra.append(pytest_html.extras.image(_capture_screenshot()))
        report.extra = extra