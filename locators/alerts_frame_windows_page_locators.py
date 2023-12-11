from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.XPATH, "//button[@id='tabButton']")
    NEW_WINDOW_BUTTON = (By.XPATH, "//button[@id='windowButton']")
    NEW_TAB_WINDOW_CHECK_TEXT = (By.XPATH, "//h1[@id='sampleHeading']")


class AlertsPageLocators:
    SIMPLE_ALERT_BUTTON = (By.XPATH, "//button[@id='alertButton']")
    TIMER_5_SEC_ALERT_BUTTON = (By.XPATH, "//button[@id='timerAlertButton']")
    CONFIRM_BOX_ALERT_BUTTON = (By.XPATH, "//button[@id='confirmButton']")
    CONFIRM_BOX_ALERT_TEXT = (By.XPATH, "//span[@id='confirmResult']")
    PROMT_BOX_ALERT_BUTTON = (By.XPATH, "//button[@id='promtButton']")
    PROMT_BOX_ALERT_TEXT = (By.XPATH, "//span[@id='promptResult']")


