Feature: Derp Bear Users Service

  In order to get all current users
  as a Consumer of the Derp Bear Service
  I want to the data returned to as json

  Scenario: Get a user
    When I request one user
    Then I be returned one user

