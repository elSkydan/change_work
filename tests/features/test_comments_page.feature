Feature: Login functionality

  Scenario Outline: Adding comment to the page
    Given I am on the home page
    When I login with firstname "<firstname>" and secondname "<secondname>"
    When I go to the comments page
    And I add a new comment to the comments page
    Then I verify that comment is saved




    Examples:
      | firstname | secondname  |
      | test      | test        |

