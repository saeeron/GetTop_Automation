# Created by Saeed Roshan at 2/15/22
Feature: checking categories

  Scenario Outline: Only items of correct category are shown
    Given gettop.us is open
    When clicking on category <category>
    Then All browsed items have category label <category_label>
    Examples:
    | category    | category_label |
    | Accessories | Accessories    |
    | iPad        | iPad           |
    | iPhone      | iPhone         |
    | MacBook     | MacBook        |

  Scenario Outline: Showing all correct count of items under categories
    Given gettop.us is open
    When clicking on category <category>
    Then "Showing all <N> results" is present with matching <N>
    Examples:
    | category    |
    | Accessories |
    | iPad        |
    | iPhone      |
    | MacBook     |

  Scenario Outline: All browsed items have category, name and price
    Given gettop.us is open
    When clicking on category <category>
    Then All browsed items have category, name and price
    Examples:
    | category    |
    | Accessories |
    | iPad        |
    | iPhone      |
    | MacBook     |

  Scenario Outline: User can open and close Quick View by clicking on closing X
    Given gettop.us is open
    When clicking on category <category>
    Then Quick View opens and closes properly
    Examples:
    | category    |
    | Accessories |
    | iPad        |
    | iPhone      |
    | MacBook     |


  Scenario Outline: User can click Quick View and add product to cart
    Given gettop.us is open
    When clicking on category <category>
    Then Adding each item from Quick View to cart and seeing added item
   Examples:
    | category    |
    | Accessories |
    | iPad        |
    | iPhone      |
    | MacBook     |




