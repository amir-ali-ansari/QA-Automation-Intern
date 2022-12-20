from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.base_page import Page
from app.application import Application
from page.main_page import MainPage
from selenium.webdriver.chrome.options import Options


def browser_init(context):
    """
    :param context: Behave context
    """
    options = Options()
    options.headless = True
    context.driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=options)
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox(executable_path='./geckodriver.exe')
    context.driver.maximize_window()
    # context.driver.implicitly_wait(4)
    context.wait=WebDriverWait(context, 10)
    # wait = WebDriverWait(context.driver, 10)
    context.page = Page(context.driver)
    context.page = MainPage(context.driver)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
