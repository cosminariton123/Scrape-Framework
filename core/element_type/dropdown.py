from time import time
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

from config.default_driver_options import TIMEOUT, STALE_TIMEOUT, NUMBER_OF_TRIES_FOR_STALE_OBJECTS
from core.element_type.button import Button
from core.element_type.webelement import WebElement


class DropDown(WebElement):
    def __init__(self, xpath, drop_button, parent=None, timeout=TIMEOUT):
        self._xpath = xpath
        self._parent = parent
        self._timeout = timeout
        self.drop_button = drop_button

    def initialize(self):
        super().__init__(xpath=self._xpath, parent=self._parent, timeout=self._timeout)

    def select_by_text(self, text):
        self.drop_button.click()
        self.initialize()
        searched_button = Button(f"//*[text()= \"{text}\"]", parent=self, timeout=self._timeout)
        searched_button.scroll_into_view()

        ok = False
        for _ in range(NUMBER_OF_TRIES_FOR_STALE_OBJECTS):
            try:
                searched_button.element.click()
                ok = True
                break
            except StaleElementReferenceException:
                time.sleep(STALE_TIMEOUT)
                searched_button.refresh(timeout=self._timeout)
            except TimeoutException:
                self.drop_button.click()
                self.refresh(timeout=self._timeout)
                searched_button.refresh(timeout=self._timeout)

        if ok is False:
            searched_button.click()

    def select_by_text_js(self, text):
        self.drop_button.click_js()
        self.initialize()
        searched_button = Button(f"//*[text()= \"{text}\"]", parent=self, timeout=self._timeout)
        searched_button.click_js()

    def refresh(self, timeout=TIMEOUT):
        self.initialize()
