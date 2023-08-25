Feature: Login Page

  @regression
  Scenario Outline: To check the login functionality of the Customer with Valid Data
    Given User should launch the application in the edge browser
    And User should enter the value for Username and Password as "<Username>" and "<Password>"
    When User clicks on the SignIn Button
    Then The application should navigate the user to My Account page

    Examples:
      | Username               | Password   |
      | sabarivivek7@gmail.com | Sabari@123 |
      | sabarivivek7@gmail.com | Sabari@123 |