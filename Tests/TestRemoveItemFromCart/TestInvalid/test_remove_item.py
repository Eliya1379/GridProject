import pytest

from Pages.CheckOut.CheckOutPage import CheckOutPage
from Pages.ItemsPage import ItemsPage
from Pages.LoginPage import LoginPage
from Pages.Utilities.ReadFromXlsx import read_from_xlsx


@pytest.mark.usefixtures("BaseTest")
class TestItemToCart:
    @pytest.fixture(scope="class", autouse=True)
    def make_sure_the_cart_is_not_empty(self):
        ##################################
        # 1. verify user in connected , if not use in user default
        # 2. verify the cart have items , if not added same item from cart.
        ##################################
        itemPage = ItemsPage()

        # 1 ->
        if itemPage.verify_user_is_online() == False:
            user = read_from_xlsx("C:\\Users\\tkhvn\\PycharmProjects\\projectAutomation2\\Recourses\\userForTest.xlsx")[
                0]
            loginPage = LoginPage()
            loginPage.login(user['UserName'], user['Password'])
        # 2 - >
        itemPage.click_on_button_all_items()
        index = 1
        if itemPage.get_quantity_in_cart() == 0:
            itemPage.choose_item_by_index(index).add_to_cart()

        # return all items page
        itemPage.click_on_button_all_items()

    def test_remove_item_from_cart(self):
        ####################################
        # 1. choose some item and added to cart
        # 2. verify the count of cart is changed
        # 3. nav to cart page and make sure the item is founded
        ####################################

        checkOutPage = CheckOutPage()
        itemsPage = ItemsPage()

        # 1 ->
        quantity_before = itemsPage.get_quantity_in_cart()
        name_of_item = itemsPage.choose_item_by_index(1).get_name_item()
        itemsPage.choose_item_by_index(1).remove_from_cart()
        # 2 ->
        assert itemsPage.get_quantity_in_cart() == quantity_before - 1
        # 3 ->
        itemsPage.click_on_cart_button()
        assert checkOutPage.verify_item_in_cart(name_of_item) is False
