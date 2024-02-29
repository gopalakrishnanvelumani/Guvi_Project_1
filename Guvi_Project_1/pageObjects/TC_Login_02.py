from selenium.webdriver.common.by import By


class invalidLogin:

    def __init__(self, driver):
        self.driver = driver

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    submit = (By.XPATH, "//button[@type='submit']")

    def getUsername(self):
        return self.driver.find_element(*invalidLogin.username)

    def getPassword(self):
        return self.driver.find_element(*invalidLogin.password)

    def getSubmit(self):
        return self.driver.find_element(*invalidLogin.submit)
