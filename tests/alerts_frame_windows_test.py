import time

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramePage, NestedFramePage


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

    class TestFramePage:

        def test_both_frames(self, driver):
            url = "https://demoqa.com/frames"
            frame_page = FramePage(driver, url)
            frame_page.open()
            frame_one_text = frame_page.check_frame("frame1")
            frame_two_text = frame_page.check_frame("frame2")
            check_assert_one_text = ['This is a sample page', '500px', '350px']
            check_assert_two_text = ['This is a sample page', '100px', '100px']
            assert frame_one_text == check_assert_one_text, "Frame not found"
            assert frame_two_text == check_assert_two_text, "Frame not found"

    class TestNestedFramesPage:

        def test_nested_frames(self, driver):
            url = "https://demoqa.com/nestedframes"
            nested_frame_page = NestedFramePage(driver, url)
            nested_frame_page.open()
            parent_frame, child_frame = nested_frame_page.nested_frame_check()
            assert parent_frame == "Parent frame", "Nested frame not found"
            assert child_frame == "Child Iframe", "Nested frame not found"
