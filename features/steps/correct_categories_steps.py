from behave import given, when, then


@given("gettop.us is open")
def get_top_browsed(context):
    context.app.main_page.open()


@when("clicking on category {category}")
def click_cat(context, category):
    context.category = category
    context.app.main_page.select_category(category)


@then("All browsed items have category label {category_label}")
def text_label_on_items(context, category_label):
    context.app.category_page.check_text_labels(category_label)


@then('"Showing all <N> results" is present with matching <N>')
def count_of_categories(context):
    context.app.category_page.check_count(context.category)


@then("All browsed items have category, name and price")
def have_cat_name_price(context):
    context.app.category_page.count_name_price_title()


@then("Quick View opens and closes properly")
def open_close_QV(context):
    context.app.category_page.open_and_close_quick_view()


@then("Adding each item from Quick View to cart and seeing added item")
def add_item_cart(context):
    context.app.category_page.add_to_cart()



