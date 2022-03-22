import pytest

from Pages.CheckOut.CheckOutPage import CheckOutPage
from Pages.ItemsPage import ItemsPage
from Pages.LoginPage import LoginPage
from Pages.Utilities.ReadFromXlsx import read_from_xlsx


@pytest.mark.usefixtures("BaseTest")
class TestRemoveAndAddSameItem:
    name_of_item = "Sauce Labs Onesie"

    @pytest.fixture(scope="class", autouse=True)
    def make_sure_same_item_in_cart(self):
        ##################################
        # 1. verify user in connected , if not use in user default
        # 2. verify the item 'name_of_item' exist in cart, if not add it.
        ##################################
        itemsPage = ItemsPage()

        # 1 ->
        if itemsPage.verify_user_is_online() is False:
            user = read_from_xlsx("C:\\Users\\tkhvn\\PycharmProjects\\projectAutomation2\\Recourses\\userForTest.xlsx")[
                0]
            loginPage = LoginPage()
            loginPage.login(user['UserName'], user['Password'])
        # 2 - >
        item_in_cart = False
        if itemsPage.get_quantity_in_cart() > 0:
            itemsPage.click_on_cart_button()
            checkOutPage = CheckOutPage()
            # verify item in cart
            item_in_cart = checkOutPage.verify_item_in_cart(self.name_of_item)
            checkOutPage.click_on_button_all_items()

        # if item not exist in cart add it
        if item_in_cart is False:
            itemsPage.choose_item_by_name(self.name_of_item).add_to_cart()

    def test_add_item_to_cart(self):
        ####################################
        # 1. save that all items before
        # 1. delete the item "name_of_item"
        # 3. add item "name_of_item"
        # 4. nav to cart page and make sure the item is founded and the cart have the same items before
        ####################################

        checkOutPage = CheckOutPage()
        itemsPage = ItemsPage()

        # 1 ->
        itemsPage.click_on_cart_button()
        items_in_cart_before = checkOutPage.get_items_in_cart()
        checkOutPage.click_on_continue_shopping()
        # 2 ->
        itemsPage.choose_item_by_name(self.name_of_item).remove_from_cart()
        # 3 ->
        itemsPage.choose_item_by_name(self.name_of_item).add_to_cart()
        # 4 ->
        assert itemsPage.get_quantity_in_cart() == len(items_in_cart_before)
        itemsPage.click_on_cart_button()
        assert checkOutPage.verify_list_of_items_in_cart(items_in_cart_before)
