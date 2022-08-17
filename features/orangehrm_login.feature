Feature: Login into OrangeHRM

  Scenario: Login into OrangeHRM
    Given Open web browser
    When I am on the OrangeHRM login page
    Then I enter "Admin" as username and "admin123" as password
    And I click on login button
    Then I should see the OrangeHRM home page
    And Close the web browser


  Scenario Outline: Login into OrangeHRM
    Given Open web browser
    When I am on the OrangeHRM login page
    Then I enter "<username>" as username and "<password>" as password
    And I click on login button
    Then I should see the OrangeHRM home page
    And Close the web browser

    Examples:
    | username | password |
    | Admin    | admin123 |
    | User     | user123  |
    | Alpha    | alpha123 |