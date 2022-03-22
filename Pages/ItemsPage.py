from selenium.webdriver.common.by import By
import allure
from Pages.BasePage import BasePage
from Pages.Element import Element
from Pages.ItemPage import ItemPage
from Pages.Utilities.AllureReports import add_screen_shot


class ItemsPage(BasePage):
    def __init__(self):
        BasePage.__init__(self)
        self.items = Element(By.CLASS_NAME, "inventory_item")
        self.sort_button = Element(By.CLASS_NAME, "product_sort_container")

        correct_item = None
        # get all items

    def choose_item_by_name(self, name) -> ItemPage:
        list_of_items = self.items.number_Of_Elements_More_Than()
        # found the correct item
        for item in list_of_items:
            # create constractor of the correct item
            correct_item = ItemPage(item)
            if correct_item.get_name_item() == name:
                break
            # restart the correct_item because the current item is not matched
            correct_item = None
        return correct_item

    def choose_item_by_index(self, index):
        correct_item = None
        # get all items
        list_of_items = self.items.number_Of_Elements_More_Than()
        # create constractor of the correct item
        correct_item = ItemPage(list_of_items[index - 1])
        return correct_item

    def choose_item_by_index(self, *args):
        correct_item = None
        # get all items
        for index in args:
            list_of_items = self.items.number_Of_Elements_More_Than()
            # create constractor of the correct item
            correct_item = ItemPage(list_of_items[index - 1])
            yield correct_item

    def add_items_by_index(self, *args):
        for index in args:
            list_of_items = self.items.number_Of_Elements_More_Than()
            # create constractor of the correct item
            correct_item = ItemPage(list_of_items[index - 1])
            correct_item.add_to_cart()

    @allure.step
    def sort_by(self, value):
        self.sort_button.select_by_value(value)

    def varify_sort(self, value):
        items_list = self.items.number_Of_Elements_More_Than(0)
        flag = True

        if value == "Name (A to Z)":
            previous_name = ItemPage(items_list[0]).get_name_item()
            # pass on all items and check if name order by A-Z
            for index in range(len(items_list - 1)):
                current_name = ItemPage(items_list[index]).get_name_item()
                if ItemPage(items_list[index]).get_name_item() < previous_name:
                    flag = False
                    break
                previous_name = current_name

        elif value == "Name (Z to A)":
            previous_name = ItemPage(items_list[0]).get_name_item()
            # pass on all items and check if name order by Z-A
            for index in range(len(items_list - 1)):
                current_name = ItemPage(items_list[index]).get_name_item()
                if ItemPage(items_list[index]).get_name_item() > previous_name:
                    flag = False
                    break
                previous_name = current_name

        elif value == "Price (low to high)":
            previous_price = ItemPage(items_list[0]).get_price_of_item()
            # check's if items is order from low to high
            for index in range(len(items_list - 1)):
                current_price = ItemPage(items_list[index]).get_price_of_item()
                if current_price < previous_price:
                    flag = False
                    break
                previous_price = current_price

        elif value == "Price (high to low)":
            previous_price = ItemPage(items_list[0]).get_price_of_item()
            # check's if items is order from high to low
            for index in range(len(items_list - 1)):
                current_price = ItemPage(items_list[index]).get_price_of_item()
                if current_price > previous_price:
                    flag = False
                    break
                previous_price = current_price

        add_screen_shot(f"order by value {value} is success : {flag}")
        return flag

    def remove_list_of_items(self, list_items):
        for item in list_items:
            self.choose_item_by_name(item).remove_from_cart()
