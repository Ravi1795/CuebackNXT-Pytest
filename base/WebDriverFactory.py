from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class WebDriverFactory():

    def __int__(self,browser_name):
        self.browser_name = browser_name

    def getWebDriverFactory(self):
        if self.browser_name == "chrome":
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif self.browser_name == "firefox":  # add --browser_name firefox in command to run on Firefox browser
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif self.browser_name == "edge":  # add --browser_name edge in command to run on Edge browser
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.get("https://app-qa.mystoriesmatter.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver