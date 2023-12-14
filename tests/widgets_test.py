import time

from pages.widgets_page import AccordianPage, AutoCompletePage


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
