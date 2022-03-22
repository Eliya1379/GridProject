import allure
from selenium.webdriver.common.by import By

from Pages.Element import Element
from Pages.Utilities.AllureReports import add_screen_shot


class checkOutInformation:
    def __init__(self):
        self.first_name = Element(By.ID, "first-name")
        self.last_name = Element(By.ID, "last-name")
        self.zip_code = Element(By.ID, "postal-code")
        self.error_message = Element(By.CSS_SELECTOR, "[data-test='error']", waitToElement=2)
        self.continue_button = Element(By.ID, "continue")
        self.cancel_button = Element(By.ID, "cancel")

    @allure.step
    def set_checkout_information(self, first_name_value, last_name_value, zip_code_value):
        self.first_name.send_Keys(first_name_value)
        self.last_name.send_Keys(last_name_value)
        self.zip_code.send_Keys(zip_code_value)

    def get_error_message(self):
        if self.error_message.is_visible():
            add_screen_shot("The Error Message")
            return self.error_message.get_text()
        else:
            add_screen_shot("Not have any Error message")
            return "There is no error message"

    def click_on_continue(self):
        self.continue_button.click()

    def click_on_cancel_button(self):
        self.cancel_button.click()
