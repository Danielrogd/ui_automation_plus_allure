import time

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage


class TestAlertFrameWindows:
    class TestBrowserWindowsPage():

        def test_new_tab(self, driver):
            url = "https://demoqa.com/browser-windows"
            browser_windows_page = BrowserWindowsPage(driver, url)
            browser_windows_page.open()
            text_check = browser_windows_page.check_new_tab()
            assert text_check == "This is a sample page", "New tab not open or incorrect was found"

        def test_new_window(self, driver):
            url = "https://demoqa.com/browser-windows"
            browser_windows_page = BrowserWindowsPage(driver, url)
            browser_windows_page.open()
            text_check = browser_windows_page.check_new_window()
            assert text_check == "This is a sample page", "New window not open or incorrect was found"

    class TestAlertsPage:

        def test_simple_alert(self, driver):
            url = "https://demoqa.com/alerts"
            alerts_page = AlertsPage(driver, url)
            alerts_page.open()
            check_alert_text = alerts_page.check_simple_alert()
            assert check_alert_text == "You clicked a button", "Alert does not open/found"

        def test_check_timer_5_sec_alert(self, driver):
            url = "https://demoqa.com/alerts"
            alerts_page = AlertsPage(driver, url)
            alerts_page.open()
            check_alert_text = alerts_page.check_timer_5_sec_alert()
            assert check_alert_text == "This alert appeared after 5 seconds", "Alert does not open/found"

        def test_check_confirm_alert(self, driver):
            url = "https://demoqa.com/alerts"
            alerts_page = AlertsPage(driver, url)
            alerts_page.open()
            check_alert_text = alerts_page.check_confirm_alert()
            assert check_alert_text == "You selected Ok", "Alert does not open/found"

        def test_check_promt_alert(self, driver):
            url = "https://demoqa.com/alerts"
            alerts_page = AlertsPage(driver, url)
            alerts_page.open()
            check_alert_text, text_promt = alerts_page.check_promt_alert()
            assert text_promt in check_alert_text, "Alert does not open/found"
