from pages.alerts_frame_windows_page import BrowserWindowsPage


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
