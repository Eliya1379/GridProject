import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from Pages.Utilities import BaseUtilitis


@pytest.fixture(scope="session")
def BaseTest(browser= "chrome"):
    # s = Service('./Drivers/chromedriver.exe')
    s = "sdf"
    BaseUtilitis.driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4444",
        desired_capabilities={"browserName": "chrome",
                              "video": "True"})
    # BaseUtilitis.driver = webdriver.Chrome("C:\\Users\\tkhvn\\PycharmProjects\\projectAutomation2\\Drivers\\chromedriver.exe")
    # BaseUtilitis.driver = webdriver.Chrome(service=s)

    txt = 'my new update'
    sd = "Fd"
    BaseUtilitis.driver.get("https://www.saucedemo.com/")
    BaseUtilitis.wait = WebDriverWait(BaseUtilitis.driver, 30)
    BaseUtilitis.action = ActionChains(BaseUtilitis.driver)
    BaseUtilitis.driver.maximize_window()
    # request.cls.driver = driver
    # request.cls.wait = wait
    # request.cls.action = action
    yield
    # BaseUtilitis.driver.close()
    # BaseUtilitis.driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store")


@pytest.fixture(scope="session")
def browser(pytestconfig):
    return pytestconfig.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")


def pytest_collection_modifyitems(items):
    """Modifies test items in place to ensure test classes run in a given order."""
    CLASS_ORDER = ["TestCreateIncidents", "TestLogin", "TestForgetPassword", "TestLoginInvalid"]
    class_mapping = {item: item.cls.__name__ for item in items}

    sorted_items = items.copy()
    # Iteratively move tests of each class to the end of the test queue
    for class_ in CLASS_ORDER:
        sorted_items = [it for it in sorted_items if class_mapping[it] != class_] + [
            it for it in sorted_items if class_mapping[it] == class_
        ]
    items[:] = sorted_items
