import time

from pages.NewMemory import New

from base.Selenium_Driver import SeleniumDriver
import utilities.custom_logger as cl


class PromptPage(SeleniumDriver):
    log = cl.getLogger()

    def __int__(self, driver):
        super().__init__(driver)
        self.driver = driver  # to initiate the driver, the argument driver will get from
        # the actual test case, at that time the constructor will
        # get the driver and initiate the internal driver

    #locator
    navBar = "body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > h3:nth-child(1) > div:nth-child(1) > button:nth-child(1)"
    promptCTA = ".Navbar__NavItem-sc-bpaubx-9.fszrsq"
    prompts = "PromptCard__PromptCardWrapper-sc-ugk9r0-1 iDMtuk"
    secondPrompt = "body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(2) > div:nth-child(2) > span:nth-child(1)"
    title = "#memory-title"
    editor = "//div[@class='ProseMirror']"
    publish = ".styled__StyledButton-sc-1edb4g-3.berOvv.styled__StyledButton-sc-16mjhso-6.fpIBar"
    dateField = "input[placeholder='mm/dd/yyyy']"


    def clickNavBar(self):
        self.waitforElement(self.navBar,"css")
        if self.isElementPresent(self.navBar,"css") == True:
            self.clickElement(self.navBar,"css")
        else:
            pass

    def click_prompt(self):
        self.waitforElement(self.promptCTA, "css")
        if self.isElementPresent(self.promptCTA,"css") == True:
            self.clickElement(self.promptCTA,"css")
        else:
            pass

    def clickOnPrompt(self):
        self.waitforElement(self.secondPrompt, "css")
        if self.isElementPresent(self.secondPrompt, "css") == True:
            self.clickElement(self.secondPrompt, "css")
        else:
            pass

    def enter_title(self, title):
        self.waitforElement(self.title, "css")
        self.sendKeys(title, self.title, "css")

    def enter_description(self, description):
        self.sendKeys(description, self.editor, "xpath")

    def publish_memory(self):
        self.clickElement(self.publish, "css")

    def enter_date(self, date):
        self.waitforElement(self.dateField, "css")
        self.sendKeys(date, self.dateField, "css")

    def verify_prompt_memory_publish(self):
        self.aa = New(self.driver)
        self.aa.verify_memory_publish()

    def prompt_memory(self,title,date,description):
        self.clickNavBar()
        self.click_prompt()
        time.sleep(5)
        self.clickOnPrompt()
        self.enter_title(title)
        self.enter_date(date)
        self.enter_description(description)
        self.publish_memory()
        time.sleep(5)