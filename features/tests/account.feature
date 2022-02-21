# Created by saeed at 2/20/22
Feature: account icon
  Scenario: clicking on account icon takes user to login page
    Given gettop.us is open
    When clicking on account icon
    Then login page is open
