from behave import *
from features.pages.CreateAnAccountPage import *


@given(u'Launch the browser and navigate to create account page')
def step_impl(context):
    navigates_to_create_account_page(context)


@given(u'Enter random values in firstname, lastname, email, password, confirm_password')
def step_impl(context):
    enter_required_details_for_account_creation(context)


@when(u'Clicks on Create An Account Button')
def step_impl(context):
    clicks_on_create_an_account_button(context)


@then(u'User should navigates to My Account Page')
def step_impl(context):
    navigates_to_my_account_page(context)
