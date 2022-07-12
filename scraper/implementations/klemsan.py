import time

from selenium.common.exceptions import TimeoutException

import core.drivers.driver_instance as driver_instance
from core.element_type.textbox import TextBox
from core.element_type.input_textbox import InputTextBox


def scrape_related_product(item):
    timeout_amount = 5
    result = "Error"
    URL = "https://www.klemsan.com.tr/home"

    try:
        driver_instance.DRIVER.get(URL)
        time.sleep(1)

        search_box = InputTextBox(xpath = "//input[@type=\"text\" and @ name=\"txtSearch\"]", timeout = timeout_amount)
        search_box.set_text(item)

        searched_data_textbox = TextBox(xpath = "//*[@id=\"divLiveSearchResult\"]/table/tbody/tr[1]/td[3]/a", timeout = timeout_amount)
        result = searched_data_textbox.get_text()

    except TimeoutException:
        result = "Error"
    
    return result
