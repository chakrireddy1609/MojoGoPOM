from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Pages.PublishersPage import PublishersPage


class JobsPage(BasePage):

    def __init__(self,driver):
        self.driver = driver

    job_names = (By.XPATH, "//span[@class='name']")
    count_jobs = (By.XPATH, "//div[contains(@class,'active-tab')]/p[2]")
    tab_notpublished = (By.XPATH, "//p[text()='Not published']")
    tab_free = (By.XPATH, "//p[text()='Free']")
    tab_sponsored = (By.XPATH, "//p[text()='Sponsored']")
    tab_all = (By.XPATH, "//p[text()='All']")

    def assert_jobcount(self):
        count = self.driver.find_elements(*JobsPage.job_names)
        assert len(count) != 0

    def count_active(self):
        active_jobs = self.driver.find_element(*JobsPage.count_jobs)
        print("Count of Active jobs : ", active_jobs.text)

    def notpublished(self):
        return self.driver.find_element(*JobsPage.tab_notpublished)

    def count_notpublished(self):
        notpublished_jobs = self.driver.find_element(*JobsPage.count_jobs)
        print("Count of Not Published jobs : ", notpublished_jobs.text)

    def free(self):
        return self.driver.find_element(*JobsPage.tab_free)

    def count_free(self):
        free_jobs = self.driver.find_element(*JobsPage.count_jobs)
        print("Count of Free jobs : ", free_jobs.text)

    def sponsored(self):
        return self.driver.find_element(*JobsPage.tab_sponsored)

    def count_sponsored(self):
        sponsored_jobs = self.driver.find_element(*JobsPage.count_jobs)
        print("Count of Sponsored jobs : ", sponsored_jobs.text)

    def all(self):
        return self.driver.find_element(*JobsPage.tab_all)

    def count_all(self):
        all_jobs = self.driver.find_element(*JobsPage.count_jobs)
        print("Count of All jobs : ", all_jobs.text)
        publisherspage = PublishersPage(self.driver)
        return publisherspage






