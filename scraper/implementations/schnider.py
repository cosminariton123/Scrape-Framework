import time

from selenium.common.exceptions import TimeoutException

import core.drivers.driver_instance as driver_instance
from core.element_type.textbox import TextBox
from core.element_type.button import Button
from core.element_type.input_textbox import InputTextBox


def scrape_related_product(item):
    timeout_amount = 10

    result = "Error"
    URL = "https://tools.se.app/xref-overhaul/prod/index.html"

    try:
        driver_instance.DRIVER.get(URL)
        time.sleep(1)

        try:
            agree_button = Button(xpath = "//*[contains(text(), \"Agree\")]", timeout = 3)
            agree_button.click()
        except TimeoutException:
            pass

        
        input_field =  InputTextBox(xpath = "//*[@id=\"free-solo-with-text-demo\"]", timeout = timeout_amount)
        input_field.set_text(text = item)

        search_button = Button(xpath = "//button[@class=\"MuiButtonBase-root MuiButton-root MuiButton-contained isActivesearch\"]", timeout = timeout_amount)
        search_button.click()
        
        searched_data_text_box = TextBox(xpath = "//*[@id=\"table-to-xls\"]/tbody/tr[1]/td[3]/span", timeout = timeout_amount)
        searched_data = searched_data_text_box.get_text()

        if searched_data != "NO EQUAL":
            result = searched_data
            
    except TimeoutException:
        result = "Error"

    return result
