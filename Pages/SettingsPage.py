from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class SettingsPage(BasePage):

    def __init__(self,driver):
        self.driver = driver

    settings_icon = (By.XPATH, "//mat-icon[@data-mat-icon-name='settings']//*[name()='svg']")

    def click_settings_icon(self):
        return self.driver.find_element(*SettingsPage.settings_icon)
