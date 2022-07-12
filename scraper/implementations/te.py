import time

from selenium.common.exceptions import TimeoutException

import core.drivers.driver_instance as driver_instance
from core.element_type.textbox import TextBox
from core.element_type.button import Button


def scrape_related_product(item):
    timeout_amount = 10
    result = "Error"
    URL = "https://www.te.com/usa-en/product-" + item + ".html"

    try:
        driver_instance.DRIVER.get(URL)
        time.sleep(1)

        internal_description_box = Button(xpath = "//li[@class = \"product-description\"]", timeout = timeout_amount)
        searched_data = TextBox(xpath = "//span[@class = \"part-basic-detail-value\"]", parent = internal_description_box, timeout = timeout_amount)
        result = searched_data.get_text()

    except TimeoutException:
        result = "Error"
        
    return result
