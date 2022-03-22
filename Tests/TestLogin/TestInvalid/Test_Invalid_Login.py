import pytest

from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Pages.Utilities.ReadFromXlsx import read_from_xlsx


@pytest.mark.usefixtures("BaseTest")
class TestInvalid:

    @pytest.fixture(scope="function", autouse=True)
    def make_sure_user_disconnected(self):
        basePage = BasePage()
        if basePage.verify_user_is_online():
            basePage.log_out()

    @pytest.mark.parametrize("userDetails", read_from_xlsx("C:\\Users\\tkhvn\\PycharmProjects\\projectAutomation2\\Recourses\\userTest.xlsx"))
    def test_login_invalid(self, userDetails):
        basePage = BasePage()
        loginPage = LoginPage()
        loginPage.login(userDetails["UserName"], userDetails["Password"])
        assert basePage.verify_user_is_online() is False
        assert loginPage.get_error_message() == loginPage.get_error_message()
