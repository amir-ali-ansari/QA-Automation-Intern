from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@given('open CureSkin web')
def open_CureSkin(context):
    context.app.main_page.open_main()


@when('login to a profile')
def log_in(context):
    context.app.main_page.log_in()
    sleep(20)


@when('search for a product')
def search_for_product(context):
    context.app.main_page.search_product("shampoo")


@when('add items to the cart')
def add_to_cart(context):
    context.app.main_page.add_item()



@when('logout from profile')
def log_out(context):
        context.app.main_page.log_out()


@then('user verify that cart is empty')
def verify_cart_is_empty(context):
    context.app.main_page.cart_is_empty()

