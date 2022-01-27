import time
from selenium import webdriver
from tqdm import tqdm

from ScraperLogic import scraper_logic

def scraper_loop(id_curent_process, d, searched_items, close_reopen_driver= False, delay = 0, options = None):

    results = dict()
    driver = None
    if close_reopen_driver == False:
        driver = webdriver.Chrome(executable_path= 'chromedriver.exe', chrome_options = options)

    for item in tqdm(searched_items):

        if close_reopen_driver == True:
            driver = webdriver.Chrome(executable_path= 'chromedriver.exe', chrome_options = options)


        results[item] = scraper_logic(item, driver)

        time.sleep(delay)
        
        if close_reopen_driver == True:
            driver.quit()

    if close_reopen_driver == False:
        driver.quit()


    d[id_curent_process] = results