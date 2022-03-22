import allure
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Pages.Element import Element
from Pages.Utilities.AllureReports import add_screen_shot


class LoginPage:
    def __init__(self):
        self.user_name = Element(By.ID, "user-name")
        self.password = Element(By.ID, "password")
        self.button_login = Element(By.ID, "login-button")
        self.error_message = Element(By.CSS_SELECTOR, "[data-test='error']")

    @allure.step
    def login(self, user_name_value=None, password_value=None):
        self.user_name.send_Keys(user_name_value)
        self.password.send_Keys(password_value)
        self.button_login.click()

    def get_error_message(self):
        try:
            error = self.error_message.get_text()
            add_screen_shot(f"The error message : {error}")
        except:
            add_screen_shot("The error message :Don't any error message")
            return "Don't any error message"
