from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # form fields
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # created form
    CREATED_FULL_NAME = (By.XPATH, "//div[@id='output']//p[@id='name']")
    CREATED_EMAIL = (By.XPATH, "//div[@id='output']//p[@id='email']")
    CREATED_CURRENT_ADDRESS = (By.XPATH, "//div[@id='output']//p[@id='currentAddress']")
    CREATED_PERMANENT_ADDRESS = (By.XPATH, "//div[@id='output']//p[@id='permanentAddress']")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.XPATH, "//button[@class='rct-option rct-option-expand-all']")
    ITEM_LIST = (By.XPATH, "//span[@class='rct-title']")
    ALL_CLOSE_BTN = (By.XPATH, "//button[@class='rct-option rct-option-collapse-all']")
    CHECKED_ITEMS = (By.XPATH, "//*[name()='svg'][@class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    TEXT_SUCCESS = (By.XPATH, "//span[@class='text-success']")


class RadioButtonPageLocators:
    YES_RADIOBUTTON = (By.XPATH, "//label[@for='yesRadio']")
    IMPRESSIVE_RADIOBUTTON = (By.XPATH, "//label[@for='impressiveRadio']")
    NO_RADIOBUTTON = (By.XPATH, "//label[@for='noRadio']")
    TEXT_SUCCESS_OUTPUT = (By.XPATH, "//span[@class='text-success']")


class WebTablePageLocators:
    # add person form
    ADD_BUTTON = (By.XPATH, "//button[@id='addNewRecordButton']")
    FIRSTNAME_INPUT = (By.XPATH, "//input[@id='firstName']")
    LASTNAME_INPUT = (By.XPATH, "//input[@id='lastName']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='userEmail']")
    AGE_INPUT = (By.XPATH, "//input[@id='age']")
    SALARY_INPUT = (By.XPATH, "//input[@id='salary']")
    DEPARTMENT_INPUT = (By.XPATH, "//input[@id='department']")
    SUBMIT = (By.XPATH, "//button[@id='submit']")

    # table

    FULL_PEOPLE_LIST = (By.XPATH, "//div[@class='rt-tr-group']")
    SEARCH_INPUT = (By.XPATH, "//input[@id='searchBox']")
    DELETE_BUTTON = (By.XPATH, "//span[@title='Delete']")
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"
