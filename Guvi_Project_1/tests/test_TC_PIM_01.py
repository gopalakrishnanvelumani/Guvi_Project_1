import pytest
from TestData.TC_PIM_01_Data import TC_PIM_01_Data
from pageObjects.TC_PIM_01 import AddEmployee
from utilities.BaseClass import BaseClass


class Test_PIM_01(BaseClass):

    def test_pim(self, setup, pimData):
        addEmp = AddEmployee(self.driver)
        addEmp.getUsername().send_keys(pimData["username"])
        addEmp.getPassword().send_keys(pimData["password"])
        addEmp.getSubmit().click()
        addEmp.getPim().click()
        addEmp.getAdd().click()
        addEmp.getFName().send_keys(pimData["f_name"])
        addEmp.getlName().send_keys(pimData["l_name"])
        addEmp.getSave().click()
        DOB = (addEmp.getDOB())
        date = "1996-08-09"
        DOB.send_keys(date)

    @pytest.fixture(params=TC_PIM_01_Data.PIM_01_Data)
    def pimData(self, request):
        return request.param
