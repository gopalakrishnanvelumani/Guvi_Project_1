from selenium.webdriver.common.by import By


class EditEmployee:

    def __init__(self, driver):
        self.driver = driver

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    submit = (By.XPATH, "//button[@type='submit']")
    pim = (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='PIM']")
    placeHolder = (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
    search = (By.XPATH, "//button[normalize-space()='Search']")
    edit = (By.XPATH, "//i[@class='oxd-icon bi-pencil-fill']")
    editClick = (By.XPATH, "//input[@placeholder='Last Name']")

    def getUsername(self):
        return self.driver.find_element(*EditEmployee.username)

    def getPassword(self):
        return self.driver.find_element(*EditEmployee.password)

    def getSubmit(self):
        return self.driver.find_element(*EditEmployee.submit)

    def getPim(self):
        return self.driver.find_element(*EditEmployee.pim)

    def getPlace(self):
        return self.driver.find_element(*EditEmployee.placeHolder)

    def getSearch(self):
        return self.driver.find_element(*EditEmployee.search)

    def getEdit(self):
        return self.driver.find_element(*EditEmployee.edit)

    def getEditClick(self):
        return self.driver.find_element(*EditEmployee.editClick)


