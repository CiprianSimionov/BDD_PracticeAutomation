from behave import *


@given(u'I am on demoblaze homepage')
def step_impl(context):
    print(u'STEP: Given I am on demoblaze homepage')
    context.base_page.demoblaze_page()


@when(u'I press on laptops categories')
def step_impl(context):
    print(u'STEP: When I press on laptops categories')
    context.demoblaze_page.click_laptops_categories()


@when(u'I select MacBook air')
def step_impl(context):
    print(u'STEP: When I select MacBook air')
    context.demoblaze_page.click_macBook_air()


@when(u'I press Add to cart')
def step_impl(context):
    print(u'STEP: When I press Add to cart')
    context.demoblaze_page.add_to_cart()


@then(u'I should see product added to cart')
def step_impl(context):
    print(u'STEP: Then I should see product added to cart')
    context.demoblaze_page.verify_cart_product()


@when(u'I press place order button')
def step_impl(context):
    print(u'STEP: When I press place order button')
    context.demoblaze_page.place_order()


@when(u'I fill out the form')
def step_impl(context):
    print(u'STEP: When I fill out the form')
    context.demoblaze_page.fill_out_form()


@then(u'I should see the following message: "Thank you for your purchase!"')
def step_impl(context):
    print(u'STEP: Then I should see the following message: "Thank you for your purchase!"')
    context.demoblaze_page.verify_purchase()
