"""Exercise 14: Extract card-like elements using CSS selectors.

This is a template. Set PAGE_URL and selectors for a site you own or are allowed to scrape.
Inspect the page HTML first; selectors vary from site to site.
"""
import requests
from bs4 import BeautifulSoup

PAGE_URL = "https://quotes.toscrape.com/"
CARD_SELECTOR = "div.quote"
TITLE_SELECTOR = "span.text"
DETAIL_SELECTOR = "small.author"

try:
    response = requests.get(PAGE_URL, timeout=15)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")

    for card in soup.select(CARD_SELECTOR):
        title = card.select_one(TITLE_SELECTOR)
        detail = card.select_one(DETAIL_SELECTOR)
        print({
            "title": title.get_text(" ", strip=True) if title else None,
            "detail": detail.get_text(" ", strip=True) if detail else None,
        })
except requests.RequestException as exc:
    print("Request failed:", exc)
