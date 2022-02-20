# Created by saeed at 2/19/22
Feature: home page link
  Scenario Outline: going back to home page from navigation bar items
    Given gettop.us is open
    And clicking on navigation bar item <nav_item>
    When clicking home page icon
    Then home page is browsed
    Examples:
      | nav_item |
      | MacBook  |
      | iphone   |
      | ipad     |
      | watch    |
      | airpods   |

  Scenario Outline: going back to home page from a searched product page
    Given  gettop.us is open
    And searching for item <item_title>
    When clicking home page icon
    Then home page is browsed
  Examples:
    |item_title|
    | macbook |
    | apple    |
    | watch    |
    | series |