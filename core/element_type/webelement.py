from selenium.common.exceptions import TimeoutException
from config.default_driver_options import TIMEOUT
from config.other import INF
from core.utils.wrappers import stale_element_reference_fix_loop, element_click_intercepted_fix_loop
import core.drivers.driver_instance as driver_instance
from abc import ABC, abstractmethod


class WebElement(ABC):
    @abstractmethod
    def __init__(self, xpath, parent=None, timeout=TIMEOUT):

        if parent is None:
            self.xpath = xpath
        else:
            self.xpath = f"{parent.xpath}{xpath}"

        self.element = driver_instance.DRIVER.get_element_visible(
            xpath=self.xpath,
            timeout=timeout
        )

    def refresh(self, timeout=TIMEOUT):
        self.__init__(xpath=self.xpath, parent=None, timeout=timeout)

    @element_click_intercepted_fix_loop
    @stale_element_reference_fix_loop
    def scroll_into_view(self):
        driver_instance.DRIVER.execute_script("arguments[0].scrollIntoView();", self.element)

    def get_children(self, BaseClass, timeout=TIMEOUT):
        children = list()
        for idx in range(1, INF):
            try:
                current_element = BaseClass(
                    xpath=f"/*[{idx}]",
                    parent=self,
                    timeout=timeout)

                current_element.scroll_into_view()
                children.append(current_element)
            except TimeoutException:
                break

        return children
