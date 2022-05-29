from core.utils.wrappers import stale_element_reference_fix_loop, element_click_intercepted_fix_loop
import core.drivers.driver_instance as driver_instance

from config.default_driver_options import TIMEOUT
from core.element_type.webelement import WebElement


class TextBox(WebElement):
    def __init__(self, xpath, parent=None, timeout=TIMEOUT):
        super().__init__(
            xpath=xpath,
            parent=parent,
            timeout=timeout
        )

    @element_click_intercepted_fix_loop
    @stale_element_reference_fix_loop
    def get_text(self):
        self.scroll_into_view()
        found_text = self.element.text
        return found_text

    @element_click_intercepted_fix_loop
    @stale_element_reference_fix_loop
    def get_text_js(self):
        self.scroll_into_view()
        found_text = driver_instance.DRIVER.execute_script("arguments[0].value;", self.element)
        return found_text

    @element_click_intercepted_fix_loop
    @stale_element_reference_fix_loop
    def clear_text(self):
        self.scroll_into_view()
        self.element.clear()

    @element_click_intercepted_fix_loop
    @stale_element_reference_fix_loop
    def set_text(self, text):
        self.scroll_into_view()
        self.clear_text()
        self.element.send_keys(text)


