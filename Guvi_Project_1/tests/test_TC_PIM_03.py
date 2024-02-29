from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
from TestData.TC_Login_01_Data import TC_Login_01_Data
from pageObjects.TC_Login_01 import Login
from pageObjects.TC_PIM_03 import del_emp
from utilities.BaseClass import BaseClass


class TestDeleteEmployee(BaseClass):

    def test_deleteEmp(self, setup):
        delete = del_emp(self.driver)
        delete.getUsername().send_keys("Admin")
        delete.getPassword().send_keys("admin123")
        delete.getSubmit().click()
        delete.getPim().click()
        delete.getPlace().send_keys("Gopalakrishnan")
        delete.getSearch().click()
        delete.getDelButton().click()
        delete.getDeleted().click()




