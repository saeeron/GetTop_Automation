# Created by Saeed Roshan at 2/19/22
Feature: checking functionalities of cart

  Scenario: Clicking on Cart icon opens Empty Cart page if no products were added
    Given gettop.us is open
    When clicking on cart icon
    Then navigating to empty cart page

  Scenario: Hovering over empty cart icon shows "No products in the cart." message
    Given gettop.us is open
    When hovering mouse over cart icon
    Then "No products in the cart." is shown

   Scenario: Add product to cart, verify that price in top nav menu is correct
     Given page for iPhone SE is open
      When setting quantity 2
      And pushing "Add To Cart"
      Then Nav bar shows correct subtotal

     Scenario: Add products to cart, verify that amount of items shown in top nav menu are correct#
       Given page for iPhone SE is open
       When setting quantity 2
       And pushing "Add To Cart"
       Then cart shows correct quantity

     Scenario: Add products to cart, hover over cart icon, verify correct products and subtotal shown
        Given page for iPhone SE is open
        When setting quantity 2
        And pushing "Add To Cart"
        And hovering mouse over cart icon
        Then cart shows correct quantity
        And correct product is shown


     Scenario: Add products to cart, hover over cart icon, verify user can click on "View Cart" and is taken to cart page
         Given page for iPhone SE is open
         When setting quantity 2
         And pushing "Add To Cart"
         And hovering mouse over cart icon
         Then "View Cart" is present
         When clicking on "View Cart"
         Then navigating to cart page


     Scenario: Add products to cart, hover over cart icon, verify user can click on "Checkout" and is taken to checkout page
         Given page for iPhone SE is open
         When setting quantity 2
         And pushing "Add To Cart"
         And hovering mouse over cart icon
         Then "Checkout" is present
         When clicking on "Checkout"
         Then navigating to checkout page

     Scenario: Add a product to cart, hover over cart icon, verify user can remove a product
         Given page for iPhone SE is open
         When setting quantity 2
         And pushing "Add To Cart"
         And hovering mouse over cart icon
         And push remove item
         When hovering mouse over cart icon
         Then "No products in the cart." is shown


