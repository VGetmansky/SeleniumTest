import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--driver", action="store", default="firefox", help="Type in browser type")
    parser.addoption("--url", action="store", default="https://www.citilink.ru/catalog/smartfony/?f=discount.any%2Crating.any&pf=discount.any%2Crating.any&price_max=3500&pprice_max=2999", help="url")


@pytest.fixture(scope="module")
def driver(request):
    browser = request.config.getoption("--driver")
    if browser == 'firefox':

        firefoxoptions = webdriver.FirefoxProfile()
        browser = webdriver.Firefox(firefoxoptions)
        browser.get("about:blank")
        browser.implicitly_wait(10)
        browser.maximize_window()

        yield browser
        browser.quit()

    else:
        print('only firefox is supported at the moment')


@pytest.fixture(scope="module")
def url(request):
    return request.config.getoption("--url")
