from selenium.webdriver.common.by import By
import re

from Pages.BaseFunctinos import get_double_from_str
from Pages.Element import Element
from Pages.ItemPage import ItemPage
from Pages.Utilities.AllureReports import add_screen_shot


class checkOutOverView:
    def __init__(self):
        self.items_in_check_out = Element(By.CLASS_NAME, "cart_item")
        self.cancel_button = Element(By.ID, "cancel")
        self.finish_button = Element(By.ID, "finish")
        self.total_price_items = Element(By.CLASS_NAME, "summary_subtotal_label")
        self.tax_price_element = Element(By.CLASS_NAME, "summary_tax_label")
        self.total_price_element = Element(By.CLASS_NAME, "summary_total_label")

    def get_item_in_check_out_overview(self):
        all_items = self.items_in_check_out.number_Of_Elements_More_Than(0)
        items_names = [ItemPage(item).get_name_item() for item in all_items]
        return items_names

    def verify_total_price(self, tax):
        ############################
        # 1. check if total price is correct (sum price's item)
        # 2. check if tax price is correct
        # 3. check if total price's is correct( tax + total)
        ############################
        all_items = self.items_in_check_out.number_Of_Elements_More_Than(0)
        total_prices_items = sum([ItemPage(item).get_price_of_item() for item in all_items])
        flag = True
        # 1 check
        if total_prices_items == get_double_from_str(self.total_price_items.get_text()):
            add_screen_shot("sum of total price is correct")
        else:
            flag = False
            add_screen_shot(
                f"sum of total price is not correct ,  sum of total price is {total_prices_items} but write {self.total_price_items.get_text()}")

        # 2 check
        if round(total_prices_items * (tax / 100)) == round(get_double_from_str(self.tax_price_element.get_text())):
            add_screen_shot("tax is matched")

        else:
            flag = False
            add_screen_shot(
                f"tax is didn't match ,  expected to {tax} but actual {self.tax_price_element.get_text()}")

        # 3 check

        if get_double_from_str(self.total_price_element.get_text()) == (
                get_double_from_str(self.tax_price_element.get_text()) + total_prices_items):
            add_screen_shot("total prices is match!")
        else:
            add_screen_shot(
                f"total price's is not match expected to {tax + total_prices_items} , but actual {self.total_price_element.get_text()}")

        return flag

    def click_on_finish(self):
        self.finish_button.click()

    def click_on_cancel(self):
        self.cancel_button.click()

    def verify_list_of_items_in_cart_checkout_overview(self, list_items):
        ###########################
        # 1. check if don't have difference between two list
        # 2. if have a difference get the screen and add the difference
        ###########################
        current_items_in_cart = self.get_item_in_check_out_overview()
        if sorted(list_items) == sorted(current_items_in_cart):
            add_screen_shot(f"list {list_items} is founded!")
            return True
        else:
            items_not_founded = (current_items_in_cart - list_items) + (list_items - current_items_in_cart)
            add_screen_shot(f"the items is not founded {items_not_founded}")
            return items_not_founded
