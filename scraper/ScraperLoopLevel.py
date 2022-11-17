import time
from tqdm import tqdm

from scraper.ScraperLogic import scraper_logic
import core.drivers.driver_instance as driver_instance

def scraper_loop(id_curent_process, d, searched_items, delay = 0):

    results = dict()
    driver_instance.DRIVER = driver_instance.get_new_default_chrome_driver()

    for item in tqdm(searched_items):
        results[item] = scraper_logic(item)
        time.sleep(delay)

    driver_instance.DRIVER.quit()
    driver_instance.DRIVER = None
    d[id_curent_process] = results
    