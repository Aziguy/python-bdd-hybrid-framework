Feature: Search functionality

  @search_done
  Scenario: Search for a valid product
    Given I am on home page screen
    When I enter valid product as "HP" into the search box field
    And I click on Search button
    Then Valid product should get display in search results

  @search_done
  Scenario: Search for an invalid product
    Given I am on home page screen
    When I enter invalid product as "Honda" into the search box field
    And I click on Search button
    Then Proper message should be displayed in search results

  @search_done
  Scenario: Search without entering any product
    Given I am on home page screen
    When I don't enter any term into search box field
    And I click on Search button
    Then Proper message should be displayed in search results