from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinkPage
import time
import random

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


class TestWebTable:

    def test_web_table_add_person(self, driver):
        url = "https://demoqa.com/webtables"
        web_table_page = WebTablePage(driver, url)
        web_table_page.open()
        new_person = web_table_page.add_new_person()
        table_result = web_table_page.check_new_added_person()
        assert new_person in table_result

    def test_web_table_search_person(self, driver):
        url = "https://demoqa.com/webtables"
        web_table_page = WebTablePage(driver, url)
        web_table_page.open()
        key_word = web_table_page.add_new_person()[random.randint(0, 5)]
        web_table_page.search_some_person(key_word)
        table_result = web_table_page.check_search_person()
        print(key_word)
        print(table_result)
        assert key_word in table_result, "person didn`t found in the table "

    def test_web_table_update_person_info(self, driver):
        url = "https://demoqa.com/webtables"
        web_table_page = WebTablePage(driver, url)
        web_table_page.open()
        lastname = web_table_page.add_new_person()[1]
        web_table_page.search_some_person(lastname)
        age = web_table_page.update_person_info()
        row = web_table_page.check_search_person()
        assert age in row, f" Person card has not been changed. age:{age} is not found in row:{row}"

    def test_web_table_delete_person(self, driver):
        url = "https://demoqa.com/webtables"
        web_table_page = WebTablePage(driver, url)
        web_table_page.open()
        email = web_table_page.add_new_person()[3]
        web_table_page.search_some_person(email)
        web_table_page.delete_person()
        text = web_table_page.check_deleted()
        assert text == "No rows found"

    def test_web_table_change_count_of_rows(self, driver):
        url = "https://demoqa.com/webtables"
        web_table_page = WebTablePage(driver, url)
        web_table_page.open()
        web_table_page.change_count_of_rows()
        row_inputed = web_table_page.change_count_of_rows()[0]
        row_checked = web_table_page.change_count_of_rows()[1]
        assert row_inputed == row_checked, f"selected row count: {row_inputed} not equal checked row: {row_checked}"


class TestButtons:

    def test_different_click_on_buttons(self, driver):
        url = "https://demoqa.com/buttons"
        buttons_page = ButtonsPage(driver, url)
        buttons_page.open()
        buttons_page.double_click_me_btn()
        buttons_page.right_click_me_btn()
        buttons_page.left_click_me_btn()
        check_double_btn = buttons_page.check_double_click_me_btn()
        check_right_btn = buttons_page.check_right_click_me_btn()
        check_left_btn = buttons_page.check_left_click_me_btn()
        assert check_double_btn == "You have done a double click", "Double click button was not pressed"
        assert check_right_btn == "You have done a right click", "Right click button was not pressed"
        assert check_left_btn == "You have done a dynamic click", "Left (dynamic id) click button was not pressed"


class TestLink:

    def test_check_link(self, driver):
        url = "https://demoqa.com/links"
        link_page = LinkPage(driver, url)
        link_page.open()
        href_link, current_url = link_page.check_new_tab_simple_link()
        assert href_link == current_url, "Link is broken or url is incorrect"


    def tests_broken_link(self, driver):
        url = "https://demoqa.com/links"
        link_page = LinkPage(driver, url)
        link_page.open()
        response_code = link_page.check_broken_link("https://demoqa.com/bad-request")
        assert response_code == 400, "Link is working or status code is not 400"

