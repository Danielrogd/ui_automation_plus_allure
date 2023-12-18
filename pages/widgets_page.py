import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {
            'first': {'title': self.locators.FIRST_SECTION,
                      'content': self.locators.FIRST_SECTION_TEXT},
            'second': {'title': self.locators.SECOND_SECTION,
                       'content': self.locators.SECOND_SECTION_TEXT},
            'third': {'title': self.locators.THIRD_SECTION,
                      'content': self.locators.THIRD_SECTION_TEXT},
        }

        section_title = self.element_is_present(accordian[accordian_num]['title'])
        section_title.click()
        section_content = self.element_is_visible(accordian[accordian_num]['content'])
        return [section_title.text, len(section_content.text)]


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_multi_input(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        multi_input = self.element_is_visible(self.locators.MULTI_AUTO_COMPLETE_INPUT)
        for color in colors:
            multi_input.send_keys(color)
            multi_input.send_keys(Keys.RETURN)
        return colors

    def remove_value_from_multi(self):
        count_value_before = len(self.element_are_present(self.locators.MULTI_AUTO_COMPLETE_VALUE))
        remove_btn_list = self.element_are_present(self.locators.MULTI_REMOVE_BTN)
        for value in remove_btn_list:
            value.click()
            break
        count_value_after = len(self.element_are_present(self.locators.MULTI_AUTO_COMPLETE_VALUE))
        return count_value_before, count_value_after

    def check_color_in_multi(self):
        color_list = self.element_are_present(self.locators.MULTI_AUTO_COMPLETE_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_single_input(self):
        single_input_text = random.sample(next(generated_color()).color_name, k=1)
        single_input = self.element_is_visible(self.locators.SINGLE_AUTO_COMPLETE_INPUT)
        single_input.send_keys(single_input_text)
        single_input.send_keys(Keys.RETURN)
        return single_input_text

    def check_color_in_single(self):
        single_value = self.element_is_visible(self.locators.SINGLE_AUTO_COMPLETE_VALUE)
        return [single_value.text]


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_day_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return [value_date_before, value_date_after]

    def select_date_and_time(self):
        date = next(generated_date())
        date_year = '2020'
        input_date = self.element_is_visible(self.locators.DATE_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_visible(self.locators.DATE_TIME_SELECT_MONTH).click()
        self.set_day_from_list(self.locators.DATE_TIME_SELECT_MONTH_LIST, date.month)
        self.element_is_visible(self.locators.DATE_TIME_SELECT_YEAR).click()
        self.set_day_from_list(self.locators.DATE_TIME_SELECT_YEAR_LIST, date_year)
        self.set_day_from_list(self.locators.DATE_TIME_SELECT_DAY_LIST, date.day)
        self.set_day_from_list(self.locators.DATE_TIME_SELECT_TIME, date.time)
        input_date_after = self.element_is_visible(self.locators.DATE_TIME_INPUT)
        value_date_after = input_date_after.get_attribute('value')
        return [value_date_before, value_date_after]

    def set_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def set_day_from_list(self, elements, value):
        day_list = self.element_are_present(elements)
        for day in day_list:
            if day.text == value:
                day.click()
                break
