import time
import pytest
from pages.login_page import LoginPage
from utilities.BaseClass import BaseClass



class TestLogin(BaseClass):

    @pytest.fixture(autouse=True)
    def classMethod(self):
        self.lp = LoginPage(self.driver)

    def test_login_without_email(self):
        self.lp.logout()
        time.sleep(3)
        self.lp.login(" ", "Abcd@12345")
        result = self.lp.verify_test_login_without_email()
        assert result == True

    def test_login_without_password(self):
        self.lp.login("santosh.parate@infobeans.com", "")
        result = self.lp.verify_test_login_without_password()
        assert result == True

    def test_login_without_email_and_password(self):
        self.lp.login("", "")
        result = self.lp.verify_test_login_without_email()
        assert result == True

    def test_login_with_invalid_email(self):
        self.lp.login("xyz@infobeans.com", "Abc@12345")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        result = self.lp.verify_invalid_username()
        assert result == True

    def test_login_with_invalid_password(self):
        self.lp.login("santosh.parate@infobeans.com", "123243455")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        result = self.lp.verify_invalid_username()
        assert result == True

    def test_valid_login(self):
        self.lp.login("ravi701@mailinator.com","Rr@778998445665")
        time.sleep(7)
        self.lp.logout()
        time.sleep(5)
