#@functionaltests
Feature: : Valid Location

Background:
  Given Chrome is opened and Magic bricks app is opened
    When User Clicks on location field and removes the default Value

  Scenario: Validate location field in the search bar with valid data
    And User enter the location ValidLocation for first dataset
    And User selects location from the drop-down list
    And User Clicks on search button
    Then It shows the first dataset related locations

  Scenario: Validate location field in the search bar with valid data
    And User enter the location ValidLocation for second dataset
    And User selects location from the drop-down list
    And User Clicks on search button
    Then It shows the second dataset related locations

