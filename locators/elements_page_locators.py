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
