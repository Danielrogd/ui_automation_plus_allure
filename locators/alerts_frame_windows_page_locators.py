from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:

    NEW_TAB_BUTTON = (By.XPATH, "//button[@id='tabButton']")
    NEW_WINDOW_BUTTON = (By.XPATH, "//button[@id='windowButton']")
    NEW_TAB_WINDOW_CHECK_TEXT = (By.XPATH, "//h1[@id='sampleHeading']")
