Feature: Register account functionality

  @register_done
  Scenario: Register with mandatory fields
    Given I navigate to register page
    When I enter below details into mandatory fields
      |first_name|last_name|telephone   |password              |
      |John      |Doe      |0123456789  |the_super_password    |
    And I click on continue button
    Then Account should be created

    @register_done
  Scenario: Register with all fields
    Given I navigate to register page
    When I enter below details into all fields
      |first_name|last_name|telephone |password              |
      |John      |Doe      |0123456789|the_super_password    |
    And I click on continue button
    Then Account should be created

  @register_done
  Scenario: Register with a duplicate email address
    Given I navigate to register page
    When I enter details into all fields except email field
      |first_name|last_name|telephone |password              |
      |John      |Doe      |0123456789|the_super_password    |
    And I fill an existing email address as "aziguy_one@gmail.com" into the email field
    And I click on continue button
    Then Proper warning message informing about duplicate account should be displayed

  @register_done
  Scenario: Register without fill any fields
    Given I navigate to register page
    When I don't fill any fields
    And I click on continue button
    Then Proper warning message for every mandatory fields should be displayed