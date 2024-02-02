import time

from base.Selenium_Driver import SeleniumDriver
import utilities.custom_logger as cl


class New(SeleniumDriver):
    log = cl.getLogger()

    def __int__(self, driver):
        super().__init__(driver)
        self.driver = driver  # to initiate the driver, the argument driver will get from
        # the actual test case, at that time the constructor will
        # get the driver and initiate the internal driver

    # locators
    navBar = ".Navbar__NavProfileItem-sc-bpaubx-6.jmTvbu.ph-no-capture"
    newMemoryButton = ".styled__StyledButton-sc-1edb4g-3.berOvv.Navbar__AddMemoryButton-sc-bpaubx-9.boPqwh"
    title = "#memory-title"
    editor = "//div[@class='ProseMirror']"
    publish = ".styled__StyledButton-sc-1edb4g-3.berOvv.styled__StyledButton-sc-16mjhso-6.fpIBar"
    dateField = "input[placeholder='mm/dd/yyyy']"
    withoutTitleToast = ".styled__ToastBody-sc-f5j15e-0.bxzuVv"
    calendar = "typography__Body-sc-1rnknoa-5 styled__DateBox-sc-16mjhso-12 fOXgTn bQWMZG ph-no-capture"
    futureDateToast = ".styled__ToastBody-sc-f5j15e-0.bxzuVv"
    invalidDateToast = ".styled__ToastBody-sc-f5j15e-0.bxzuVv"
    memoryPublishValidation = ".typography__LargeTitle-sc-1rnknoa-0.gRJGfv.ph-no-capture"
    backbutton = ".styled__StyledButton-sc-1edb4g-3.glReAC"


    def click_nav_bar(self):
        self.waitforElement(self.navBar, "css")
        if self.isElementPresent(self.navBar,"css") == True:
            self.clickElement(self.navBar, "css")
        else:
            pass

    def click_new_memory(self):
        self.waitforElement(self.newMemoryButton, "css")
        if self.isElementPresent(self.newMemoryButton,"css") == True:
            self.clickElement(self.newMemoryButton, "css")
        else:
            pass

    def enter_title(self, title):
        self.waitforElement(self.title, "css")
        self.sendKeys(title, self.title, "css")

    def enter_description(self, description):
        self.sendKeys(description, self.editor, "xpath")

    def publish_memory(self):
        self.clickElement(self.publish, "css")

    def click_back_button(self):
        self.waitforElement(self.backbutton,"css")
        self.clickElement(self.backbutton,"css")

    def set_date(self, date):
        self.waitforElement(self.dateField, "css")
        self.sendKeys(date, self.dateField, "css")

    def verify_memory_without_title(self):
        self.waitforElement(self.withoutTitleToast, "css")
        result = self.isElementPresent(self.withoutTitleToast, "css")
        print(result)
        return result

    def verify_invalid_date(self):
        self.waitforElement(self.invalidDateToast, "css")
        result = self.isElementPresent(self.invalidDateToast, "css")
        return result

    def verify_future_date(self):
        self.waitforElement(self.futureDateToast, "css")
        result = self.isElementPresent(self.futureDateToast, "css")
        return result

    def verify_newCTA(self):
        self.waitforElement(self.newMemoryButton, "css")
        valid = self.isElementPresent(self.newMemoryButton, "css")
        return valid

    def verify_memory_publish(self):
        self.waitforElement(self.memoryPublishValidation,"css")
        result = self.isElementPresent(self.memoryPublishValidation,"css")
        return result

    def pageRefresh(self):
        refresh = self.driver.refresh()
        return refresh

    def create_memory(self, title, date, description):
        self.click_nav_bar()
        self.click_new_memory()
        time.sleep(2)
        self.pageRefresh()
        self.enter_title(title)
        self.set_date(date)
        self.enter_description(description)
        self.publish_memory()
        time.sleep(5)
