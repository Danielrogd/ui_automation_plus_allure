import random
import time

from selenium.common import UnexpectedAlertPresentException, NoAlertPresentException

from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators, AlertsPageLocators
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


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_simple_alert(self):
        self.element_is_visible(self.locators.SIMPLE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_timer_5_sec_alert(self):
        self.element_is_visible(self.locators.TIMER_5_SEC_ALERT_BUTTON).click()
        time.sleep(6)
        try:
            alert_window = self.driver.switch_to.alert
            return alert_window.text
        except UnexpectedAlertPresentException:
            alert_window = self.driver.switch_to.alert
            return alert_window.text

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        text_result = self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_TEXT).text
        return text_result

    def check_promt_alert(self):
        text_promt = f'autotest {random.randint(1, 999)}'
        self.element_is_visible(self.locators.PROMT_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text_promt)
        alert_window.accept()
        text_result = self.element_is_visible(self.locators.PROMT_BOX_ALERT_TEXT).text
        return text_result, text_promt

