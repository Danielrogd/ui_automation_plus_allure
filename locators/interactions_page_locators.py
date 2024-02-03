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


class ResizablePageLocators:
    HANDLE = "/span[@class='react-resizable-handle react-resizable-handle-se']"
    LIMIT = "//div[@id='resizableBoxWithRestriction']"
    NO_LIMIT = "//div[@id='resizable']"
    LIMIT_BOX = (By.XPATH, f"{LIMIT}")
    NO_LIMIT_BOX = (By.XPATH, f"{NO_LIMIT}")
    LIMIT_HANDLE = (By.XPATH, f"{LIMIT}{HANDLE}")
    NO_LIMIT_HANDLE = (By.XPATH, f"{NO_LIMIT}{HANDLE}")


class DroppablePageLocators:
    #Simple
    SIMPLE_TAB = (By.XPATH, "//a[@id='droppableExample-tab-simple']")
    DRAG_ME_SIMPLE = (By.XPATH, "//div[@class='simple-drop-container']/div[@id='draggable']")
    DROP_HERE_SIMPLE = (By.XPATH, "//div[@class='simple-drop-container']/div[@id='droppable']")

    #Accept
    ACCEPT_TAB = (By.XPATH, "//a[@id='droppableExample-tab-accept']")
    ACCEPTABLE = (By.XPATH, "//div[@class='accept-drop-container']//div[@id='acceptable']")
    NOT_ACCEPTABLE = (By.XPATH, "//div[@class='accept-drop-container']//div[@id='notAcceptable']")
    DROP_HERE_ACCEPT = (By.XPATH, "//div[@class='accept-drop-container']//div[@class='drop-box ui-droppable']")

    #Prevent propogation
    PREVENT_TAB = (By.XPATH, "//a[@id='droppableExample-tab-preventPropogation']")
    DRAG_ME_PREVENT = (By.XPATH, "//div[@class='pp-drop-container']/div[@id='dragBox']")
    DROP_HERE_PREVENT = (By.XPATH, "//div[@class='pp-drop-container']/div[@id='dragBox']")
    NOT_GREEDY_DROP_BOX_TEXT = (By.XPATH, "//div[@class='pp-drop-container']//div[@id='notGreedyDropBox']/p")
    NOT_GREEDY_INNER_BOX = (By.XPATH, "//div[@class='pp-drop-container']//div[@id='notGreedyInnerDropBox']")
    GREEDY_DROP_BOX_TEXT = (By.XPATH, "//div[@class='pp-drop-container']//div[@id='greedyDropBox']/p")
    GREEDY_INNER_BOX = (By.XPATH, "//div[@class='pp-drop-container']//div[@id='greedyDropBoxInner']")

    #Revert draggable
    REVERT_TAB = (By.XPATH, "//a[@id='droppableExample-tab-revertable']")
    WILL_REVERT = (By.XPATH, "//div[@class='revertable-drop-container']//div[@id='revertable']")
    NOT_REVERT = (By.XPATH, "//div[@class='revertable-drop-container']//div[@id='notRevertable']")
    DROP_REVERT = (By.XPATH, "//div[@class='revertable-drop-container']//div[@id='droppable']")


class DraggablePageLocators:
    #Simple
    SIMPLE_TAB = (By.XPATH, "//a[@id='draggableExample-tab-simple']")
    DRAG_ME = (By.XPATH, "//div[@id='dragBox']")

    #Axis restricted
    AXIS_TAB = (By.XPATH, "//a[@id='draggableExample-tab-axisRestriction']")
    ONLY_X = (By.XPATH, "//div[@id='restrictedX']")
    ONLY_Y = (By.XPATH, "//div[@id='restrictedY']")








