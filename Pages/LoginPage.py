from selenium.webdriver.common.by import By

from Pages.JobsPage import JobsPage


class LoginPage:

    username = (By.XPATH, "//input[@formcontrolname='email']")
    password = (By.XPATH, "//input[@formcontrolname='password']")
    login_button = (By.XPATH, "//button[contains(@class,'login-btn')]")

    def __init__(self, driver):
        self.driver = driver

    def input_username(self):
        return self.driver.find_element(*LoginPage.username)

    def input_password(self):
        return self.driver.find_element(*LoginPage.password)

    def login_button_click(self):
        self.driver.find_element(*LoginPage.login_button).click()
        jobspage = JobsPage(self.driver)
        return jobspage





