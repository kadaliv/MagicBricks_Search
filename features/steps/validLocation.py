import time
from behave import *
from hamcrest import *
from features.pages.SearchClass import SearchClass
from datafiles import ExcelUtils
from features.utility.ConfigClass import ConfigClass

###################### First location dataset ########################
@step("User enter the location {ValidLocation} for first dataset")
def step_impl(context, ValidLocation):
    ExcelUtils.get_row_count(ConfigClass.dataFilePath, "Sheet1")
    ValidLocation = ExcelUtils.read_data(ConfigClass.dataFilePath, "Sheet1", 2, 1)
    time.sleep(2)
    enterValidLocation = SearchClass(context.driver)
    enterValidLocation.enter_valid_location(ValidLocation)

@step("User selects location from the drop-down list")
def step_impl(context):
    time.sleep(2)
    selectLocation = SearchClass(context.driver)
    selectLocation.select_location()

@then("It shows the first dataset related locations")
def step_impl(context):
    context.driver.implicitly_wait(10)
    context.textVisibility = SearchClass(context.driver)
    expectedTitle = '2 BHK Flats in Visakhapatnam for Sale'
    actualTitle = context.textVisibility.get_Text()
    print("The text is : " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))

#######################second location dataset ###########################

@step("User enter the location {ValidLocation} for second dataset")
def step_impl(context, ValidLocation):
    ExcelUtils.get_row_count(ConfigClass.dataFilePath, "Sheet1")
    ValidLocation = ExcelUtils.read_data(ConfigClass.dataFilePath, "Sheet1", 3, 1)
    time.sleep(2)
    enterValidLocation = SearchClass(context.driver)
    enterValidLocation.enter_valid_location(ValidLocation)

@then("It shows the second dataset related locations")
def step_impl(context):
    expectedTitle = "2 BHK Flats for Sale in Pro cube, Vadodara"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))