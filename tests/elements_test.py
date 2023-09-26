from pages.elements_page import TextBoxPage
import pytest
import time


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            url = "https://demoqa.com/text-box"
            text_box_page = TextBoxPage(driver, url)
            text_box_page.open()
            text_box_page.fill_all_fields()
            time.sleep(2)
            output_name, output_email, output_cur_addr, output_perm_addr = text_box_page.check_filled_form()
            print(output_name, output_email, output_cur_addr, output_perm_addr )
