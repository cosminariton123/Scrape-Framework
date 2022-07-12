import time

from selenium.common.exceptions import TimeoutException

import core.drivers.driver_instance as driver_instance
from core.element_type.textbox import TextBox
from core.element_type.button import Button
from core.element_type.input_textbox import InputTextBox



def _delete_shadow_section_harting(driver_instance, timeout):
        shadow_section = driver_instance.DRIVER.get_element_invisible(xpath = "//*[@id=\"usercentrics-root\"]", timeout = timeout)
        driver_instance.DRIVER.execute_script("""
        var shadow_section = arguments[0];
        shadow_section.parentNode.removeChild(shadow_section);
        """, shadow_section)
        




def scrape_related_product(item):
    timeout_amount = 10
    
    result = "Error"
    URL = "https://b2b.harting.com/ebusiness/ro/"


    try:
        driver_instance.DRIVER.get(URL)
        time.sleep(1)

        _delete_shadow_section_harting(driver_instance = driver_instance, timeout = timeout_amount)

        try:
            newsletter_window = Button(xpath = "//*[@class=\"popup popup--newsletter\"]", timeout = 4)

            newsletter_x_button = Button(xpath = "//*[@class=\"popup-close\"]", parent=newsletter_window , timeout = 1)
            newsletter_x_button.click_js()
        except:
            pass

        magnifying_glass = Button(xpath = "//*[@class=\"header-search__button\"]", timeout = timeout_amount)
        magnifying_glass.click_js()

        input_field =  InputTextBox(xpath = "//*[@id=\"header-search__input\"]", timeout = timeout_amount)
        input_field.search(text = item)


        side_bar = Button(xpath = "//*[@id=\"sideBarElement\"]", timeout = timeout_amount)
        searched_data = TextBox(xpath = "//*[@class=\"newPDP_sidebar__part\" and contains(text(), \"Part number\")]", parent = side_bar, timeout = 1)
        result = searched_data.get_text()
        result = result[13:]

    except TimeoutException:
        result = "Error"

    return result



def scrape_description(item):
    timeout_amount = 10
    
    result = "Error"
    URL = "https://b2b.harting.com/ebusiness/ro/"


    try:
        driver_instance.DRIVER.get(URL)
        time.sleep(1)

        _delete_shadow_section_harting(driver_instance = driver_instance, timeout = timeout_amount)

        try:
            newsletter_window = Button(xpath = "//*[@class=\"popup popup--newsletter\"]", timeout = 4)

            newsletter_x_button = Button(xpath = "//*[@class=\"popup-close\"]", parent=newsletter_window , timeout = 1)
            newsletter_x_button.click_js()
        except:
            pass

        magnifying_glass = Button(xpath = "//*[@class=\"header-search__button\"]", timeout = timeout_amount)
        magnifying_glass.click_js()

        input_field =  InputTextBox(xpath = "//*[@id=\"header-search__input\"]", timeout = timeout_amount)
        input_field.search(text = item)


        side_bar = Button(xpath = "//*[@id=\"sideBarElement\"]", timeout = timeout_amount)
        searched_data = TextBox(xpath = "//*[@class=\"newPDP_sidebar__name\"]", parent = side_bar, timeout = 1)
        result = searched_data.get_text()

    except TimeoutException:
        result = "Error"

    return result
    
