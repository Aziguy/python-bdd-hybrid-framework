Feature: Register account functionality

  Scenario: Register with mandatory fields
    Given I navigate to register page
    When I fill mandatory fields
    And I click on continue button
    Then Account should be created

  Scenario: Register with all fields
    Given I navigate to register page
    When I fill all fields
    And I click on continue button
    Then Account should be created

  Scenario: Register with a duplicate email address
    Given I navigate to register page
    When I fill all fields except email field
    And I fill an existing amail address into the email field
    And I click on continue button
    Then Proper warning message informing about duplicate account should be displayed

  Scenario: Register without fill any fields
    Given I navigate to register page
    When I don't fill any fields
    And I click on continue button
    Then Proper warning message for every mandatory fields should be displayed