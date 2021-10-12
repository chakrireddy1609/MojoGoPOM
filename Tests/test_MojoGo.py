import time

import pytest

from Config.TestData import TestData
from Pages.LoginPage import LoginPage
from Tests.BaseTest import BaseTest



class Test_E2E(BaseTest):

    def test_e2e(self):
        loginpage = LoginPage(self.driver)
        loginpage.input_username().send_keys(TestData.username)
        loginpage.input_password().send_keys(TestData.password)
        jobspage = loginpage.login_button_click()
        jobspage.implicitly_wait()
        jobspage.assert_jobcount()
        jobspage.count_active()
        jobspage.notpublished().click()
        jobspage.count_notpublished()
        jobspage.free().click()
        jobspage.count_free()
        jobspage.sponsored().click()
        jobspage.count_sponsored()
        jobspage.all().click()
        publisherspage = jobspage.count_all()
        publisherspage.click_publisher_icon().click()
        settingspage = publisherspage.count_publisher_names()
        settingspage.click_settings_icon().click()



