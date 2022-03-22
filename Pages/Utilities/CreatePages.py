from Pages import BasePage
from Pages.Incidents.CreateIncidentsPage import CreateIncidentsPage
from Pages.Incidents.IncidentsPage import IncidentsPage
from Pages.LoginPage import LoginPage


class pages:
    def __init__(self):
        global loginPage
        global createIncidentsPage
        global incidentsPage
        global basePage

    def create_pages(self):
        self.loginPage = LoginPage()
        self.createIncidentsPage = CreateIncidentsPage()
        self.incidentsPage = IncidentsPage()
        self.basePage = BasePage()
