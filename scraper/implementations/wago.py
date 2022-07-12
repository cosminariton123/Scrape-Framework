import time

from selenium.common.exceptions import TimeoutException

import core.drivers.driver_instance as driver_instance
from core.element_type.textbox import TextBox


def scrape_related_product(item):
    timeout_amount = 2

    result = "Error"

    URL = "https://www.wago.com/us/search?text=" + item

    try:
            
        driver_instance.DRIVER.get(URL)
        time.sleep(1)

        if driver_instance.DRIVER.is_element_visible(xpath = "//*[@class=\"wg-noresult-improve__headline\"]", timeout = timeout_amount) is False:
            part_number_text_box = TextBox(xpath = "//*[@class=\"wg-listitem-neo__breadcrumb-item\"][2]", timeout = timeout_amount)
            result = part_number_text_box.get_text()
            result = result[9:]
        else:
            result = "Error"

    except TimeoutException:
        result = "Error"

    return result
