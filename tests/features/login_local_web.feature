Feature: Login

  Scenario Outline: Successful login from home page
    Given I am on the home page
    When I login with firstname "<firstname>" and secondname "<secondname>"
    Then I should see the dashboard

    Examples:
      | firstname | secondname  |
      | byb    | byb   |