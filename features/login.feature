Feature: Login functionality

  @login_done
  Scenario: Login with valid credentials
    Given I navigated to login page
    When I enter valid email and valid password into the fields
    And I click on login button
    Then I should get logged in

  @login_done
  Scenario: Login with invalid email and valid password
    Given I navigated to login page
    When I enter invalid email and valid password into the fields
    And I click on login button
    Then I should get a proper warning message

  @login_done
  Scenario: Login with valid email and invalid password
    Given I navigated to login page
    When I enter valid email and invalid password into the fields
    And I click on login button
    Then I should get a proper warning message

  @login_done
  Scenario: Login with invalid credentials
    Given I navigated to login page
    When I enter invalid email and invalid password into the fields
    And I click on login button
    Then I should get proper warning message

  @login_done
  Scenario: Login without providing any credentials
    Given I navigated to login page
    When I don't enter anything into email and password fields
    And I click on login button
    Then I should get proper warning message