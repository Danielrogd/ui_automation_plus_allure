import datetime
import os
import time

from selenium.webdriver import Keys

from generator.generator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators()

    def fill_form_fields(self):
        person = next(generated_person())
        file_name, path = generated_file()
        self.remove_footer()

        first_name = self.element_is_visible(self.locators.FIRST_NAME)
        first_name.send_keys(person.firstname)

        last_name = self.element_is_visible(self.locators.LAST_NAME)
        last_name.send_keys(person.lastname)

        email = self.element_is_visible(self.locators.EMAIL)
        email.send_keys(person.email)

        gender = self.element_is_visible(self.locators.GENDER)
        gender.click()

        mobile = self.element_is_visible(self.locators.MOBILE)
        mobile.send_keys(person.mobile)

        date_birth_row = self.element_is_visible(self.locators.DATE_OF_BIRTH)
        self.action_tripple_click(date_birth_row)
        date_birth_row.send_keys(person.date_birth)
        date_birth_row.send_keys(Keys.RETURN)

        subject = self.element_is_visible(self.locators.SUBJECT)
        subject.send_keys("Maths")
        subject.send_keys(Keys.RETURN)
        subjects = self.element_is_visible(self.locators.SUBJECT_INPUTED)

        hobbies = self.element_is_visible(self.locators.HOBBIES)
        hobbies.click()

        file_input = self.element_is_visible(self.locators.FILE_INPUT)
        file_input.send_keys(path)
        os.remove(path)

        current_address = self.element_is_visible(self.locators.CURRENT_ADDRESS)
        current_address.send_keys(person.current_address)

        state_status = self.element_is_visible(self.locators.SELECT_STATE)
        state_status.click()
        state_input = self.element_is_visible(self.locators.STATE_INPUT)
        state_input.send_keys(Keys.RETURN)

        city_status = self.element_is_visible(self.locators.SELECT_CITY)
        city_status.click()
        city_input = self.element_is_visible(self.locators.CITY_INPUT)
        city_input.send_keys(Keys.RETURN)

        self.element_is_visible(self.locators.SUBMIT).click()

        input_result_list = [
            first_name.get_attribute('value'),
            last_name.get_attribute('value'),
            email.get_attribute('value'),
            gender.text,
            mobile.get_attribute('value'),
            date_birth_row.get_attribute('value'),
            subjects.text,
            hobbies.text,
            file_input.get_attribute('value'),
            current_address.get_attribute('value'),
            state_status.text,
            city_status.text,
        ]

        return input_result_list

    def form_result(self):
        result_list = self.element_are_visible(self.locators.RESULT_TABLE)
        data = []
        for item in result_list:
            self.go_to_element(item)
            data.append(item.text)

        first_name, last_name = data[0].split(" ")
        data[0] = first_name
        data.insert(1, last_name)

        state_city = data[-1].split(" ")
        if len(state_city) == 3:
            state = " ".join(state_city[:2])
            city = state_city[-1]
        else:
            state = state_city[0]
            city = state_city[1]
        data.insert(-1, state)
        data[-1] = city

        date = data[5]
        formatted_date = datetime.datetime.strptime(date, "%d %B,%Y").strftime(
            "%d %b %Y")
        data[5] = formatted_date

        file_name = data[8]
        file_path = rf'C:\fakepath\{file_name}'
        data[8] = file_path

        return data
