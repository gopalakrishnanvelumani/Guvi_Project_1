import pytest
from TestData.TC_Login_01_Data import TC_Login_01_Data
from pageObjects.TC_Login_01 import Login
from utilities.BaseClass import BaseClass


class Test_login(BaseClass):

    def test_login(self, setup, getData):
        login = Login(self.driver)
        login.getUsername().send_keys(getData["username"])
        login.getPassword().send_keys(getData["password"])
        login.getSubmit().click()
        print("The User is Logged in successfully")

    @pytest.fixture(params=TC_Login_01_Data.Login_01_Data)
    def getData(self, request):
        return request.param
