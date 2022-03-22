import pytest

from Pages.CheckOut.CheckOutPage import CheckOutPage
from Pages.ItemsPage import ItemsPage
from Pages.LoginPage import LoginPage
from Pages.Utilities.ReadFromXlsx import read_from_xlsx


@pytest.mark.usefixtures("BaseTest")
class TestCheckOutValid:

    @pytest.fixture(scope="class", autouse=True)
    def make_sure_cart_have_items(self):
        ##########################
        # 1. verify cart have items , if not have any item
        # 2. navigate to check out page
        #########################

        # create constructor
        itemsPage = ItemsPage()
        checkOutPage = CheckOutPage()

        if itemsPage.verify_user_is_online() == False:
            user = read_from_xlsx("C:\\Users\\tkhvn\\PycharmProjects\\projectAutomation2\\Recourses\\userForTest.xlsx")[
                0]
            loginPage = LoginPage()
            loginPage.login(user['UserName'], user['Password'])

        # 1 ->
        if itemsPage.get_quantity_in_cart() > 0:
            itemsPage.click_on_cart_button()
            all_items_in_cart = checkOutPage.get_items_in_cart()
            checkOutPage.click_on_button_all_items()
            itemsPage.remove_list_of_items(all_items_in_cart)

        # 2 ->
        itemsPage.click_on_cart_button()

    def test_check_out_invalid_user_details(self):
        checkOutPage = CheckOutPage()
        checkOutPage.click_on_check_out()
        assert checkOutPage.get_error_message() == "The cart is empty"
