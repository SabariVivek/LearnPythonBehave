from selenium.webdriver.common.by import By


class LoginPageLocators:
    Email = (By.XPATH, "//input[@id='email']")
    Password = (By.XPATH, "(//input[@id='pass'])[1]")
    SignIn = (By.XPATH, "(//span[text()='Sign In'])[1]")
    CreateAnAccount = (By.XPATH, "(//span[text()='Create an Account'])[1]")


class CreateAnAccountLocators:
    FirstName = (By.ID, "firstname")
    LastName = (By.ID, "lastname")
    Email = (By.ID, "email_address")
    Password = (By.ID, "password")
    ConfirmPassword = (By.ID, "password-confirmation")
    CreateAnAccountButton = (By.XPATH, "//button[@class='action submit primary']")


class MyAccountLocators:
    MyAccount = (By.XPATH, "//h1[@class='page-title']/span")
