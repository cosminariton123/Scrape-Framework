import time
import selenium

def scraper_logic(item, driver):

    result = None

    URL = "https://www.wago.com/us/search?text=" + item
    driver.get(URL)

    try:
        searched_data = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/section/div[3]/div[2]/div[2]/div/div[3]/div/div[1]/a/div[1]/div/span[2]")
        result = searched_data.text
            
    except selenium.common.exceptions.NoSuchElementException:
        result = "NotFoundException"

    return result