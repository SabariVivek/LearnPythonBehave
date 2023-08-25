from features.locators.Locators import LoginPageLocators, MyAccountLocators
from features.constants.Constants import MyAccountPageConstant
from features.utils.GenericMethods import *


def application_launching(context):
    print("Application launched in the browser successfully")


def enter_username_and_password(context, username, password):
    enter(context, LoginPageLocators.Email, username)
    enter(context, LoginPageLocators.Password, password)


def clicks_on_sign_in_button(context):
    click(context, LoginPageLocators.SignIn)


def navigates_to_my_account_page(context):
    my_account_identifier = get_text(context, MyAccountLocators.MyAccount)
    if my_account_identifier.__eq__(MyAccountPageConstant.MY_ACCOUNT):
        print("Successfully Logged In")
