from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from config.default_driver_options import TIMEOUT

def GenericDriver(RealDriver):
    class GenericDriverClass(RealDriver):
        def __init__(self, executable_path, options=None):
            if options is not None:
                super().__init__(options=options,
                                 executable_path=executable_path)
            else:
                super().__init__(executable_path=executable_path)

        def wait(self, timeout):
            return WebDriverWait(self, timeout)

        def get(self, url, timeout=TIMEOUT):
            self.set_page_load_timeout(timeout)
            super().get(url)

        def get_elements_visible(self, xpath, timeout=TIMEOUT):
            return self.wait(timeout=timeout).until(ec.visibility_of_all_elements_located((By.XPATH, xpath)), message=xpath)

        def get_elements_invisible(self, xpath, timeout=TIMEOUT):
            return self.wait(timeout=timeout).until(ec.presence_of_all_elements_located((By.XPATH, xpath)), message=xpath)

        def get_number_of_elements_visible(self, xpath, timeout=TIMEOUT):
            try:
                return len(self.get_elements_visible(xpath=xpath, timeout=timeout))
            except TimeoutException:
                return 0

        def get_number_of_elements_invisible(self, xpath, timeout=TIMEOUT):
            try:
                return len(self.get_elements_invisible(xpath=xpath, timeout=timeout))
            except TimeoutException:
                return 0

        def get_element_visible(self, xpath, timeout=TIMEOUT):
            self._raise_exception_if_more_elements_are_present_with_same_xpath(xpath=xpath, timeout=timeout)
            return self.wait(timeout).until(ec.visibility_of_element_located((By.XPATH, xpath)), message=xpath)

        def get_element_invisible(self, xpath, timeout=TIMEOUT):
            self._raise_exception_if_more_elements_are_present_with_same_xpath(xpath=xpath, timeout=timeout)
            return self.wait(timeout).until(ec.presence_of_element_located((By.XPATH, xpath)), message=xpath)

        def get_element_clickable(self, xpath, timeout=TIMEOUT):
            self._raise_exception_if_more_elements_are_present_with_same_xpath(xpath=xpath, timeout=timeout)
            return self.wait(timeout).until(ec.element_to_be_clickable((By.XPATH, xpath)), message=xpath)

        def wait_for_element_to_become_invisible(self, xpath, timeout=TIMEOUT):
            self._raise_exception_if_more_elements_are_present_with_same_xpath(xpath=xpath, timeout=timeout)
            self.wait(timeout).until(ec.invisibility_of_element((By.XPATH, xpath)), message=xpath)

        def is_element_visible(self, xpath, timeout=TIMEOUT):
            try:
                self.get_element_visible(xpath=xpath, timeout=timeout)
                return True
            except TimeoutException:
                return False

        def is_element_clickable(self, xpath, timeout=TIMEOUT):
            try:
                self.get_element_clickable(xpath=xpath, timeout=timeout)
                return True
            except TimeoutException:
                return False

        def _raise_exception_if_more_elements_are_present_with_same_xpath(self, xpath, timeout=TIMEOUT):
            count = self.get_number_of_elements_invisible(xpath=xpath, timeout=timeout)
            if count > 1:
                raise ValueError(f"Given xpath: {xpath} has more than one element")

    return GenericDriverClass