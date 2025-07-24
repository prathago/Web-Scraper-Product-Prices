import requests
from bs4 import BeautifulSoup
import re
import csv 
import logging

logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

HEADERS = {
    'User-Agent': 'Mozilla/5.0'
}

def cleanText(text):
    text = re.sub(r'\s+', ' ', text)  # remove extra whitespace
    text = re.sub(r'[^\w\s.,$]', '', text)  # remove special chars except dots, commas, and $
    return text.strip()

def cleanPrice(text):
    price_pattern = r"(?<!\w)(\$|₹|€|£)?\s?\d{1,5}(?:[\.,]\d{2})?"
    match = re.search(price_pattern, text.replace(',', ''))
    if match:
        return match.group().strip()
    return ""


def scrapePage(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'lxml')

        products = []
        items = soup.select('.product_pod')

        for item in items:
            name = item.h3.a['title']
            price = item.select_one('.price_color').text

            products.append({
                'name': cleanText(name),
                'price': cleanPrice(price)
            })

        return products

    except Exception as e:
        logging.error(f"Error scraping {url}: {e}")
        return []

def saveToCSV(data, filename='scraped_data.csv'):
    if not data:
        return
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    urls = [
        "http://books.toscrape.com/catalogue/category/books/travel_2/index.html",
        "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
        "https://books.toscrape.com/catalogue/category/books/business_35/index.html"
    ]
    all_data = []
    for url in urls:
        data = scrapePage(url)
        all_data.extend(data)

    saveToCSV(all_data)
    print(f"Scraped {len(all_data)} products.")
