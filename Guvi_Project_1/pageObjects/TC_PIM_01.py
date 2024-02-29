from selenium.webdriver.common.by import By


class AddEmployee:

    def __init__(self, driver):
        self.driver = driver

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    submit = (By.XPATH, "//button[@type='submit']")
    pim = (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='PIM']")
    add = (By.XPATH, "//button[normalize-space()='Add']")
    f_name = (By.NAME, "firstName")
    l_name = (By.NAME, "lastName")
    save = (By.XPATH, "//button[normalize-space()='Save']")
    dob = (By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[2]")

    def getUsername(self):
        return self.driver.find_element(*AddEmployee.username)

    def getPassword(self):
        return self.driver.find_element(*AddEmployee.password)

    def getSubmit(self):
        return self.driver.find_element(*AddEmployee.submit)

    def getPim(self):
        return self.driver.find_element(*AddEmployee.pim)

    def getAdd(self):
        return self.driver.find_element(*AddEmployee.add)

    def getFName(self):
        return self.driver.find_element(*AddEmployee.f_name)

    def getlName(self):
        return self.driver.find_element(*AddEmployee.l_name)

    def getSave(self):
        return self.driver.find_element(*AddEmployee.save)

    def getDOB(self):
        return self.driver.find_element(*AddEmployee.dob)
