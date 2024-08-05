Feature: Login functionality

  @login_done
  Scenario Outline: Login with valid credentials
    Given I navigated to login page
    When I enter valid email as "<email>" and valid password as "<password>" into the fields
    And I click on login button
    Then I should get logged in
    Examples:
      |email                          |password               |
      |aziguy_one@gmail.com           |secure_password_one    |
      |aziguy_two@gmail.com           |secure_password_two    |
      |aziguy_two@gmail.com           |secure_password_three  |

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