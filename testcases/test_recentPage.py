import time
import pytest

from pages.recent_page import RecentPage
from utilities.BaseClass import BaseClass


class TestRecentPage(BaseClass):
    @pytest.fixture(autouse=True)
    def classMethod(self):
        self.rp = RecentPage(self.driver)

    def test_verify_recent(self):
        time.sleep(10)
        result = self.rp.verify_recent_page()
        assert result == True

    # def test_memories_on_recent_page(self):
    #     result = self.rp.verify_memory_on_recent_page()
    #     assert result == True

    def test_edit_memory(self,):
        self.rp.recentPage()
        result = self.test_verify_recent_page()
        assert result == True
        time.sleep(5)