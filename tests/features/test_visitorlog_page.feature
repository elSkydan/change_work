Feature: Visitor log checkout

  Scenario Outline: Checking visitor log
    Given I am on the home page
    When I login with firstname "<firstname>" and secondname "<secondname>"
    When I go to the visitor log page
    Then I verify that log is saved


    Examples:
      | firstname | secondname |
      | test      | test       |