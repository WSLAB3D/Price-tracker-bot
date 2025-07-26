import requests
from bs4 import BeautifulSoup

def scrape_coles(product_name):
    # Basic search scraping
    url = f"https://www.coles.com.au/search?q={product_name}"
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(r.text, "html.parser")
    title = soup.select_one("div[data-testid='product-tile-title']")
    price = soup.select_one("span[data-testid='product-tile-price']")
    return price.text.strip() if price else "N/A"

def scrape_woolies(product_name):
    url = f"https://www.woolworths.com.au/shop/search/products?searchTerm={product_name}"
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(r.text, "html.parser")
    title = soup.select_one("a.product-title")
    price = soup.select_one("span.price")
    return price.text.strip() if price else "N/A"