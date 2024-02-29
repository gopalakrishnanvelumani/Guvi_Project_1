from selenium.webdriver.common.by import By
# import BaseClass


class del_emp():

    def __init__(self, driver):
        self.driver = driver

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    submit = (By.XPATH, "//button[@type='submit']")
    pim = (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='PIM']")
    placeHolder = (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
    search = (By.XPATH, "//button[normalize-space()='Search']")
    delButton = (By.XPATH, "(//button[@type='button'])[5]")
    deleted = (By.XPATH, "//button[normalize-space()='Yes, Delete']")



    def getUsername(self):
        return self.driver.find_element(*del_emp.username)

    def getPassword(self):
        return self.driver.find_element(*del_emp.password)

    def getSubmit(self):
        return self.driver.find_element(*del_emp.submit)

    def getPim(self):
        return self.driver.find_element(*del_emp.pim)

    def getPlace(self):
        return self.driver.find_element(*del_emp.placeHolder)

    def getSearch(self):
        return self.driver.find_element(*del_emp.search)

    def getDelButton(self):
        return self.driver.find_element(*del_emp.delButton)

    def getDeleted(self):
        return self.driver.find_element(*del_emp.deleted)

