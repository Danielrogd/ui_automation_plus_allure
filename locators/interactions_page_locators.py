from selenium.webdriver.common.by import By


class SortablePageLocators:
    TAB_LIST = (By.XPATH, "//a[@id='demo-tab-list']")
    LIST_ITEM = (By.XPATH, "//div[@class='vertical-list-container mt-4']/div")
    TAB_GRID = (By.XPATH, "//a[@id='demo-tab-grid']")
    GRID_ITEM = (By.XPATH, "//div[@class='grid-container mt-4']//div[@class='list-group-item list-group-item-action']")


class SelectablePageLocators:
    TAB_LIST = (By.XPATH, "//a[@id='demo-tab-list']")
    TAB_GRID = (By.XPATH, "//a[@id='demo-tab-grid']")
    TAB_LIST_ITEM = (By.XPATH, "//li[@class='mt-2 list-group-item list-group-item-action']")
    TAB_LIST_ITEM_ACTIVE = (By.XPATH, "//li[@class='mt-2 list-group-item active list-group-item-action']")
    TAB_GRID_ITEM = (By.XPATH, "//li[@class='list-group-item list-group-item-action']")
    TAB_GRID_ITEM_ACTIVE = (By.XPATH, "//li[@class='list-group-item active list-group-item-action']")
