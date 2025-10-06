Feature: Login functionality

  Scenario Outline: Successful login with different users
    Given I am on the login page
    When I login with username "<username>" and password "<password>"
    Then I should see the dashboard page

    Examples:
      | username | password  |
      | admin    | 1234      |
      | guest    | guest123  |
