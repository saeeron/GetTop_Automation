from behave import given, when, then


@given("clicking on navigation bar item {item_type}")
def navigating(context, item_type):
    context.app.main_page.navigate_to_nav_bar_item(item_type)


@when("clicking home page icon")
def click_on_homepage(context):
    context.app.nav_page.click_on_homepage()


@then("home page is browsed")
def is_homepage(context):
    context.app.main_page.is_home_page()


@given("searching for item {item_title}")
def search_item(context, item_title):
    context.app.main_page.search_item(item_title)
