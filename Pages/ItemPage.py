from selenium.webdriver.common.by import By

from Pages.BaseFunctinos import get_double_from_str
from Pages.Utilities.AllureReports import add_screen_shot


class ItemPage(object):
    def __init__(self, item_element):
        self.item_element = item_element
        self.add_to_cart_button = (By.TAG_NAME, "button")
        self.remove_from_cart_button = (By.TAG_NAME, "button")
        self.price_of_element = (By.CLASS_NAME, "inventory_item_price")
        self.name_of_item = (By.CLASS_NAME, "inventory_item_name")

    def get_name_item(self):
        return self.item_element.find_element(self.name_of_item[0], self.name_of_item[1]).text

    def add_to_cart(self):
        self.item_element.find_element(self.add_to_cart_button[0], self.add_to_cart_button[1]).click()
        add_screen_shot(f"item {self.get_name_item()} added to cart")

    def remove_from_cart(self):
        self.item_element.find_element(self.remove_from_cart_button[0], self.remove_from_cart_button[1]).click()
        add_screen_shot(f"item {self.get_name_item()} removed to cart")

    def get_price_of_item(self):
        price = self.item_element.find_element(self.price_of_element[0], self.price_of_element[1]).text
        return float(get_double_from_str(price))
