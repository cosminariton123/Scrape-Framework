import multiprocessing
import time

from scraper.ScraperLoopLevel import scraper_loop


def scraper(searched_items, delay = 0, delay_between_process_launches = 0, nr_of_processes = 5):

    with multiprocessing.Manager() as manager:
        d = manager.dict()

        i = 0
        j = unitate = len(searched_items)/ nr_of_processes
        jobs = []
        j = int(j)
        unitate = int(unitate)
        id_curent_process = 0

        while j <= len(searched_items) + 1:
            searched_items_curent_process = searched_items[i:j]
            p = multiprocessing.Process(target = scraper_loop, args=(id_curent_process, d, searched_items_curent_process, delay))
            id_curent_process += 1
            jobs.append(p)

            i += unitate
            j += unitate

        if i < len(searched_items) and j != len(searched_items) + 1:
            j = len(searched_items) + 1
            searched_items_curent_process = searched_items[i:j]
            p = multiprocessing.Process(target = scraper_loop, args=(id_curent_process, d, searched_items_curent_process, delay))
            id_curent_process += 1
            jobs.append(p)

        nr_of_processes = id_curent_process


        for job in jobs:
            job.start()

            if hasattr(delay_between_process_launches, "__next__"):
                time_to_sleep = next(delay_between_process_launches)
            else:
                time_to_sleep = delay_between_process_launches

            time.sleep(time_to_sleep)

        for job in jobs:
            job.join()
        

        aux = [d[id_process] for id_process in range(nr_of_processes)]
        
        
        found_data = dict()

        for dictionary in aux:
            for key, value in dictionary.items():
                found_data[key] = value 

    
    return found_data