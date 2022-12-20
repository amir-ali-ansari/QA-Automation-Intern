# Created by AAA at 12/19/2022
Feature: after logout user should re-enter email and password

  Scenario: The cart should be empty after logout
    Given open CureSkin web
    When login to a profile
    And logout from profile
    Then user should authenticate again