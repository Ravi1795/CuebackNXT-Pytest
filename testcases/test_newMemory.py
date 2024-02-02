import time

import pytest
from pages.NewMemory import New
from utilities.BaseClass import BaseClass
from datetime import date
from random import choice


class TestNewMemory(BaseClass):

    @pytest.fixture(autouse=True)
    def classMethod(self):
        self.nm = New(self.driver)

    def test_memory_without_title(self):
        self.nm.create_memory("","","")
        result = self.nm.verify_memory_without_title()
        assert result == True

    def test_memory_with_future_date(self):
        self.nm.create_memory("Test memory during automation","02,30,3011","Test description during automation")
        result = self.nm.verify_future_date()
        assert result == True

    def test_memory_with_invalid_date(self):
        self.nm.create_memory("Test Memory during automation","01/01/0001","Test description during automation")
        result = self.nm.verify_invalid_date()
        assert result == True

    def test_memory_published(self):
        self.nm.create_memory("Test memory during automation " + str(date.today()),"", "Test description during automation")
        result = self.nm.verify_memory_publish()
        self.nm.click_back_button()
        assert result == True


    def test_memory_published_on_past_date(self):
        months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        years = ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020',
                 '2021', '2022']
        ran_date =  '{}.{}.{}'.format(*map(choice, [months, days, years]))
        self.nm.create_memory("Test memory during automation " + str(date.today()),ran_date,"Test description during automation")
        result = self.nm.verify_memory_publish()
        assert result == True