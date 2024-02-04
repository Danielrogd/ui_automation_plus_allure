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


class FramePageLocators:
    FIRST_FRAME = (By.XPATH, "//iframe[@id='frame1']")
    SECOND_FRAME = (By.XPATH, "//iframe[@id='frame2']")
    TEXT_IN_FRAME = (By.XPATH, "//h1[@id='sampleHeading']")
    FRAME_LOCATORS = {"frame1": FIRST_FRAME, "frame2": SECOND_FRAME}


class NestedFramePageLocators:
    PARENT_FRAME = (By.XPATH, "//iframe[@id='frame1']")
    CHILD_FRAME = (By.XPATH, "//iframe[@srcdoc]")
    PARENT_TEXT_IN_FRAME = (By.XPATH, "//body")
    CHILD_TEXT_IN_FRAME = (By.XPATH, "//p")


class ModalDialogPageLocators:
    SMALL_MODAL_BTN = (By.XPATH, "//button[@id='showSmallModal']")
    LARGE_MODAL_BTN = (By.XPATH, "//button[@id='showLargeModal']")
    SMALL_MODAL_TITLE = (By.XPATH, "//div[@id='example-modal-sizes-title-sm']")
    SMALL_MODAL_BODY = (By.XPATH, "//div[@class='modal-body']")
    LARGE_MODAL_TITLE = (By.XPATH, "//div[@id='example-modal-sizes-title-lg']")
    LARGE_MODAL_BODY = (By.XPATH, "//div[@class='modal-body']/p")
    CLOSE_SMALL_MODAL_BTN = (By.XPATH, "//button[@id='closeSmallModal']")
    CLOSE_LARGE_MODAL_BTN = (By.XPATH, "//button[@id='closeLargeModal']")
