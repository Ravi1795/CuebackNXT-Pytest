import time

import pytest

from pages.SignUpPage import SignUpPage
from pages.login_page import LoginPage
from utilities.BaseClass import BaseClass


class TestSignUp(BaseClass):
    @pytest.fixture(autouse=True)
    def classMethod(self):
        self.sp = SignUpPage(self.driver)
        self.lp = LoginPage(self.driver)

    def test_signup_without_firstName(self):
        self.lp.logout()
        time.sleep(3)
        self.sp.signup("", "Nagesh", "ravi88@mailinator.com", "1995", "Rr@778998445665", "Rr@778998445665")
        result = self.sp.verify_signup_without_first_name()
        assert result == True

    def test_signup_without_lastName(self):
        self.sp.signup("Rohit", "", "ravi89@mailinator.com", "1995", "Rr@778998445665", "Rr@778998445665")
        result = self.sp.verify_signup_without_last_name()
        assert result == True

    def test_signup_without_email(self):
        self.sp.signup("Rohit", "Nagesh", "", "1995", "Rr@778998445665", "Rr@778998445665")
        result = self.sp.verify_signup_without_email()
        assert result == True

    def test_signup_with_invalid_email(self):
        self.sp.signup("Rohit", "Nagesh", "ravi91@mailinator", "1995", "Rr@778998445665", "Rr@778998445665")
        result = self.sp.verify_signup_with_invalid_email()
        assert result == True

    def test_signup_without_birthyear(self):
        self.sp.signup("Rohit", "Nagesh", "ravi89@mailinator.com", "", "Rr@778998445665", "Rr@778998445665")
        result = self.sp.verify_signup_without_birthyear()
        assert result == True

    def test_signup_with_invalid_birth_year(self):
        self.sp.signup("Rohit", "Nagesh", "ravi92@mailinator.com", "2025", "Rr@778998445665", "Rr@778998445665")
        result = self.sp.verify_invalid_birthyear()
        assert result == True

    def test_signup_with_birth_year_before_1920(self):
        self.sp.signup("Rohit", "Nagesh", "ravi92@mailinator.com", "1918", "Rr@778998445665", "Rr@778998445665")
        result = self.sp.verify_birth_year()
        assert result == True

    def test_valid_signup(self):
        self.sp.signup("Rohit", "Nagesh", self.sp.email(), "1995", "Rr@778998445665", "Rr@778998445665")
        result = self.sp.verify_valid_signup()
        time.sleep(5)
        assert result == True

