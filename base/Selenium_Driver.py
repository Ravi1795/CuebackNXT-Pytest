from selenium.common import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utilities.custom_logger as cl

class SeleniumDriver():
    log = cl.getLogger()
    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "id":
            return By.ID
        elif locatorType == "tag":
            return By.TAG_NAME
        else:
            print("Locator type is not supported")
        return False

    def findElement(self, locator, locatorType):
        element = None
        try:
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info('Element found with: ' + locator + 'and locatorType: ' + locatorType)
        except:
            self.log.info("Element not found")
        return element

    def clickElement(self, locator, locatorType):
        try:
            element = self.findElement(locator, locatorType)
            element.click()
            self.log.info("Click on element with: " + locator + 'and locatorType: ' + locatorType)
        except:
            print("Cannot click on element with: " + locator + 'and locatorType: ' + locatorType)

    def sendKeys(self, data, locator, locatorType):
        try:
            element = self.findElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with: " + locator + 'and locatorType: ' + locatorType)
        except:
            self.log.info("Cannot send data on element with: " + locator + 'and locatorType: ' + locatorType)
        return element

    def isElementPresent(self, locator, locatorType=""):
        try:
            element = self.findElement(locator, locatorType)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitforElement(self, locator, locatorType, timeout=10, pollfrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollfrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
        return element

    def findElements(self, locator, getByType):
        element = None
        try:
            element = self.driver.find_elements(getByType, locator)
            self.log.info('Element found with: ' + locator + 'and locatorType: ' + getByType)
        except:
            self.log.info("Element not found")
        return element
