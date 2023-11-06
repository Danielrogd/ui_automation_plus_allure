from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage
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

    class TestCheckBox:
        def test_check_box(self, driver):
            url = "https://demoqa.com/checkbox"
            check_box_page = CheckBoxPage(driver, url)
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            check_box_page.should_be_equal_checkbox_and_output(input_checkbox, output_result)
            time.sleep(5)

    class TestRadioButton:

        def test_radio_button(self, driver):
            url = "https://demoqa.com/radio-button"
            radio_button_page = RadioButtonPage(driver, url)
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', " 'Yes' is not selected"
            assert output_impressive == 'Impressive', " 'Impressive' is not selected"
            assert output_no == 'No', " 'No' is not selected"
