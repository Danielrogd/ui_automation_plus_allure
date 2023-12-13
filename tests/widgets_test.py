from pages.widgets_page import AccordianPage


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
