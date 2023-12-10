from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=8):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_are_visible(self, locator, timeout=8):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=8):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_present(self, locator, timeout=8):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_are_present(self, locator, timeout=8):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_clickable(self, locator, timeout=8):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def should_be_equal_checkbox_and_output(self, checkbox, output):
        for item in checkbox:
            assert item in output, f" {item} checkbox is not in output text: {output}"

    def action_double_click(self, element):
        ActionChains(self.driver).double_click(element).perform()

    def action_right_click(self, element):
        ActionChains(self.driver).context_click(element).perform()

    def action_tripple_click(self, element):
        actions = ActionChains(self.driver)
        actions.double_click(element).click(element).perform()

    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementById('close-fixedban').remove();")

    def check_new_tab_window(self, locator):
        self.element_is_present(locator).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
