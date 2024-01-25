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


class DatePickerPageLocators:
    DATE_INPUT = (By.XPATH, "//input[@id='datePickerMonthYearInput']")
    DATE_SELECT_MONTH = (By.XPATH, "//select[@class='react-datepicker__month-select']")
    DATE_SELECT_YEAR = (By.XPATH, "//select[@class='react-datepicker__year-select']")
    DATE_SELECT_DAY_LIST = (By.XPATH, "//div[@class='react-datepicker__week']/div")

    DATE_TIME_INPUT = (By.XPATH, "//input[@id='dateAndTimePickerInput']")
    DATE_TIME_SELECT_MONTH = (By.XPATH, "//div[@class='react-datepicker__month-read-view']")
    DATE_TIME_SELECT_YEAR = (By.XPATH, "//div[@class='react-datepicker__year-read-view']")
    DATE_TIME_SELECT_DAY_LIST = (By.XPATH, "//div[@class='react-datepicker__week']/div")
    DATE_TIME_SELECT_TIME = (By.XPATH, "//li[@class='react-datepicker__time-list-item ']")
    DATE_TIME_SELECT_MONTH_LIST = (By.XPATH, "//div[@class='react-datepicker__month-option']")
    DATE_TIME_SELECT_YEAR_LIST = (By.XPATH, "//div[@class='react-datepicker__year-option']")


class SliderPageLocators:
    INPUT_SLIDER = (By.XPATH, "//input[@class='range-slider range-slider--primary']")
    SLIDER_VALUE = (By.XPATH, "//input[@id='sliderValue']")


class ProgressBarPageLocators:
    PROGRESS_BAR_BUTTON = (By.XPATH, "//button[@id='startStopButton']")
    PROGRESS_BAR_VALUE = (By.XPATH, "//div[@role='progressbar']")


class TabsPageLocators:
    TAB_WHAT = (By.XPATH, "//a[@id='demo-tab-what']")
    TAB_WHAT_CONTENT = (By.XPATH, "//div[@id='demo-tabpane-what']")
    TAB_ORIGIN = (By.XPATH, "//a[@id='demo-tab-origin']")
    TAB_ORIGIN_CONTENT = (By.XPATH, "//div[@id='demo-tabpane-origin']")
    TAB_USE = (By.XPATH, "//a[@id='demo-tab-use']")
    TAB_USE_CONTENT = (By.XPATH, "//div[@id='demo-tabpane-use']")
    TAB_MORE = (By.XPATH, "//a[@id='demo-tab-more']")
    TAB_MORE_CONTENT = (By.XPATH, "//div[@id='demo-tabpane-more']")


class ToolTipsPageLocators:
    TOOL_TIP_BTN = (By.XPATH, "//button[@id='toolTipButton']")
    TOOL_TIP_BTN_CHECK = (By.XPATH, "//button[@aria-describedby='buttonToolTip']")

    TOOL_TIP_TEXT_INPUT_FIELD = (By.XPATH, "//input[@id='toolTipTextField']")
    TOOL_TIP_TEXT_INPUT_FIELD_CHECK = (By.XPATH, "//input[@aria-describedby='textFieldToolTip']")

    TOOL_TIP_CONTRARY = (By.XPATH, "//a[text()='Contrary']")
    TOOL_TIP_CONTRARY_CHECK = (By.XPATH, "//a[@aria-describedby='contraryTexToolTip']")

    TOOL_TIP_DIGITS = (By.XPATH, "//a[text()='1.10.32']")
    TOOL_TIP_DIGITS_CHECK = (By.XPATH, "//a[@aria-describedby='sectionToolTip']")

    TOOL_TIPS_INNER = (By.XPATH, "//div[@class='tooltip-inner']")


class MenuPageLocators:
    MENU_ITEM_LIST = (By.XPATH, "//ul[@id='nav']//li")
