import time

from base.Selenium_Driver import SeleniumDriver



class RecentPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    recent = ".typography__Title3-sc-1rnknoa-3.eKjfJP"
    FirsrMemory = "body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)"
    ThreeDots = "body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)"
    EditMemory = ".styled__ContextMenuWrapper-sc-yfmyxx-6.dNMwYL"
    MemoryTitle = "//input[@id='memory-title']"
    MemoryEditor = ".ProseMirror"
    CTAPublish = "button[class='styled__StyledButton-sc-1edb4g-3 berOvv styled__StyledButton-sc-16mjhso-6 fpIBar'] span[class='typography__Label-sc-1rnknoa-12 fRdMgI']"
    MemoryDetailPage = ".styled__StyledButton-sc-1edb4g-3.gVNTJd.styled__EditButton-sc-gj12hh-4.eYmbHn"
    BackButton = ".styled__StyledButton-sc-1edb4g-3.glReAC"


    def verify_recent_page(self):
        self.waitforElement(self.recent,"css")
        result = self.isElementPresent(self.recent, "css")
        return result

    def verify_memory_on_recent_page(self):
        result = self.isElementPresent(self.FirsrMemory, "css")
        return result

    def click_edit_memory(self):
        self.clickElement(self.ThreeDots, "css")
        self.clickElement(self.EditMemory,"css")

    def memory_title_text(self):
        self.waitforElement(self.MemoryTitle,"xpath")
        self.clickElement(self.MemoryTitle,"xpath")
        self.sendKeys(" text added to title during automation",self.MemoryTitle,"xpath")

    def memory_edit(self):
        self.waitforElement(self.MemoryEditor,"css")
        self.sendKeys("\nNew Text during automation", self.MemoryEditor, "css")

    def clickPublishMemory(self):
        self.waitforElement(self.CTAPublish,"css")
        self.clickElement(self.CTAPublish,"css")


    def clickBackButton(self):
        self.waitforElement(self.BackButton,"css")
        self.clickElement(self.BackButton,"css")

    def recentPage(self):
        time.sleep(2)
        self.click_edit_memory()
        self.memory_title_text()
        self.memory_edit()
        self.clickPublishMemory()
        time.sleep(5)
        self.clickBackButton()
