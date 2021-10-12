from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Pages.SettingsPage import SettingsPage


class PublishersPage(BasePage):

    def __init__(self,driver):
        self.driver = driver


    publishers_icon = (By.XPATH, "//mat-icon[@data-mat-icon-name='sponsoring']//*[name()='svg']")
    publishers_name = (By.XPATH, "//tr[@role='row']/td[1]/span")

    def click_publisher_icon(self):
        return self.driver.find_element(*PublishersPage.publishers_icon)

    def count_publisher_names(self):
        publisher_names = self.driver.find_elements(*PublishersPage.publishers_name)
        assert len(publisher_names) != 0
        settingspage = SettingsPage(self.driver)
        return settingspage
