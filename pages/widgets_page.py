import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from generator.generator import generated_color
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators
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
