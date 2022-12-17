from page.main_page import MainPage
from page.base_page import Page


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.base_page = Page(self.driver)
