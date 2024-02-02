import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pages.login_page import LoginPage

def pytest_addoption(parser):
    parser.addoption("--browser_name",action= "store",default="chrome")

@pytest.fixture(scope="class")
def setUp(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":  # add --browser_name firefox in command to run on Firefox browser
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == "edge":  # add --browser_name edge in command to run on Edge browser
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://app-qa.mystoriesmatter.com/")
    driver.maximize_window()
    time.sleep(2)
    lp = LoginPage(driver)
    time.sleep(2)
    lp.login("ravi701@mailinator.com", "Rr@778998445665")
    time.sleep(5)
    if request.cls is not None:
        request.cls.driver = driver
    yield
    driver.close()