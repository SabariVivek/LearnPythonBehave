from behave import *
from features.pages.LoginPage import *


@given(u'User should launch the application in the edge browser')
def step_impl(context):
    application_launching(context)


@given(u'User should enter the value for Username and Password as "{username}" and "{password}"')
def step_impl(context, username, password):
    enter_username_and_password(context, username=username, password=password)


@when(u'User clicks on the SignIn Button')
def step_impl(context):
    clicks_on_sign_in_button(context)


@then(u'The application should navigate the user to My Account page')
def step_impl(context):
    navigates_to_my_account_page(context)
