import time

from selenium.common.exceptions import TimeoutException

import core.drivers.driver_instance as driver_instance
from core.element_type.textbox import TextBox
from core.element_type.input_textbox import InputTextBox

def scrape_related_product(item):
    timeout_amount = 10
    result = "Error"
    URL = "http://www.cabur.it/?l=2"

    try:
        driver_instance.DRIVER.get(URL)
        time.sleep(1)
        
        search_input_textbox = InputTextBox(xpath = "//input[@type=\"text\" and @name=\"search\"]", timeout = timeout_amount)
        search_input_textbox.search(item)

        searched_data = TextBox(xpath = "//*[@id=\"leftcolumn\"]/table[1]/tbody[1]/tr[2]/td[3]", timeout = timeout_amount)
        result = searched_data.get_text()

    except TimeoutException:
        result = "Error"
    
    return result
