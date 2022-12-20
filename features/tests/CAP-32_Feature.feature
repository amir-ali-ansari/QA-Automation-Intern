# Created by AAA at 12/19/2022
Feature: user can delete an item from the cart

  Scenario: user delete an item from the cart
    Given open CureSkin web
    When search for a product
    And add items to the cart
    And view and delete the product
    Then Verify cart is empty






