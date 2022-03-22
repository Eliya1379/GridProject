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

        itemsPage.click_on_button_all_items()
        # 1 ->
        if itemsPage.get_quantity_in_cart() == 0:
            itemsPage.choose_item_by_index(3).add_to_cart()

        # 2 ->
        itemsPage.click_on_cart_button()

    @pytest.fixture(scope="function", autouse=True)
    def return_to_all_items_page(self):
        checkOutPage = CheckOutPage()
        checkOutPage.click_on_button_all_items()
        checkOutPage.click_on_cart_button()

    @pytest.mark.parametrize('userDetails', read_from_xlsx(
        "C:\\Users\\tkhvn\\PycharmProjects\\projectAutomation2\\Recourses\\userDetailsCheckOut.xlsx"))
    def test_check_out_invalid_user_details(self, userDetails):
        checkOutPage = CheckOutPage()
        checkOutPage.click_on_check_out()
        checkOutPage.set_checkout_information(userDetails['FirstName'], userDetails['LastName'], userDetails['ZipCode'])
        checkOutPage.click_on_continue()
        assert checkOutPage.get_error_message() == userDetails['ErrorMessage']
