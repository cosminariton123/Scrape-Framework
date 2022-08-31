import time

from selenium.common.exceptions import TimeoutException

import core.drivers.driver_instance as driver_instance
from core.element_type.textbox import TextBox
from core.element_type.button import Button
from core.element_type.table import Table


def scrape_related_products(item):
    timeout_amount = 10
    result = "Error"
    URL = "https://catalog.weidmueller.com/catalog/Start.do;jsessionid=5E9D8162E7FEAFD88246FD0436A48039?ObjectID=" + str(item) + "&page=Product"

    try:
        driver_instance.DRIVER.get(URL)

        related_products_button = Button(xpath = "//*[@id=\"SimilarProducts\"]", timeout = timeout_amount)
        related_products_button.click()

        related_PN_products_table = Table(xpath = "//div[@id=\"SimilarProductsDiv\"]//div[@class=\"ProductInfoWrapper\"]", timeout = timeout_amount, table_children_timeout = 2)
        
        result = ""
        for child in related_PN_products_table.rows:
            part_number_textbox = TextBox(xpath = "//span[@class=\"listAttributeValue products.BaseProduct.bestNr\"]", parent = child, timeout = timeout_amount)
            result += part_number_textbox.get_text() + ","
        
        if result == "":
            result = "Error"

        result = result[:-1]

    except TimeoutException:
        result = "Error"

    return result


def scrape_accessories(item):
    timeout_amount = 10
    result = "Error"
    URL = "https://catalog.weidmueller.com/catalog/Start.do;jsessionid=5E9D8162E7FEAFD88246FD0436A48039?ObjectID=" + str(item) + "&page=Product"

    try:
        driver_instance.DRIVER.get(URL)
        time.sleep(1)

        accesories_products_button = Button(xpath = "//*[@id=\"accessoryList\"]", timeout = timeout_amount)
        accesories_products_button.click()

        accesories_list_group = Table(xpath = "//*[@id=\"accessoryListDiv\"]", timeout = timeout_amount, table_children_timeout = 2)

        result = ""
        for group in accesories_list_group.rows:   
            accesories_group_products_table = Table(xpath = "/table/tbody/tr/td", parent=group, timeout = 0.1, table_children_timeout = 0.2)
            accesories_group_products_table.rows = accesories_group_products_table.rows[1:]

            for subgroup in accesories_group_products_table.rows:
            
                subgroup_wrapper = Table(xpath = "//div[@class=\"ProductInfoWrapper\"]", parent = subgroup, timeout = timeout_amount, table_children_timeout=0.1)
    
                for product in subgroup_wrapper.rows:
                    part_number_textbox = TextBox(xpath = "//span[@class=\"listAttributeValue products.BaseProduct.bestNr\"]", parent = product, timeout = timeout_amount)
                    result += part_number_textbox.get_text() + ","
        
        if result == "":
            result = "Error"
        else:
            result = result[:-1]

    except TimeoutException:
        result = "Error"

    return result
