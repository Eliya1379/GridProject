import pytest

from Pages.CheckOut.CheckOutPage import CheckOutPage
from Pages.ItemsPage import ItemsPage
from Pages.LoginPage import LoginPage
from Pages.Utilities.ReadFromXlsx import read_from_xlsx


@pytest.mark.usefixtures("BaseTest")
class TestItemToCart:
    @pytest.fixture(scope="class", autouse=True)
    def make_sure_the_cart_is_empty(self):
        ##################################
        # 1. verify user in connected , if not use in user default
        # 2. verify the cart is empty , if not delete all item from cart.
        ##################################
        itemPage = ItemsPage()

        # 1 ->
        if itemPage.verify_user_is_online() == False:
            user = read_from_xlsx("C:\\Users\\tkhvn\\PycharmProjects\\projectAutomation2\\Recourses\\userForTest.xlsx")[
                0]
            loginPage = LoginPage()
            loginPage.login(user['UserName'], user['Password'])
        # 2 - >
        if itemPage.get_quantity_in_cart() > 0:
            itemPage.click_on_cart_button()
            checkOutPage = CheckOutPage()
            # get all items in cart and removed
            itemsInCart = checkOutPage.get_items_in_cart()
            checkOutPage.click_on_continue_shopping()
            # delete all item's from cart
            itemPage.remove_list_of_items(itemsInCart)

        # return all items page
        itemPage.click_on_button_all_items()

    def test_add_item_to_cart(self):
        ####################################
        # 1. choose some item and added to cart
        # 2. verify the count of cart is changed
        # 3. nav to cart page and make sure the item is founded
        ####################################

        checkOutPage = CheckOutPage()
        itemsPage = ItemsPage()

        # 1 ->
        itemsPage.add_items_by_index(1, 2, 3)
        name_of_item = "Sauce Labs Onesie"
        itemsPage.choose_item_by_name(name_of_item).add_to_cart()
        # 2 ->
        assert itemsPage.get_quantity_in_cart() == 1
        # 3 ->
        itemsPage.click_on_cart_button()
        assert checkOutPage.verify_item_in_cart(name_of_item)
