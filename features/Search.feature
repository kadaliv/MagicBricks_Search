#@functionaltests
Feature: search bar

Background:
    Given Chrome is opened and Magic bricks app is opened

    Scenario Outline: Validate location field in the search bar with Invalid data
        When User Clicks on location field and removes the default Value
        And User enter the location <InvalidLocation> in the location field
        And User Clicks on search button
        Then It will show default display the placeholder text

    Examples:
    | InvalidLocation |
    | #&^&45 |
    | France |

    Scenario: Validate to edit property type field
        When User Clicks on Property Type field
        And User removes the default Value by deselecting options
        And User select property type features
        And User Clicks on search button
        Then It shows the related properties

    Scenario: validate the budget field
        When User Clicks on budget field
        And User selects min and max budget from the drop down-list
        And User Clicks on search button
        Then It shows the expected results

    Scenario: Validate the Ts_PostFreePropertyAd link
        When User Clicks on Ts_PostFreePropertyAd link
        Then It displays Ts_PostFreePropertyAd home page

    Scenario: Validate the Commercial Type (Lease/rent) drop-down list
        When User Clicks on Commercial tab
        And User Clicks on Lease/Rent drop-down list
        And User Clicks on search button
        Then It shows the available results





