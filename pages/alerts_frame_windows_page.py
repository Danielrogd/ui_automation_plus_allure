from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_new_tab(self):
        self.check_new_tab_window(self.locators.NEW_TAB_BUTTON)
        text_check = self.element_is_present(self.locators.NEW_TAB_WINDOW_CHECK_TEXT).text
        return text_check

    def check_new_window(self):
        self.check_new_tab_window(self.locators.NEW_WINDOW_BUTTON)
        text_check = self.element_is_present(self.locators.NEW_TAB_WINDOW_CHECK_TEXT).text
        return text_check
