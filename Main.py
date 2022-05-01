import os
from matplotlib import pyplot as plt

from scraper.ScraperParalelizationLevel import scraper
from data_manipulation.DataLoader import read_items
from data_manipulation.DataDumper import save_results

from config.paths import INPUT_FILES_PATH, EXCEL_INPUT_FILENAME, OUTPUT_FILES_PATH
from config.other import NR_OF_PROCESSES

def scrape_site():


    searched_items = read_items(os.path.join(INPUT_FILES_PATH, EXCEL_INPUT_FILENAME))

    aux = set(searched_items)
    if len(aux) != len(searched_items):
        plt.title("Warning, duplicate items in given excel\nClose this window to continue")
        plt.show()
    aux = None

    results = scraper(searched_items, nr_of_processes = NR_OF_PROCESSES)

    save_results(results, OUTPUT_FILES_PATH)

def main():
    scrape_site()

if __name__ == '__main__':
    main()