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
