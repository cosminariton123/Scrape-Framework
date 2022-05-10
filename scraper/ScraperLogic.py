import time

from selenium.common.exceptions import TimeoutException

import core.drivers.driver_instance as driver_instance
from core.element_type.textbox import TextBox
from core.element_type.button import Button
from core.element_type.input_textbox import InputTextBox

def scraper_logic(item):                #Aici e logica de scraper. Daca aveam un singur site, scriam direct aici
                                               #Cum avem 3, consideram functia drept interfata si implementam separat ca sa putem schimba
                                                #Implementarea dupa nevoie

    #return scrape_wago(item)
    #return scrape_schnider(item)
    #return scrape_harting(item)
    #return scrape_harting_description(item)
    #return scrape_klemsan(item)
    #return scrape_te(item)
    return scrape_cabur(item)


def scrape_wago(item):
    timeout_amount = 2

    result = "Error"

    URL = "https://www.wago.com/us/search?text=" + item

    try:
            
        driver_instance.DRIVER.get(URL)

        if driver_instance.DRIVER.is_element_visible(xpath = "//*[@class=\"wg-noresult-improve__headline\"]", timeout = timeout_amount) is False:
            part_number_text_box = TextBox(xpath = "//*[@class=\"wg-listitem-neo__breadcrumb-item\"][2]", timeout = timeout_amount)
            result = part_number_text_box.get_text()
            result = result[9:]
        else:
            result = "Error"

    except TimeoutException:
        result = "Error"

    return result


def scrape_schnider(item):
    timeout_amount = 10

    result = "Error"
    URL = "https://tools.se.app/xref-overhaul/prod/index.html"

    try:
        driver_instance.DRIVER.get(URL)

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



def scrape_harting(item):
    timeout_amount = 10
    
    result = "Error"
    URL = "https://b2b.harting.com/ebusiness/ro/"

    def delete_shadow_section():
        shadow_section = driver_instance.DRIVER.find_element_by_xpath("/html/body/div[6]")
        driver_instance.DRIVER.execute_script("""
        var shadow_section = arguments[0];
        shadow_section.parentNode.removeChild(shadow_section);
        """, shadow_section)

    try:
        driver_instance.DRIVER.get(URL)
        time.sleep(1)

        delete_shadow_section()

        try:
            newsletter_window = Button(xpath = "//*[@class=\"popup popup--newsletter\"]", timeout = 4)

            newsletter_x_button = Button(xpath = "//*[@class=\"popup-close\"]", parent=newsletter_window , timeout = 1)
            newsletter_x_button.click()
        except:
            pass

        magnifying_glass = Button(xpath = "//*[@class=\"header-search__button\"]", timeout = timeout_amount)
        magnifying_glass.click()

        input_field =  InputTextBox(xpath = "//*[@id=\"header-search__input\"]", timeout = timeout_amount)
        input_field.search(text = item)


        side_bar = Button(xpath = "//*[@id=\"sideBarElement\"]", timeout = timeout_amount)
        searched_data = TextBox(xpath = "//*[@class=\"newPDP_sidebar__part\" and contains(text(), \"Part number\")]", parent = side_bar, timeout = 1)
        result = searched_data.get_text()
        result = result[13:]

    except TimeoutException:
        result = "Error"

    return result



def scrape_harting_description(item):
    timeout_amount = 10
    
    result = "Error"
    URL = "https://b2b.harting.com/ebusiness/ro/"

    def delete_shadow_section():
        shadow_section = driver_instance.DRIVER.find_element_by_xpath("/html/body/div[6]")
        driver_instance.DRIVER.execute_script("""
        var shadow_section = arguments[0];
        shadow_section.parentNode.removeChild(shadow_section);
        """, shadow_section)

    try:
        driver_instance.DRIVER.get(URL)
        time.sleep(1)

        delete_shadow_section()

        try:
            newsletter_window = Button(xpath = "//*[@class=\"popup popup--newsletter\"]", timeout = 4)

            newsletter_x_button = Button(xpath = "//*[@class=\"popup-close\"]", parent=newsletter_window , timeout = 1)
            newsletter_x_button.click()
        except:
            pass

        magnifying_glass = Button(xpath = "//*[@class=\"header-search__button\"]", timeout = timeout_amount)
        magnifying_glass.click()

        input_field =  InputTextBox(xpath = "//*[@id=\"header-search__input\"]", timeout = timeout_amount)
        input_field.search(text = item)


        side_bar = Button(xpath = "//*[@id=\"sideBarElement\"]", timeout = timeout_amount)
        searched_data = TextBox(xpath = "//*[@class=\"newPDP_sidebar__name\"]", parent = side_bar, timeout = 1)
        result = searched_data.get_text()

    except TimeoutException:
        result = "Error"

    return result
    


def scrape_klemsan(item):
    timeout_amount = 5
    result = "Error"
    URL = "https://www.klemsan.com.tr/home"

    try:
        driver_instance.DRIVER.get(URL)

        search_box = InputTextBox(xpath = "//input[@type=\"text\" and @ name=\"txtSearch\"]", timeout = timeout_amount)
        search_box.set_text(item)

        searched_data_textbox = TextBox(xpath = "//*[@id=\"divLiveSearchResult\"]/table/tbody/tr[1]/td[3]/a", timeout = timeout_amount)
        result = searched_data_textbox.get_text()

    except TimeoutException:
        result = "Error"
    
    return result



def scrape_te(item):
    timeout_amount = 5
    result = "Error"
    URL = "https://www.te.com/usa-en/product-" + item + ".html"

    try:
        driver_instance.DRIVER.get(URL)

        internal_description_box = Button(xpath = "//li[@class = \"product-description\"]")
        searched_data = TextBox(xpath = "//span[@class = \"part-basic-detail-value\"]", parent = internal_description_box, timeout = timeout_amount)
        result = searched_data.get_text()

    except TimeoutException:
        result = "Error"
        
    return result



def scrape_cabur(item):
    timeout_amount = 10
    result = "Error"
    URL = "http://www.cabur.it/?l=2"

    try:
        driver_instance.DRIVER.get(URL)
        
        search_input_textbox = InputTextBox(xpath = "//input[@type=\"text\" and @name=\"search\"]", timeout = timeout_amount)
        search_input_textbox.search(item)

        searched_data = TextBox(xpath = "//*[@id=\"leftcolumn\"]/table[1]/tbody[1]/tr[2]/td[3]", timeout = timeout_amount)
        result = searched_data.get_text()

    except TimeoutException:
        result = "Error"
    
    return result
