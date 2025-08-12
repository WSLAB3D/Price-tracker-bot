from scraper import scrape_coles, scrape_woolies
from storage import save_price

def scheduled_scrape(item, store):
    if store == "Coles":
        result = scrape_coles(item)
    else:
        result = scrape_woolies(item)

    save_price(item, store, result["price"])
    return result["price"]