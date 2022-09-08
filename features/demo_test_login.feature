Feature: Duplicate Feature

#  Background:
@validation
  Scenario: This is duplicate scenario
    Given Open web browser
    When I am on the OrangeHRM login page
    Then I enter "Admin" as username and "admin123" as password
    And I click on login button
    Then I should see the OrangeHRM home page
    And Close the web browser
