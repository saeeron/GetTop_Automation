from behave import when, then


@when("clicking on account icon")
def click_account(context):
    context.app.main_page.click_on_account()


@then("login page is open")
def login_appears(context):
    context.app.main_page.wait_until_appearance_login()
