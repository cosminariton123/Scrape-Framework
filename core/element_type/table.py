from config.default_driver_options import TIMEOUT
from core.element_type.row import Row
from core.element_type.webelement import WebElement


class Table(WebElement):
    def __init__(self, xpath, parent=None, timeout=TIMEOUT):
        super().__init__(
            xpath=xpath,
            parent=parent,
            timeout=timeout
        )

        self.rows = self.get_children(BaseClass=Row, timeout=2)

    def get_number_of_rows(self):
        return len(self.rows)
