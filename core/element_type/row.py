from config.default_driver_options import TIMEOUT
from core.element_type.textbox import TextBox
from core.element_type.webelement import WebElement
import core.drivers.driver_instance as driver_instance
from selenium.common.exceptions import TimeoutException

class Row(WebElement):
    def __init__(self, xpath, parent=None, timeout=TIMEOUT):

        if parent is None:
            self.xpath = xpath
        else:
            self.xpath = f"{parent.xpath}{xpath}"

        self.element = driver_instance.DRIVER.get_element_invisible(
            xpath=self.xpath,
            timeout=timeout
        )

    def check_if_text_present(self, text, timeout=TIMEOUT):
        try:
            TextBox(
                xpath=f"//*[contains(text(), \"{text}\")]",
                parent=self,
                timeout=timeout)

            return True

        except TimeoutException:
            return False

