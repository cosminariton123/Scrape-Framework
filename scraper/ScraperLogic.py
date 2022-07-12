import time

from selenium.common.exceptions import TimeoutException

from scraper.ScraperLogicUtils import delete_shadow_section_harting
import core.drivers.driver_instance as driver_instance
from core.element_type.textbox import TextBox
from core.element_type.button import Button
from core.element_type.table import Table
from core.element_type.input_textbox import InputTextBox

def scraper_logic(item):                #Aici e logica de scraper. Daca aveam un singur site, scriam direct aici
                                               #Cum avem 3, consideram functia drept interfata si implementam separat ca sa putem schimba
                                                #Implementarea dupa nevoie

    
    #from scraper.implementations import cabur
    #return cabur.scrape_related_product(item)

    #from scraper.implementations import harting
    #return harting.scrape_related_product(item)
    #return harting.scrape_description(item)
    
    #from scraper.implementations import klemsan
    #return klemsan.scrape_related_product(item)

    #from scraper.implementations import schnider
    #return schnider.scrape_related_product(item)

    #from scraper.implementations import te
    #return te.scrape_related_product(item)

    #from scraper.implementations import wago
    #return wago.scrape_related_product(item)

    from scraper.implementations import weidmueller
    return weidmueller.scrape_accessories(item)
    #return weidmueller.scrape_related_product(item)

