from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from Pages.Utilities import BaseUtilitis


class Element(object):
    def __init__(self, by=By.XPATH, locator=None, waitToElement=10, element=None):
        self.by = by
        self.locator = locator
        self.driver = BaseUtilitis.driver
        if waitToElement != 10:
            self.wait = WebDriverWait(self.driver, waitToElement)
        else:
            self.wait = BaseUtilitis.wait
        self.element = element

    def getElement(self):
        element = self.wait.until(EC.visibility_of_element_located((self.by, self.locator)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def is_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located((self.by, self.locator)))
            return True
        except:
            return False

    def wait_for_disable(self):
        self.wait.until(EC.invisibility_of_element_located((self.by, self.locator)))

    def click(self):
        if self.element is not None:
            self.wait.until(EC.element_to_be_clickable(self.element)).click()
        else:
            self.getElement()
            self.wait.until(EC.element_to_be_clickable((self.by, self.locator))).click()

    def send_Keys(self, value, clear=True):
        ele = self.getElement()
        if clear:
            ele.clear()
        elif value is not None:
            ele.send_keys("\n")
        ele.send_keys(value)

    def number_Of_Elements_More_Than(self, number=0):
        self.wait.until(lambda driver: len(self.driver.find_elements(self.by, self.locator)) > number)
        return self.driver.find_elements(self.by, self.locator)

    def number_Of_Elements_Less_Than(self, number=2):
        self.wait.until(lambda driver: len(self.driver.find_elements(self.by, self.locator)) < number)
        return self.driver.find_elements(self.by, self.locator)

    def number_Of_Elements_To_Be(self, number=2):
        self.wait.until(lambda driver: len(self.driver.find_elements(self.by, self.locator)) == number)
        return self.driver.find_elements(self.by, self.locator)

    def get_text(self):
        return self.getElement().text

    def switch_to_iframe(self):
        self.driver.switch_to.default_content()
        self.wait.until(EC.frame_to_be_available_and_switch_to_it((self.by, self.locator)))

    def select_by_value(self, option):
        ele = Select(self.getElement())
        ele.select_by_value(option)
