from config.default_driver_options import TIMEOUT
from config.default_driver_options import TABLE_CHILDREN_TIMEOUT
from core.element_type.row import Row
from core.element_type.webelement import WebElement


class Table(WebElement):
    def __init__(self, xpath, parent=None, timeout=TIMEOUT, table_children_timeout=TABLE_CHILDREN_TIMEOUT):
        super().__init__(
            xpath=xpath,
            parent=parent,
            timeout=timeout
        )

        self.rows = self.get_children(BaseClass=Row, timeout=table_children_timeout)

    def get_number_of_rows(self):
        return len(self.rows)
