import pytest

from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Pages.Utilities.ReadFromXlsx import read_from_xlsx


@pytest.mark.usefixtures("BaseTest")
class TestWithRegularUser:
    @pytest.fixture(scope="class", autouse=True)
    def make_sure_user_disconnected(self):
        basePage = BasePage()
        if basePage.verify_user_is_online():
            basePage.log_out()

    def test_login(self):
        user_for_login = \
        read_from_xlsx("C:\\Users\\tkhvn\\PycharmProjects\\projectAutomation2\\Recourses\\userForTest.xlsx")[
            0]
        loginPage = LoginPage()
        loginPage.login(user_for_login['UserName'], user_for_login['Password'])
        basePage = BasePage()
        assert basePage.verify_user_is_online()
