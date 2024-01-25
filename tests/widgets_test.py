import time

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage


class TestWidgets:
    class TestAccordianPage:

        def test_accordian_page(self, driver):
            url = "https://demoqa.com/accordian"
            accordian_page = AccordianPage(driver, url)
            accordian_page.open()
            first_section = accordian_page.check_accordian('first')
            second_section = accordian_page.check_accordian('second')
            third_section = accordian_page.check_accordian('third')
            assert first_section[0] == 'What is Lorem Ipsum?' and first_section[1] > 0
            assert second_section[0] == 'Where does it come from?' and second_section[1] > 0
            assert third_section[0] == 'Why do we use it?' and third_section[1] > 0

    class TestAutoCompletePage:

        def test_multi_auto_complete(self, driver):
            url = "https://demoqa.com/auto-complete"
            auto_complete_page = AutoCompletePage(driver, url)
            auto_complete_page.open()
            colors = auto_complete_page.fill_multi_input()
            colors_result = auto_complete_page.check_color_in_multi()
            assert colors_result == colors, "Color names didn`t inputed"

        def test_remove_auto_complete(self, driver):
            url = "https://demoqa.com/auto-complete"
            auto_complete_page = AutoCompletePage(driver, url)
            auto_complete_page.open()
            auto_complete_page.fill_multi_input()
            count_value_before, count_value_after = auto_complete_page.remove_value_from_multi()
            assert count_value_before != count_value_after, "Color didn`t removed"

        def test_single_auto_complete(self, driver):
            url = "https://demoqa.com/auto-complete"
            auto_complete_page = AutoCompletePage(driver, url)
            auto_complete_page.open()
            color = auto_complete_page.fill_single_input()
            color_result = auto_complete_page.check_color_in_single()
            assert color == color_result, "Color name didn`t inputed"


class TestDatePickerPage:

    def test_change_date(self, driver):
        url = "https://demoqa.com/date-picker"
        date_picker_page = DatePickerPage(driver, url)
        date_picker_page.open()
        date = date_picker_page.select_date()
        assert date[0] != date[1], "date has not been changed"

    def test_change_date_and_time(self, driver):
        url = "https://demoqa.com/date-picker"
        date_picker_page = DatePickerPage(driver, url)
        date_picker_page.open()
        date = date_picker_page.select_date_and_time()
        assert date[0] != date[1], "date and time has not been changed"


class TestSliderPage:
    def test_slider(self, driver):
        url = "https://demoqa.com/slider"
        slider_page = SliderPage(driver, url)
        slider_page.open()
        value_before, value_after = slider_page.change_slider_value()
        assert value_before != value_after, "Slider value did not changed"


class TestProgressBarPage:
    def test_progress_bar(self, driver):
        url = "https://demoqa.com/progress-bar"
        progress_bar_page = ProgressBarPage(driver, url)
        progress_bar_page.open()
        value_before, value_after = progress_bar_page.change_progress_bar_value()
        assert value_before != value_after, "Progress bar value did not changed"


class TestTabsPage:

    def test_tabs_page(self, driver):
        url = "https://demoqa.com/tabs"
        tabs_page = TabsPage(driver, url)
        tabs_page.open()
        what_button, what_content = tabs_page.check_tabs('what')
        origin_button, origin_content = tabs_page.check_tabs('origin')
        use_button, use_content = tabs_page.check_tabs('use')
        more_button, more_content = tabs_page.check_tabs('more')
        assert what_button == 'what' and what_content != 0, 'tab "what" was not pressed or text is missing'
        assert origin_button == 'origin' and origin_content != 0, 'tab "origin" was not pressed or text is missing'
        assert use_button == 'use' and use_content != 0, 'tab "use" was not pressed or text is missing'
        assert more_button == 'more' and more_content != 0, 'tab "more" was not pressed or text is missing'


class TestToolTipsPage:

    def test_tool_tip(self, driver):
        url = "https://demoqa.com/tool-tips"
        tool_tip_page = ToolTipsPage(driver, url)
        tool_tip_page.open()
        btn_text, field_text, contrary_text, digits_text = tool_tip_page.check_tool_tips()
        assert btn_text == 'You hovered over the Button', 'hover missing or incorrect content'
        assert field_text == 'You hovered over the text field', 'hover missing or incorrect content'
        assert contrary_text == 'You hovered over the Contrary', 'hover missing or incorrect content'
        assert digits_text == 'You hovered over the 1.10.32', 'hover missing or incorrect content'


class TestMenuPage:

    def test_menu(self,driver):
        url = "https://demoqa.com/menu"
        menu_page = MenuPage(driver, url)
        menu_page.open()
        result_list, check_list = menu_page.check_menu()
        assert result_list == check_list, 'hover missing or incorrect content'
