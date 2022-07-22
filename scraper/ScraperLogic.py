def scraper_logic(item):                #Aici e logica de scraper. Daca aveam un singur site, scriam direct aici
                                               #Cum avem 3, consideram functia drept interfata si implementam separat ca sa putem schimba
                                                #Implementarea dupa nevoie

    
    #from scraper.implementations import cabur
    #return cabur.scrape_related_product(item)

    from scraper.implementations import harting
    return harting.scrape_related_product(item)
    #return harting.scrape_description(item)
    
    #from scraper.implementations import klemsan
    #return klemsan.scrape_related_product(item)

    #from scraper.implementations import schnider
    #return schnider.scrape_related_product(item)

    #from scraper.implementations import te
    #return te.scrape_related_product(item)

    #from scraper.implementations import wago
    #return wago.scrape_related_product(item)

    #from scraper.implementations import weidmueller
    #return weidmueller.scrape_accessories(item)
    #return weidmueller.scrape_related_product(item)

