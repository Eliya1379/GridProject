import allure
from selenium.webdriver.common.by import By

from Pages.Element import Element
from Pages.Utilities import BaseUtilitis
from Pages.Utilities.AllureReports import add_screen_shot


class BasePage:
    def __init__(self):
        self.cart_button = Element(By.ID, "shopping_cart_container")
        self.quantity_of_cart = Element(By.CLASS_NAME, "shopping_cart_badge", waitToElement=3)
        self.menu_button = Element(By.ID, "react-burger-menu-btn", waitToElement=3)
        self.menu_category = Element(By.CSS_SELECTOR, "[class = 'bm-item menu-item'][tabindex='0']")
        self.close_menu = Element(By.ID, "react-burger-cross-btn", waitToElement=3)

    def get_quantity_in_cart(self):
        try:
            return int(self.quantity_of_cart.get_text())
        except:
            return 0

    def click_on_cart_button(self):
        self.cart_button.click()

    def click_on_button_all_items(self):
        self.menu_button.click()
        Element(element=self.menu_category.number_Of_Elements_More_Than(0)[0]).click()
        # sometime menu is closed automaticlly
        try:
            self.close_menu.click()
        except:
            pass

    def click_on_about(self):
        self.menu_button.click()
        self.menu_category.number_Of_Elements_More_Than(0)[1].click()

    def log_out(self):
        self.menu_button.click()
        a = self.menu_category.number_Of_Elements_More_Than(0)
        Element(element=self.menu_category.number_Of_Elements_More_Than(0)[2]).click()

    def click_on_rest_app_state(self):
        self.menu_button.click()
        self.menu_category.number_Of_Elements_More_Than(0)[3].click()

    def verify_user_is_online(self):
        add_screen_shot("status user online")
        return self.menu_button.is_visible()
