"""Exercise 9: Follow pagination links on Quotes to Scrape."""
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

start_url = "https://quotes.toscrape.com/"
max_pages = 3
url = start_url
session = requests.Session()
session.headers.update({"User-Agent": "LearningScraper/1.0 (educational practice)"})

try:
    for page_number in range(1, max_pages + 1):
        response = session.get(url, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "lxml")

        quotes = soup.select("div.quote")
        print(f"\nPage {page_number}: {len(quotes)} quote(s)")
        for quote in quotes:
            text_el = quote.select_one("span.text")
            author_el = quote.select_one("small.author")
            if text_el and author_el:
                print(f'{text_el.get_text(strip=True)} — {author_el.get_text(strip=True)}')

        next_link = soup.select_one("li.next a[href]")
        if not next_link:
            print("No next page link. Finished.")
            break
        url = urljoin(response.url, next_link["href"])
except requests.RequestException as exc:
    print("Request failed:", exc)
finally:
    session.close()
