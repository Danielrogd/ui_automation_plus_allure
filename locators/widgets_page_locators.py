from selenium.webdriver.common.by import By


class AccordianPageLocators:
    FIRST_SECTION = (By.XPATH, "//div[@id='section1Heading']")
    SECOND_SECTION = (By.XPATH, "//div[@id='section2Heading']")
    THIRD_SECTION = (By.XPATH, "//div[@id='section3Heading']")
    FIRST_SECTION_TEXT = (By.XPATH, "//div[@id='section1Content']/p")
    SECOND_SECTION_TEXT = (By.XPATH, "//div[@id='section2Content']/p")
    THIRD_SECTION_TEXT = (By.XPATH, "//div[@id='section3Content']/p")

class AutoCompletePageLocators:
    MULTI_AUTO_COMPLETE_INPUT = (By.XPATH, "//input[@id='autoCompleteMultipleInput']")
    SINGLE_AUTO_COMPLETE_INPUT = (By.XPATH, "//input[@id='autoCompleteSingleInput']")
    MULTI_AUTO_COMPLETE_VALUE = (By.XPATH, "//div[@class='css-12jo7m5 auto-complete__multi-value__label']")
    SINGLE_AUTO_COMPLETE_VALUE = (By.XPATH, "//div[@class='auto-complete__single-value css-1uccc91-singleValue']")
    MULTI_REMOVE_BTN = (By.XPATH, "//div[@class='css-xb97g8 auto-complete__multi-value__remove']")