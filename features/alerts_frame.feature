Feature: Test alerts elements

  Background:
    Given I am on the main page

  @alerts
  Scenario: Test confirm OK button from alerts
    When I press on the alerts_frame button
    And I press on alerts button
    And I press on confirm button
    And I press on the OK button from the alert pop-up
    Then I should see the following message: "You selected Ok"

  @alerts
  Scenario: Test confirm Cancel button from alerts
    When I press on the alerts_frame button
    And I press on alerts button
    And I press on confirm button
    And I press on the Cancel button from the alert pop-up
    Then I should see the following message: "You selected Cancel"
