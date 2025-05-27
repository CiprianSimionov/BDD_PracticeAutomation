from behave import *


@given(u'I am on the main page')
def step_impl(context):
    print(u'STEP: Given I am on the main page')
    context.base_page.access_elements_page()


@when(u'I press on the alerts_frame button')
def step_impl(context):
    print(u'STEP: When I press on the alerts_frame button')
    context.alerts_frame_page.click_alerts_frame()


@when(u'I press on alerts button')
def step_impl(context):
    print(u'STEP: When I press on alerts button')
    context.alerts_frame_page.click_alerts()


@when(u'I press on confirm button')
def step_impl(context):
    print(u'STEP: When I press on confirm button')
    context.alerts_frame_page.click_confirm_button()


@when(u'I press on the OK button from the alert pop-up')
def step_impl(context):
    print(u'STEP: When I press on the OK button from the alert pop-up')
    context.alerts_frame_page.click_ok_button()


@then(u'I should see the following message: "You selected Ok"')
def step_impl(context):
    print(u'STEP: Then I should see the following message: "You selected Ok"')
    context.alerts_frame_page.confirmed_ok()


@when(u'I press on the Cancel button from the alert pop-up')
def step_impl(context):
    print(u'STEP: When I press on the Cancel button from the alert pop-up')
    context.alerts_frame_page.click_cancel_button()

@then(u'I should see the following message: "You selected Cancel"')
def step_impl(context):
    print(u'STEP: Then I should see the following message: "You selected Cancel"')
    context.alerts_frame_page.confirmed_cancel()
