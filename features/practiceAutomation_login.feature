Feature: Test the login page

  Background:
    Given I am on the login page

  @login
  Scenario: Test valid login
    When I send a valid username and password
    And I press on the login button
    Then I will see the following message: "Logged In Successfully"
    And I will see the Logout button

  @login
  Scenario: Test invalid login with correct username but wrong password
    When I send a correct username and wrong password
    And I click on the login button
    Then I will see the display banner: "Your password is invalid!"

  @login
  Scenario Outline: Test invalid login with wrong usernames and correct/wrong passwords
    When I send a wrong "<username>" and "<password>"
    And I press on the login button
    Then I will see the display banner: "Your username is invalid!"
    Examples:
      | username  | password    |
      | student22 | pass123     |
      | stud123   | Password123 |