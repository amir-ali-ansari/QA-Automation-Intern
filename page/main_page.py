from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from page.base_page import Page


class MainPage (Page):
    LOG_IN_ICON = (By.XPATH, "/html/body/div[2]/sticky-header/header/div/a[1] ")
    LOG_IN_EMAIL = (By.ID, "CustomerEmail")
    LOG_IN_PSSWD = (By.ID, "CustomerPassword")
    LOG_IN_BTN = (By.XPATH, "//*[@id='customer_login']/button")

    SEARCH_BTN = (By.CSS_SELECTOR, ".modal__toggle-open.icon-search")
    SEARCH_INPUT = (By.ID, "Search-In-Modal")
    SEARCH_GO = (By.CSS_SELECTOR, ".search__button")

    ITEM = (By.XPATH, "/html/body/main/section/div/div[3]/div/ul/li[1]/div/div[1]/div/h3/a")
    ADD_BTN = (By.XPATH,"//button[@type='submit']")
    ACCOUNT = (By.XPATH, "//a[@href='/account']")


    LOG_OUT = (By.XPATH, "//a[@href='/account/logout']")
    CART_COUNT = (By.CSS_SELECTOR, ".cart-count-bubble")

    def open_main(self):
        self.driver.get('https://shop.cureskin.com/')

    def log_in(self):
        self.click(*self.LOG_IN_ICON)
        self.input_text("abc@gmail.com", self.LOG_IN_EMAIL)
        self.input_text("asdf4321", self.LOG_IN_PSSWD)
        self.click(*self.LOG_IN_BTN)

    def search_product(self, text):
        self.click(*self.SEARCH_BTN)
        self.input_text(text, self.SEARCH_INPUT)
        self.click(*self.SEARCH_GO)

    def add_item(self):
        self.click(*self.ITEM)
        self.click(*self.ADD_BTN)
        sleep(5)

    def log_out(self):
        self.click(*self.LOG_IN_ICON)
        sleep(5)
        self.click(*self.LOG_OUT)

    def cart_is_empty(self):
        expected = ''
        actual = self.driver.find_element(*self.CART_COUNT).text
        assert expected == actual, f"expected{expected} but actual is {actual}"