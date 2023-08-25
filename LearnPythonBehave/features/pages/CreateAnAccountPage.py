from features.locators.Locators import CreateAnAccountLocators, LoginPageLocators, MyAccountLocators
from features.constants.Constants import MyAccountPageConstant
from features.utils.Random import *
from features.utils.GenericMethods import *


def navigates_to_create_account_page(context):
    click(context, LoginPageLocators.CreateAnAccount)


def enter_required_details_for_account_creation(context):
    enter(context, CreateAnAccountLocators.FirstName, random_first_name())
    enter(context, CreateAnAccountLocators.LastName, random_last_name())
    enter(context, CreateAnAccountLocators.Email, random_email())
    password = random_password()
    enter(context, CreateAnAccountLocators.Password, password)
    enter(context, CreateAnAccountLocators.ConfirmPassword, password)


def clicks_on_create_an_account_button(context):
    click(context, CreateAnAccountLocators.CreateAnAccountButton)


def navigates_to_my_account_page(context):
    my_account_identifier = get_text(context, MyAccountLocators.MyAccount)
    if my_account_identifier.__eq__(MyAccountPageConstant.MY_ACCOUNT):
        print("Successfully created an account")
