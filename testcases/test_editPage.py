import time

import pytest
from pages.edit_page import EditPage
from utilities.BaseClass import BaseClass
from datetime import date
import utilities.custom_logger as cl

class TestEditPage(BaseClass):
    log = cl.getLogger()
    @pytest.fixture(autouse=True)
    def classMethod(self):
        self.ep = EditPage(self.driver)

    def test_verify_pin_memory(self):
        self.ep.clickNavBar()
        self.ep.clickEdit()
        time.sleep(3)
        ele = self.ep.verify_pinned_collection()
        assert ele == True

    def test_verify_all_memory(self):
        ele = self.ep.verify_all_memories_collection()
        assert ele == True

    def test_verify_publish_memory(self):
        ele = self.ep.verify_publish_memories_collection()
        assert ele == True

    def test_verify_recently_deleted(self):
        ele = self.ep.verify_recently_deleted_collection()
        assert ele == True

    def test_dropdown(self):
        self.ep.clickDropdown()

    def test_create_collection(self):
        self.ep.edit_test("New Collection created on " + str(date.today()))
        time.sleep(5)

    def test_manage_collection(self):
        self.ep.collection_edit()
        time.sleep(5)
