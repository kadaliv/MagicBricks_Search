from selenium.webdriver.common.by import By

class SearchClass:

    def __init__(self, driver):
        self.driver = driver

        # Element locator values
        self.locationSelect = "(//input[@type='text'])[1]"
        self.locationdelete = "mb-search__tag-close"
        self.enterloc =  "keyword"
        self.selectloc = "(//div[@class='mb-search__auto-suggest__item'])[1]"
        self.searchbutton = "mb-search__btn"
        self.getText = "//*[text()='2 BHK Flats in Visakhapatnam for Sale']"
        self.visible = "mb-search__input"
        self.property = "(//div[@class='mb-search__title'])[1]"
        self.propertydeselect1 = "10002_10003_10021_10022"
        self.propertydeselect2 = "10001_10017"
        self.propertyselect = "11701"
        self.proResults = "//h1[@class='mb-srp__title--text1']"
        self.budgetField = "(//div[@class='mb-search__title'])[2]"
        self.selectMinValue = "(//div[@class='mb-search__min-max__item'])[39]"
        self.maxBudget = "budgetMax"
        self.selectMaxValue = "(//div[@class='mb-search__min-max__item'])[70]"
        self.profreeAdLink = "Post Free Property Ad"
        self.Commercial = "#tabCOMM"
        self.LRdropdown = "commercialType"
        self.selectBuy = "(//div[@class='mb-search__auto-suggest__item'])[1]"

    # Creating Element Methods

    # Creating Element Methods for valid location
    def click_Location_field(self):
        protypeField = self.driver.find_element(By.XPATH, self.locationSelect)
        self.driver.execute_script("arguments[0].click();", protypeField)
        self.driver.implicitly_wait(10)
        removeDefaultTag = self.driver.find_element(By.CLASS_NAME, self.locationdelete)
        self.driver.execute_script("arguments[0].click();", removeDefaultTag)

    def enter_valid_location(self, loc):
        enterValidLoc = self.driver.find_element(By.ID,self.enterloc)
        enterValidLoc.send_keys(loc)

    def select_location(self):
        selectLoc = self.driver.find_element(By.XPATH, self.selectloc)
        self.driver.execute_script("arguments[0].click();", selectLoc)

    def click_search_button(self):
        searchButton = self.driver.find_element(By.CLASS_NAME, self.searchbutton)
        self.driver.execute_script("arguments[0].click();", searchButton)

    def get_Text(self):
        validLocValidation = self.driver.find_element(By.XPATH, self.getText).text
        return validLocValidation

    # Creating Element Methods for invalid location

    def enter_Invalid_location(self, loc):
        enterInValidLoc = self.driver.find_element(By.ID,self.enterloc)
        enterInValidLoc.send_keys(loc)
        Visibile = self.driver.find_element(By.CLASS_NAME, self.visible)
        visibility = Visibile.get_attribute("value")
        print(visibility)

    def default_placeholder(self):
        Visibile = self.driver.find_element(By.CLASS_NAME, self.visible)
        visibility = Visibile.get_attribute("placeholder")
        return visibility

    # Creating Element Methods for property field

    def property_Type(self):
        proType = self.driver.find_element(By.XPATH, self.property)
        self.driver.execute_script("arguments[0].click();", proType)

    def property_Deselect(self):
        prodeselect1 = self.driver.find_element(By.ID, self.propertydeselect1)
        self.driver.execute_script("arguments[0].click();", prodeselect1)
        prodeselect2 = self.driver.find_element(By.ID, self.propertydeselect2)
        self.driver.execute_script("arguments[0].click();", prodeselect2)

    def property_Select(self):
        proselect1 = self.driver.find_element(By.ID, self.propertydeselect1)
        self.driver.execute_script("arguments[0].click();", proselect1)
        proselect2 = self.driver.find_element(By.ID, self.propertyselect)
        self.driver.execute_script("arguments[0].click();", proselect2)

    def pro_Result(self):
        propertyResult = self.driver.find_element(By.XPATH, self.proResults).is_displayed()
        return propertyResult

    # Creating Element Methods for Budget Field

    def Budget(self):
        budget = self.driver.find_element(By.XPATH, self.budgetField)
        self.driver.execute_script("arguments[0].click();", budget)

    def budget_Min_Max(self):
        budgetMinSelect = self.driver.find_element(By.XPATH, self.selectMinValue)
        self.driver.execute_script("arguments[0].click();", budgetMinSelect)
        '''
        maxBudget = self.driver.find_element(By.ID, self.maxBudget)
        self.driver.execute_script("arguments[0].click();", maxBudget)
        '''
        budgetMaxSelect = self.driver.find_element(By.XPATH, self.selectMaxValue)
        self.driver.execute_script("arguments[0].click();", budgetMaxSelect)

    # Creating Element Methods for profreeAdlink

    def click(self):
        proAdLink = self.driver.find_element(By.LINK_TEXT, self.profreeAdLink)
        self.driver.execute_script("arguments[0].click();", proAdLink)

    # Creating Element Methods for commercial tab - lease / rent field

    def commercial_tab(self):
        commTab = self.driver.find_element(By.CSS_SELECTOR, self.Commercial)
        self.driver.execute_script("arguments[0].click();", commTab)

    def dropDownLR(self):
        dropdown = self.driver.find_element(By.ID, self.LRdropdown)
        self.driver.execute_script("arguments[0].click();", dropdown)
        self.driver.implicitly_wait(10)
        select_lr = self.driver.find_element(By.XPATH, self.selectBuy)
        self.driver.execute_script("arguments[0].click();", select_lr)