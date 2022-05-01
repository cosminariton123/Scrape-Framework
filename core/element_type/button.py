

from config.default_driver_options import TIMEOUT
from core.element_type.webelement import WebElement
from core.utils.wrappers import stale_element_reference_fix_loop
import core.drivers.driver_instance as driver_instance


class Button(WebElement):
    def __init__(self, xpath, parent=None, timeout=TIMEOUT):

        if parent is None:
            self.xpath = xpath
        else:
            self.xpath = f"{parent.xpath}{xpath}"

        self.element = driver_instance.DRIVER.get_element_clickable(
            xpath=self.xpath,
            timeout=timeout
        )

    @stale_element_reference_fix_loop
    def click(self):
        self.scroll_into_view()
        self.element.click()

    @stale_element_reference_fix_loop
    def click_js(self):
        self.scroll_into_view()
        driver_instance.DRIVER.execute_script("arguments[0].click();", self.element)
