from selenium.common.exceptions import StaleElementReferenceException

from config.default_driver_options import TIMEOUT, NUMBER_OF_TRIES_FOR_STALE_OBJECTS, STALE_TIMEOUT
from core.element_type.textbox import TextBox
from selenium.webdriver.common.keys import Keys

from core.utils.wrappers import stale_element_reference_fix_loop, element_click_intercepted_fix_loop


class InputTextBox(TextBox):
    def __init__(self, xpath, parent=None, timeout=TIMEOUT):
        super().__init__(
            xpath=xpath,
            parent=parent,
            timeout=timeout
        )

    def send_input(self):

        ok = False
        for i in range(NUMBER_OF_TRIES_FOR_STALE_OBJECTS):
            try:
                self.scroll_into_view()
                self.element.send_keys(Keys.ENTER)
                ok = True
                break
            except StaleElementReferenceException:
                self.refresh(timeout=STALE_TIMEOUT)

        if ok is False:
            self.scroll_into_view()
            self.element.send_keys(Keys.ENTER)

    @element_click_intercepted_fix_loop
    @stale_element_reference_fix_loop
    def search(self, text):
        self.scroll_into_view()
        self.set_text(text)
        self.send_input()

