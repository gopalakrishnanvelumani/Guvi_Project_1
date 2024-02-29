import pytest
from TestData.TC_Login_02_Data import TC_Login_02_Data
from pageObjects.TC_Login_02 import invalidLogin
from utilities.BaseClass import BaseClass


class Test_invalid_login(BaseClass):

    def test_invalid_login(self, setup, getData):
        login = invalidLogin(self.driver)
        login.getUsername().send_keys(getData["username"])
        login.getPassword().send_keys(getData["invalid_password"])
        login.getSubmit().click()
        print("A valid error message for invalid credentials is displayed")

    @pytest.fixture(params=TC_Login_02_Data.Login_02_Data)
    def getData(self, request):
        return request.param
