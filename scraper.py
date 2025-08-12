import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}

def scrape_coles(product_name):
    url = f"https://www.coles.com.au/search?q={product_name}"
    try:
        r = requests.get(url, headers=HEADERS, timeout=5)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        title = soup.select_one("div[data-testid='product-tile-title']")
        price = soup.select_one("span[data-testid='product-tile-price']")
        return {
            "title": title.text.strip() if title else "Unknown",
            "price": price.text.strip() if price else "N/A"
        }
    except requests.RequestException as e:
        return {"title": "Error", "price": str(e)}

def scrape_woolies(product_name):
    url = f"https://www.woolworths.com.au/shop/search/products?searchTerm={product_name}"
    try:
        r = requests.get(url, headers=HEADERS, timeout=5)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        title = soup.select_one("a.product-title")
        price = soup.select_one("span.price")
        return {
            "title": title.text.strip() if title else "Unknown",
            "price": price.text.strip() if price else "N/A"
        }
    except requests.RequestException as e:
        return {"title": "Error", "price": str(e)}