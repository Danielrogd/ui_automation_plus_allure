import time

from pages.form_page import FormPage


class TestForm:

    class TestFormPage:

        def test_form(self, driver):
            url = "https://demoqa.com/automation-practice-form"
            form_page = FormPage(driver, url)
            form_page.open()
            person_input = form_page.fill_form_fields()
            person_result = form_page.form_result()
            assert person_input == person_result, "The form has not been filled"


