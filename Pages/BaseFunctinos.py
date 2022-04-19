import re

from Pages.Utilities import BaseUtilitis
from selenium.webdriver.support import expected_conditions as EC


def switch_to_default_content():
    BaseUtilitis.driver.switch_to.default_content()


def get_current_url():
    return BaseUtilitis.driver.current_url


def switch_to_new_window():
    BaseUtilitis.wait.until(EC.number_of_windows_to_be(2))
    BaseUtilitis.driver.switch_to.window(BaseUtilitis.driver.window_handles[1])


def close_last_tab():
    if (len(BaseUtilitis.driver.window_handles) == 2):
        BaseUtilitis.driver.switch_to.window(window_name=BaseUtilitis.driver.window_handles[-1])
        BaseUtilitis.driver.close()
        BaseUtilitis.driver.switch_to.window(window_name=BaseUtilitis.driver.window_handles[0])


def get_double_from_str(value):
    final = value
    while type(final) != float:
        try:
            final = float(final)
        except:
            final = final[1::]
    return final
