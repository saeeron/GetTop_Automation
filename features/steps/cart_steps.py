from behave import given, when, then


@when("clicking on cart icon")
def click_on_cart_icon(context):
    context.app.main_page.click_on_cart()


@then("navigating to empty cart page")
def is_empty_cart_page(context):
    context.app.cart_page.is_empty_cart_page()


@when("hovering mouse over cart icon")
def hover_mouse_on_cart(context):
    context.app.main_page.mouse_on_cart_icon()


@then("\"No products in the cart.\" is shown")
def empty_cart_icon(context):
    context.app.main_page.presence_of_empty_cart_text()


@given("page for iPhone SE is open")
def iphone_SE_page(context):
    context.app.main_page.open_page("product/iphone-se/")


@when("setting quantity {num}")
def set_quantity(context, num):
    context.app.product_page.set_quantity(num)


@when("pushing \"Add To Cart\"")
def push_add(context):
    context.app.product_page.push_add_to_cart()


@then("Nav bar shows correct subtotal")
def nav_bar_subtotal_check(context):
    context.app.nav_bar_page.read_subtotal()
    assert float(context.app.nav_bar_page.subtotal[1:]) == int(context.app.product_page.quantity) * \
           float(context.app.product_page.unit_price[1:]), "ERROR, the added items do not sum up to correct subtotal" \
                                                           " in the cart"


@then("cart shows correct quantity")
def nav_bar_quantity_check(context):
    context.app.nav_bar_page.read_quantity()
    assert f"{context.app.nav_bar_page.quantity}" == context.app.product_page.quantity, \
        f"ERROR, expected {context.app.product_page.quantity}, but observed {context.app.nav_bar_page.quantity}"


@then("correct product is shown")
def correct_product(context):
    context.app.nav_bar_page.read_product()
    assert context.app.nav_bar_page.product.strip() == "iPhone SE", "ERROR, product is not correct"


@then("\"View Cart\" is present")
def view_cart_clickable(context):
    context.app.nav_bar_page.view_cart_is_present()


@when("clicking on \"View Cart\"")
def click_on_view_cart(context):
    context.app.nav_bar_page.click_on_view_cart()


@then("\"Checkout\" is present")
def checkout_clickable(context):
    context.app.nav_bar_page.checkout_is_present()


@when("clicking on \"Checkout\"")
def click_on_checkout(context):
    context.app.nav_bar_page.click_on_checkout()


@then("navigating to cart page")
def is_cart_page(context):
    assert context.app.nav_bar_page.driver.current_url == "https://gettop.us/cart/", "ERROR, it is not cart page"


@then("navigating to checkout page")
def is_checkout(context):
    assert context.app.nav_bar_page.driver.current_url == "https://gettop.us/checkout/", "ERROR, it is not checkout page"


@when("push remove item")
def close_item(context):
    context.app.nav_bar_page.click_on_remove_item()
