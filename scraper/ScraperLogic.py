import time

from selenium.common.exceptions import TimeoutException

import core.drivers.driver_instance as driver_instance
from core.element_type.textbox import TextBox
from core.element_type.button import Button
from core.element_type.table import Table
from core.element_type.input_textbox import InputTextBox

def scraper_logic(item):

    #This is an example

    timeout_amount = 10
    result = "Error"
    URL = "https://www.bing.com/"

    try:
        driver_instance.DRIVER.get(URL)

        search_box = InputTextBox(xpath="//input[@id=\"sb_form_q\"]", timeout=timeout_amount)
        search_box.search(item)

        result_box = TextBox(xpath="//div[@id=\"d_ans\"]/div/div[1]/div/div[1]", timeout=timeout_amount)
        result = result_box.get_text()

    except TimeoutException:
        result = "Error"

    return result
