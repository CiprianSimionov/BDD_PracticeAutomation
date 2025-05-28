Feature: Test demoblaze purchase

  Background:
    Given I am on demoblaze homepage

  @demoblaze
  Scenario: Test add product to cart
    When I press on laptops categories
    And I select MacBook air
    And I press Add to cart
    Then I should see product added to cart

  @demoblaze
  Scenario: Test purchase product
    When I press place order button
    And I fill out the form
    Then I should see the following message: "Thank you for your purchase!"