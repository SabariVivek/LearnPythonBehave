Feature: Create An Account Feature

  Scenario: To create an account functionality
    Given Launch the browser and navigate to create account page
    And Enter random values in firstname, lastname, email, password, confirm_password
    When Clicks on Create An Account Button
    Then User should navigates to My Account Page
