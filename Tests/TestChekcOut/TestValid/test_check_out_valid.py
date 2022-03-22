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
        if itemsPage.get_quantity_in_cart() == 0:
            itemsPage.choose_item_by_index(3).add_to_cart()

        # 2 ->
        itemsPage.click_on_cart_button()

    def test_check_out(self):
        checkOutPage = CheckOutPage()

        items_in_cart = checkOutPage.get_items_in_cart()
        checkOutPage.click_on_check_out()
        checkOutPage.set_checkout_information("Eliya", "Mazuz", "12345")
        checkOutPage.click_on_continue()
        assert checkOutPage.verify_list_of_items_in_cart_checkout_overview(items_in_cart)
        assert checkOutPage.verify_total_price(8) is True
        checkOutPage.click_on_finish()
        assert checkOutPage.verify_checkout_is_success() is True
