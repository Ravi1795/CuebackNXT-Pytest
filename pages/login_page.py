import logging
import time

from selenium.webdriver.common.by import By

from base.Selenium_Driver import SeleniumDriver
import utilities.custom_logger as cl


class LoginPage(SeleniumDriver):
    log = cl.getLogger()

    def __int__(self, driver):
        super().__init__(driver)
        self.driver = driver  # to initiate the driver, the argument driver will get from
        # the actual test case, at that time the constructor will
        # get the driver and initiate the internal driver

    # locators
    loginButton ="div[class='pages__NavbarItems-sc-owc2ql-11 gOTwVJ'] a[class='styled__StyledLink-sc-1edb4g-1 jOCxTJ'] span[class='typography__Subhead-sc-1rnknoa-9 styled__ButtonItemsWrapper-sc-1edb4g-0 lelRsi cBtMLB']"
    email = "//input[@placeholder='Enter your email...']"
    passWord = "password"
    loginCTA = "//button[@type='submit']"
    logoutCTA = "//p[normalize-space()='Logout']"

    def clickLoginCTA(self):
        return self.clickElement(self.loginButton,"css")


    def enter_email(self, username):
        self.sendKeys(username,self.email,"xpath")

    def enter_password(self, password):
        self.sendKeys(password, self.passWord, "name")

    def loginClick(self):
        self.clickElement(self.loginCTA, "xpath")

    def verify_test_login_without_email(self):
        result = self.isElementPresent('//span[contains(text(),"Oops! Don\'t forget to enter your email.")]', "xpath")
        return result

    def verify_test_login_without_password(self):
        result = self.isElementPresent("//span[contains(text(),'Enter your password to let the journaling commence')]",
                                       "xpath")
        return result

    def verify_invalid_username(self):
        result = self.isElementPresent("//span[contains(text(),'Incorrect username or password.')]", "xpath")
        return result

    def pageRefresh(self):
        refresh = self.driver.refresh()
        return refresh

    def logout(self):
        self.clickElement(self.logoutCTA,"xpath")

    def login(self, username="", password=""):
        self.clickLoginCTA()
        time.sleep(2)
        self.pageRefresh()
        # self.clearFields()
        self.enter_email(username)
        self.enter_password(password)
        self.loginClick()
