from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Pages.CheckOut.checkOutInformation import checkOutInformation
from Pages.CheckOut.checkOutOverView import checkOutOverView
from Pages.Element import Element
from Pages.ItemPage import ItemPage
from Pages.Utilities.AllureReports import add_screen_shot


class CheckOutPage(BasePage, checkOutInformation, checkOutOverView):

    def __init__(self):
        BasePage.__init__(self)
        checkOutInformation.__init__(self)
        checkOutOverView.__init__(self)
        self.items_in_cart = Element(By.CLASS_NAME, "cart_item", waitToElement=4)
        self.check_out_button = Element(By.ID, "checkout")
        self.continue_shopping_button = Element(By.ID, "continue-shopping")
        self.check_out_is_complete = Element(By.ID, "checkout_complete_container", waitToElement=4)

    # return list of name's item
    def get_items_in_cart(self):
        try:
            all_items = self.items_in_cart.number_Of_Elements_More_Than(0)
            items_names = [ItemPage(item).get_name_item() for item in all_items]
            return items_names
        except:
            return []

    def choose_item(self, name):
        all_items = self.items_in_cart.number_Of_Elements_More_Than(0)
        for item in all_items:
            current_item = ItemPage(item)
            if current_item.get_name_item() == name:
                return current_item
        raise f"the item {name} not founded"

    def click_on_check_out(self):
        self.check_out_button.click()

    def verify_item_in_cart(self, item):
        if item in self.get_items_in_cart():
            add_screen_shot(f"{item} in cart")
            return True
        else:
            add_screen_shot(f"{item} not in cart")
            return False

    def click_on_continue_shopping(self):
        self.continue_shopping_button.click()

    def verify_item_is_deleted(self, previous_items, name_items_deleted):
        try:
            # wait for number of element is to be less from previous
            update_list_items = self.items_in_cart.number_Of_Elements_Less_Than(len(previous_items))
            update_items_name = [ItemPage(item).get_name_item() for item in update_list_items]
            # remove from previous list the item deleted
            previous_items.remove(name_items_deleted)
            if sorted(previous_items) == sorted(update_items_name):
                add_screen_shot(f"item {name_items_deleted} is deleted!")
                return True
            else:

                difference_between_two_list = set(previous_items) - set(update_items_name)
                difference_between_two_list += set(update_items_name) - set(previous_items)
                add_screen_shot(f"have difference items {difference_between_two_list} is deleted!")
                return False

        except:
            add_screen_shot("size of list is not changed!!!")
            return False

    def verify_checkout_is_success(self):
        return self.check_out_is_complete.is_visible()

    def verify_list_of_items_in_cart(self, list_items):
        ###########################
        # 1. check if don't have difference between two list
        # 2. if have a difference get the screen and add the difference
        ###########################
        current_items_in_cart = self.get_items_in_cart()
        if sorted(list_items) == sorted(current_items_in_cart):
            add_screen_shot(f"list {list_items} is founded!")
            return True
        else:
            items_not_founded = (current_items_in_cart - list_items) + (list_items - current_items_in_cart)
            add_screen_shot(f"the items is not founded {items_not_founded}")
            return items_not_founded
