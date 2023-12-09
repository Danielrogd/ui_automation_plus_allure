import random

from selenium.webdriver.common.by import By


class FormPageLocators:
    FIRST_NAME = (By.XPATH, "//input[@id='firstName']")
    LAST_NAME = (By.XPATH, "//input[@id='lastName']")
    EMAIL = (By.XPATH, "//input[@id='userEmail']")
    GENDER = (By.XPATH, f"//label[@for='gender-radio-{random.randint(1,3)}']")
    MOBILE = (By.XPATH, "//input[@id='userNumber']")
    DATE_OF_BIRTH = (By.XPATH, "//input[@id='dateOfBirthInput']")
    SUBJECT = (By.XPATH, "//input[@id='subjectsInput']")
    SUBJECT_INPUTED = (By.XPATH,"//div[@class='css-12jo7m5 subjects-auto-complete__multi-value__label']")
    HOBBIES = (By.XPATH, f"//label[@for='hobbies-checkbox-{random.randint(1,3)}']")
    FILE_INPUT = (By.XPATH, "//input[@id='uploadPicture']")
    CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
    SELECT_STATE = (By.XPATH, "//div[@id='state']")
    STATE_INPUT = (By.XPATH, "//input[@id='react-select-3-input']")
    SELECT_CITY = (By.XPATH, "//div[@id='city']")
    CITY_INPUT = (By.XPATH, "//input[@id='react-select-4-input']")
    SUBMIT = (By.XPATH, "//button[@id='submit']")

    #table_results

    RESULT_TABLE = (By.XPATH, "//tbody//td[2]")

