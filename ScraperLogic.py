import time
from selenium.webdriver.common.keys import Keys


def scraper_logic(item, driver):                #Aici e logica de scraper. Daca aveam un singur site, scriam direct aici
    #return scrape_wago(item, driver)           #Cum avem 3, consideram functia drept interfata si implementam separat ca sa putem schimba
    return scrape_harting(item, driver)        #Implementarea dupa nevoie
    #return scrape_schnider(item, driver)



def scrape_wago(item, driver):

    result = "Error"

    URL = "https://www.wago.com/us/search?text=" + item


    try:
        driver.get(URL)
        time.sleep(1)

        searched_data = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/section/div[3]/div[2]/div[2]/div/div[3]/div/div[1]/a/div[1]/div/span[2]")
        result = searched_data.text
            
    except :
        result = "Error"

    return result


def scrape_schnider(item, driver):
    result = "Error"

    URL = "https://tools.se.app/xref-overhaul/prod/index.html"


    try:
        driver.get(URL)
        time.sleep(1)

        input_field = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[3]/div[1]/div[2]/div/div/div/input")
        input_field.send_keys(item)

        search_button = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[3]/div[1]/div[3]/button")
        search_button.click()
        pass

        #result = searched_data.text
            
    except :
        result = "Error"

    return result



def scrape_harting(item, driver):
    
    result = "Error"

    URL = "https://b2b.harting.com/ebusiness/ro/"

    def delete_shadow_section(driver):
        shadow_section = driver.find_element_by_xpath("/html/body/div[6]")
        driver.execute_script("""
        var shadow_section = arguments[0];
        shadow_section.parentNode.removeChild(shadow_section);
        """, shadow_section)

    try:
        driver.get(URL)
        time.sleep(1)

        delete_shadow_section(driver)

        try:
            newsletter_x_button = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]")
            newsletter_x_button.click()
        except:
            pass

        magnifying_glass = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/header/div[2]/div[2]/span/div[1]/form/button")
        magnifying_glass.click()

        input_field = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/header/div[2]/div[2]/span/div[1]/form/input")
        input_field.click()
        input_field.send_keys(item)
        input_field.send_keys(Keys.ENTER)

        time.sleep(3)
        

        searched_data = driver.find_element_by_xpath("/html/body/div[1]/section[1]/div[2]/p[2]/b")
        result = searched_data.text
            
    except :
        result = "Error"

    return result
    