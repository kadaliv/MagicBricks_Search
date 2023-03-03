from behave import *
from hamcrest import *
from features.pages.SearchClass import SearchClass


@given("Chrome is opened and Magic bricks app is opened")
def step_impl(context):
    context.driver.implicitly_wait(10)
    expectedTitle = "Real Estate | Property in India | Buy/Sale/Rent Properties | MagicBricks"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))

################## Scenario outline: invalid location ######################

@when("User Clicks on location field and removes the default Value")
def step_impl(context):
    context.driver.implicitly_wait(10)
    context.proType = SearchClass(context.driver)
    context.proType.click_Location_field()

@step("User enter the location {InvalidLocation} in the location field")
def step_impl(context, InvalidLocation):
    context.driver.implicitly_wait(10)
    enterInvalidLocation = SearchClass(context.driver)
    enterInvalidLocation.enter_Invalid_location(InvalidLocation)

@step("User Clicks on search button")
def step_impl(context):
    context.driver.implicitly_wait(10)
    context.searchButton = SearchClass(context.driver)
    context.searchButton.click_search_button()
    context.driver.implicitly_wait(10)

@then("It will show default display the placeholder text")
def step_impl(context):
    context.driver.implicitly_wait(10)
    context.Visibility = SearchClass(context.driver)
    expectedValue = "Enter City, Locality, Project"
    actualValue = context.Visibility.default_placeholder()
    print(actualValue)
    assert_that(expectedValue, equal_to(actualValue))

##########################Scenario: property field #################################
@when("User Clicks on Property Type field")
def step_impl(context):
    context.driver.implicitly_wait(10)
    context.propertyType = SearchClass(context.driver)
    context.propertyType.property_Type()

@step("User removes the default Value by deselecting options")
def step_impl(context):
    context.driver.implicitly_wait(10)
    context.propertyDeselect = SearchClass(context.driver)
    context.propertyDeselect.property_Deselect()

@step("User select property type features")
def step_impl(context):
    context.driver.implicitly_wait(10)
    context.propertySelect = SearchClass(context.driver)
    context.propertySelect.property_Select()

@then("It shows the related properties")
def step_impl(context):
    context.driver.implicitly_wait(10)
    context.textVisibility = SearchClass(context.driver)
    expectedTitle = True
    actualTitle = context.textVisibility.pro_Result()
    print("link text is ", actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))

###########################Scenario : Budget Field ##################################

@when("User Clicks on budget field")
def step_impl(context):
    context.driver.implicitly_wait(10)
    context.Budget = SearchClass(context.driver)
    context.Budget.Budget()

@step("User selects min and max budget from the drop down-list")
def step_impl(context):
    context.driver.implicitly_wait(10)
    context.select_Min_Max = SearchClass(context.driver)
    context.select_Min_Max.budget_Min_Max()

@then("It shows the expected results")
def step_impl(context):
    context.driver.implicitly_wait(10)
    expectedurl = 'https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Mumbai&BudgetMin=60-Lacs&BudgetMax=1.2-Crores'
    actualurl = context.driver.current_url
    print("Page url is " + actualurl)
    assert_that(expectedurl, equal_to(actualurl))

#############################Scenario : Ts_PostFreePropertyAd link ###################################
@when("User Clicks on Ts_PostFreePropertyAd link")
def step_impl(context):
    context.driver.implicitly_wait(10)
    context.adLink = SearchClass(context.driver)
    context.adLink.click()

@then("It displays Ts_PostFreePropertyAd home page")
def step_impl(context):
    context.driver.implicitly_wait(10)
    expectedTitle = "Post Free Property Ads | Rent & Sell Property Online"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))

####################Scenario : Commercail tab (Lease/Rent field) #######################
@when("User Clicks on Commercial tab")
def step_impl(context):
    context.driver.implicitly_wait(10)
    context.commTab = SearchClass(context.driver)
    context.commTab.commercial_tab()

@when("User Clicks on Lease/Rent drop-down list")
def step_impl(context):
    context.driver.implicitly_wait(10)
    context.commdropdown = SearchClass(context.driver)
    context.commdropdown.dropDownLR()

@then("It shows the available results")
def step_impl(context):
    context.driver.implicitly_wait(10)
    expectedurl = 'https://www.magicbricks.com/property-for-rent/commercial-real-estate?bedroom=&proptype=Commercial-Office-Space,Office-ITPark-SEZ,Commercial-Shop,Commercial-Showroom&categoryC=S&cityName=Mumbai'
    actualurl = context.driver.current_url
    print("Page url is " + actualurl)
    assert_that(expectedurl, equal_to(actualurl))

