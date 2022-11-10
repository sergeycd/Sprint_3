import pytest

from selenium import webdriver


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


# def pytest_addoption(parser):
#     parser.addoption('--browser_name', action='store', default="chrome",
#                      help="Choose browser: chrome or firefox")
#
# @pytest.fixture(scope="function")
# def driver(request):
#     browser_name = request.config.getoption("browser_name")
#     browser = None
#
#     if browser_name == "chrome":
#         browser = webdriver.Chrome()
#     elif browser_name == "firefox":
#         browser = webdriver.Firefox()
#     else:
#         raise pytest.UsageError("--browser_name should be chrome or firefox")
#     browser.maximize_window()
#
#     yield browser
#
#     browser.quit()
