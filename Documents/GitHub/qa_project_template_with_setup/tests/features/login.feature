Feature: Login functionality

  Scenario Outline: Successful login with different users
    Given I am on the login page
    #When I click on personal account
    When I login with firstname "<firstname>" and secondname "<secondname>"
    Then I should see the dashboard page
    #And I go to visitor log page
    #Then I verify that my sign in is recorded



    Examples:
      | firstname | secondname  |
      | doshikdoshirak39@gmail.com    | Tampa1488!   |
  #    | guest    | guest123  |
