import pytest
from pages.promptPage import PromptPage
from utilities.BaseClass import BaseClass
from datetime import date
import utilities.custom_logger as cl


class TestPrompt(BaseClass):
    log = cl.getLogger()
    @pytest.fixture(autouse=True)
    def classMethod(self):
        self.pp = PromptPage(self.driver)


    def test_create_prompt_memory(self):
        self.pp.prompt_memory("Test prompt memory during automation " + str(date.today()),"", "Test description during automation")
        self.pp.verify_prompt_memory_publish()