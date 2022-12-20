from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@then("user should authenticate again")
def authenticate_after_logout(context):
    context.driver.back()
    sleep(5)
    assert 'https://shop.cureskin.com/account/login' in context.driver.current_url, f'Got {context.driver.current_url}'
    print(context.driver.curren_window_handler)





