import pytest


@pytest.mark.usefixtures("init_browser")
class BasePage:

    def implicitly_wait(self):
        self.driver.implicitly_wait(10)




