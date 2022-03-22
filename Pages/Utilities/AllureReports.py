import allure
from allure_commons.types import AttachmentType

from Pages.Utilities import BaseUtilitis


def add_screen_shot(description="New screen shot"):
    screen = BaseUtilitis.driver.get_screenshot_as_png(),
    allure.attach(BaseUtilitis.driver.get_screenshot_as_png(), name=description, attachment_type=AttachmentType.PNG)


def description(description):
    allure.description("eliya")
