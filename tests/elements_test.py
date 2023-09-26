from pages.elements_page import TextBoxPage
import pytest
import time


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            url = "https://demoqa.com/text-box"
            text_box_page = TextBoxPage(driver, url)
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            time.sleep(2)
            output_name, output_email, output_cur_addr, output_perm_addr = text_box_page.check_filled_form()
            assert full_name == output_name, "full name does not match to output name"
            assert email == output_email, "email does not match to output email"
            assert current_address == output_cur_addr, "current address does not match to output_current address"
            assert permanent_address == output_perm_addr, "permanent address does not match to output permanent address"
