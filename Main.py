from selenium import webdriver
import os

from ScraperParalelizationLevel import scraper
from DataLoader import read_items
from DataDumper import save_results

def scrape_site():
    path = "Files"
    excel_input_filename = "Template.xlsx"
    
    options = webdriver.ChromeOptions()
    #options.add_argument("--incognito")
    options.add_argument("--headless")

    searched_items = read_items(os.path.join(path, excel_input_filename))

    aux = set(searched_items)
    if len(aux) != len(searched_items):
        print("Attention, duplicate items")
    aux = None

    results = scraper(searched_items, options = options, nr_of_processes = 15)

    save_results(results, path)

def main():
    scrape_site()

if __name__ == '__main__':
    main()