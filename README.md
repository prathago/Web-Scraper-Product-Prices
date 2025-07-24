# Product Price Web Scraper

## Objective
To build a script that automnatically extracts product information (such as name and price) from e-commerce websites and saves the data for further analysis.

## Features
- HTML parsing using BeautifulSoup
- Supports multiple URLs
- Cleans data using RegEx
- Logs errors to `log.txt`
- Saves data to `scraped_data.csv`

## Limitations
- Supports only Static HTML Pages
- Even non heavy websites(eg: Amazon, Flipkart) can have anti bot protection restricting you from scraping their pages
-While most of the code is like a template the css selectors have to be manually adjusted depending on the website

## Requirements
Install dependencies:
```bash
pip install -r requirements.txt