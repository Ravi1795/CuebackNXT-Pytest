import time
from datetime import date

from base.Selenium_Driver import SeleniumDriver


class EditPage(SeleniumDriver):

    def __int__(self, driver):
        super.__init__(driver)
        self.driver = driver

    # locator
    navBar = "body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > h3:nth-child(1) > div:nth-child(1) > button:nth-child(1)"
    editCTA = "//p[normalize-space()='Edit']"
    pinCollection = "//span[normalize-space()='Pinned Collections']"
    allMemories = "body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)"
    publishMemories = "body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2)"
    draftMemories = "body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3)"
    recentlyDeleted = "body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4)"
    createCollectionCTA = ".typography__Headline-sc-1rnknoa-4.styled__CreateCollectiontext-sc-1oqy9zo-3.hvqsbY"
    collectionName = "//input[@class='styled__Input-sc-18y1sfc-9 FEwbq ph-no-capture']"
    dropDown = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/*[name()='svg'][1]"
    createCollection = "button[class='styled__StyledButton-sc-1edb4g-3 berOvv styled__StyledCTA-sc-18y1sfc-59 dWkXAv'] span[class='typography__Subhead-sc-1rnknoa-8 styled__ButtonItemsWrapper-sc-1edb4g-0 kEpsPS eUHyRI']"
    firstMemory = "body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > label:nth-child(3)"
    secondMemory = "body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > label:nth-child(3) > span:nth-child(2)"
    collectionValidation = "body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)"
    manageCollection = ".styled__StyledButton-sc-1edb4g-3.bgVKjU"
    threedots = ".styled__DotsContainer-sc-18y1sfc-60.ljPmkQ"
    deleteCollection = ".styled__DeleteMemoryWrapper-sc-1oqy9zo-25.fMjCs"
    deleteConfirm = "button[class='styled__StyledButton-sc-1edb4g-3 berOvv styled__StyledDeleteButton-sc-18y1sfc-70 ilItLH'] span[class='typography__Subhead-sc-1rnknoa-8 styled__ButtonItemsWrapper-sc-1edb4g-0 kEpsPS eUHyRI']"


    def clickNavBar(self):
        self.clickElement(self.navBar,"css")
    def clickEdit(self):
        self.clickElement(self.editCTA, "xpath")

    def verify_pinned_collection(self):
        self.waitforElement(self.pinCollection,"xpath")
        pin_collection = self.isElementPresent(self.pinCollection, "xpath")
        return pin_collection

    def verify_all_memories_collection(self):
        all_memories = self.isElementPresent(self.allMemories, "css")
        return all_memories

    def verify_publish_memories_collection(self):
        publish_memories = self.isElementPresent(self.publishMemories, "css")
        return publish_memories

    def verify_draft_memories_collection(self):
        draft_memories = self.isElementPresent(self.draftMemories, "css")
        return draft_memories

    def verify_recently_deleted_collection(self):
        recently_deleted = self.isElementPresent(self.recentlyDeleted, "css")
        return recently_deleted

    def create_collection(self):
        self.waitforElement(self.createCollectionCTA,"css")
        if self.isElementPresent(self.createCollectionCTA,"css") == True:
            self.clickElement(self.createCollectionCTA, "css")
        else:
            pass

    def collection_edit(self):
        self.clickElement(self.collectionValidation,"css")
        self.waitforElement(self.manageCollection,"css")
        self.clickElement(self.manageCollection,"css")
        self.waitforElement(self.threedots,"css")
        self.clickElement(self.threedots,"css")
        self.waitforElement(self.deleteCollection,"css")
        self.clickElement(self.deleteCollection,"css")
        self.waitforElement(self.deleteConfirm,"css")
        self.clickElement(self.deleteConfirm,"css")


    def collection_name(self,collection):
        self.waitforElement(self.collectionName,"xpath")
        time.sleep(3)
        ele = self.getElement(self.collectionName,"xpath")
        ele.clear()
        self.sendKeys(collection,self.collectionName,"xpath")
        self.waitforElement(self.firstMemory,"css")
        self.clickElement(self.firstMemory,"css")
        time.sleep(2)
        self.clickElement(self.secondMemory,"css")
        time.sleep(2)
        self.clickElement(self.createCollection,"css")

    def clickDropdown(self):
        self.clickElement(self.dropDown,"xpath")
        time.sleep(3)
        self.clickElement(self.dropDown,"xpath")

    def edit_test(self,collection):
        self.create_collection()
        self.collection_name(collection)
        time.sleep(5)

