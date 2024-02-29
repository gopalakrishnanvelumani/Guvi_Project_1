import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.TC_PIM_02 import EditEmployee
from utilities.BaseClass import BaseClass

class Test_PIM_02(BaseClass):




    def test_PIM_02(self, setup):
        editEmp = EditEmployee(self.driver)
        editEmp.getUsername().send_keys("Admin")
        editEmp.getPassword().send_keys("admin123")
        editEmp.getSubmit().click()
        editEmp.getPim().click()
        editEmp.getPlace().send_keys("Gopalakrishnan")
        editEmp.getSearch().click()
        editEmp.getEdit().click()
        time.sleep(5)
        editEmp.getEditClick().click()
        editEmp.getEditClick().send_keys(Keys.CONTROL + 'a')
        editEmp.getEditClick().send_keys(Keys.BACKSPACE)
        editEmp.getEditClick().send_keys("Velumani")
        print("The employee information is edited and updated successfully")




