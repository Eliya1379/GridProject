import pytest

from Pages.CheckOut.CheckOutPage import CheckOutPage
from Pages.ItemsPage import ItemsPage
from Pages.LoginPage import LoginPage
from Pages.Utilities.ReadFromXlsx import read_from_xlsx


@pytest.mark.usefixtures("BaseTest")
class TestItemToCart:
    @pytest.fixture(scope="class", autouse=True)
    def make_sure_the_cart_have_items(self):
        #############################
        # 1. verify user in connected , if not use in user default
        # 2. get all items in cart , and verify the cart is not empty.
        # if the cart is empty add random item.
        # 3. nav to all items page
        #############################
        itemsPage = ItemsPage()
        # 1 ->
        if itemsPage.verify_user_is_online() == False:
            user = read_from_xlsx("C:\\Users\\tkhvn\\PycharmProjects\\projectAutomation2\\Recourses\\userForTest.xlsx")[
                0]
            loginPage = LoginPage()
            loginPage.login(user['UserName'], user['Password'])
        # return all items page
        itemsPage.click_on_button_all_items()

        # 2 ->
        if itemsPage.get_quantity_in_cart() == 0:
            itemsPage.choose_item_by_index(1).add_to_cart()

    def test_add_item_to_cart(self):
        ########################################
        # 1. navigate to checkOut page and save all items in cart
        # 2. return to all items page and add new items
        # 3. check if logo cart is changed
        # 4. navigate to checkout page and check if element in founded
        ########################################

        checkOutPage = CheckOutPage()
        itemsPage = ItemsPage()
        # 1 ->
        itemsPage.click_on_cart_button()
        itemsInCart = checkOutPage.get_items_in_cart()
        # 2 ->
        checkOutPage.click_on_button_all_items()
        name_of_item = "Sauce Labs Bike Light"
        itemsPage.choose_item_by_name(name_of_item).add_to_cart()
        # 3 ->
        assert itemsPage.get_quantity_in_cart() == len(itemsInCart) + 1
        # 4 ->
        itemsPage.click_on_cart_button()
        assert checkOutPage.verify_item_in_cart(name_of_item)
