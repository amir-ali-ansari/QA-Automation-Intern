# Created by AAA at 12/13/2022
Feature: Log Out from a profile

  Scenario: The cart should be empty after logout
    Given open CureSkin web
    When login to a profile
    And search for a product
    And add items to the cart
    And logout from profile
    Then user verify that cart is empty


