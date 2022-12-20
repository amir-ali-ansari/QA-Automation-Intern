from behave import given, when, then
from selenium.webdriver.common.by import By

from time import sleep

CART_BTN = (By.ID, "cart-icon-bubble")
CART_DELETE_BTN = (By.ID, "Remove-1")

@when ('view and delete the product')
def delete_product(context):
    context.app.base_page.click(*CART_BTN)
    context.app.base_page.click(*CART_DELETE_BTN)
    sleep(1)
@then('Verify cart is empty')
def verify_cart_empty(context):
    expected_value = 'Your cart is empty'
    actual_value = context.driver.find_element(By.CSS_SELECTOR, ".cart__empty-text").text
    assert expected_value == actual_value, f'error| expected: {expected_value}, but got {actual_value}'



