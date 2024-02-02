import time

from selenium.webdriver.common.by import By

from base.Selenium_Driver import SeleniumDriver
import secrets
import utilities.custom_logger as cl


class SignUpPage(SeleniumDriver):
    log = cl.getLogger()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver  # to initiate the driver, the argument driver will get from
        # the actual test case, at that time the constructor will
        # get the driver and initiate the internal driver

    # locators
    signupButton = "//span[normalize-space()='Sign up']"
    firstName = "firstName"
    lastName = "lastName"
    emailID = "//input[@placeholder='bill.shakespeare@example.com']"
    birthYear = "//input[@placeholder='1564']"
    NextCTA = "//span[normalize-space()='Next']"
    passwordCTA = "//input[@name='password']"
    confirmPassword = "//input[@name='confirmPassword']"
    signupCTA = "//span[normalize-space()='Sign up']"
    nextButton = ".styled__StyledButton-sc-1edb4g-3.bMUkje"

    def clickSignupCTA(self):
        self.clickElement(self.signupButton, "xpath")

    def enter_firstName(self, fname):
        ele = self.waitforElement(self.firstName, locatorType="name")
        ele.send_keys(fname)

    def enter_lastName(self, lname):
        ele = self.waitforElement(self.lastName, locatorType="name")
        ele.send_keys(lname)

    def enter_email(self, username):
        ele = self.waitforElement(self.emailID, locatorType="xpath")
        ele.send_keys(username)

    def enter_birthYear(self, year):
        ele = self.waitforElement(self.birthYear, locatorType="xpath")
        ele.send_keys(year)

    def NEXT(self):
        CTA = self.findElement(self.nextButton,"css")
        prop = CTA.is_enabled()
        print(prop)
        return prop

    def clickNextCTA(self):
        CTA = self.clickElement(self.NextCTA, "xpath")

    def enter_password(self, password):
        ele = self.waitforElement(self.passwordCTA, locatorType="xpath")
        ele.send_keys(password)

    def enter_confirm_password(self, confpassword):
        ele = self.waitforElement(self.confirmPassword, locatorType="xpath")
        ele.send_keys(confpassword)

    def clickSignUp(self):
        self.clickElement(self.signupCTA, locatorType="xpath")

    def verify_signup_without_first_name(self):
        result = self.isElementPresent('(//span[normalize-space()="Required. We don\'t want to call you '
                                       '\'Anonymous.\'"])[1]', "xpath")
        return result

    def verify_signup_without_last_name(self):
        result = self.isElementPresent("//span[normalize-space()='Required (goes well with your first name).']",
                                       "xpath")
        return result

    def verify_signup_without_email(self):
        result = self.isElementPresent("//span[normalize-space()='Required. Your journal awaits!']",
                                       "xpath")
        return result

    def verify_signup_with_invalid_email(self):
        result = self.isElementPresent('//span[normalize-space()="This doesn\'t look quite right. Try re-typing!"]',"xpath")
        return result

    def verify_signup_without_birthyear(self):
        result = self.isElementPresent("//span[normalize-space()='Why do we ask this?']",
                                       "xpath")
        return result

    def verify_birth_year(self):
        result = self.isElementPresent("//span[normalize-space()='Hmm, enter a valid birth year after 1920.']", "xpath")
        return result

    def verify_invalid_birthyear(self):
        result = self.isElementPresent("//span[normalize-space()='Hmm, enter a valid birth year']", "xpath")
        return result

    def verify_confirm_password(self):
        result = self.isElementPresent("//span[normalize-space()='Passwords do not match']", "xpath")
        return result

    def verify_valid_signup(self):
        result = self.isElementPresent('//span[normalize-space()="Let\'s verify your email"]',"xpath")
        return result

    def pageRefresh(self):
        refresh = self.driver.refresh()
        return refresh

    def email(self):
        self.log.info(f"Email Id registered: {secrets.token_hex(2)}@mailinator.com")
        return f"{secrets.token_hex(2)}@mailinator.com"           #Will generate random email address during signup
            #secrets.token_hex() ~ Return a random text string, in hexadecimal. The string has nbytes random bytes,
            #each byte converted to two hex digits.



    def signup(self, firstname="", lastname="", email ="", birthyear="", password="", confirmpassword=""):
        self.clickSignupCTA()
        time.sleep(2)
        self.pageRefresh()
        self.enter_firstName(firstname)
        self.enter_lastName(lastname)
        self.enter_email(email)
        self.enter_birthYear(birthyear)
        if self.NEXT() == True:
            time.sleep(2)
            self.clickNextCTA()
            self.enter_password(password)
            self.enter_confirm_password(confirmpassword)
            self.clickSignUp()
            time.sleep(3)
        else:
            pass
