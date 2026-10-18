"""Exercise 11: Scrape quotes and save them to CSV."""
import csv
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
rows = []

try:
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")

    for quote in soup.select("div.quote"):
        text_el = quote.select_one("span.text")
        author_el = quote.select_one("small.author")
        tags = [tag.get_text(strip=True) for tag in quote.select(".tags .tag")]
        if text_el and author_el:
            rows.append({
                "quote": text_el.get_text(strip=True),
                "author": author_el.get_text(strip=True),
                "tags": ", ".join(tags),
            })

    with open("quotes.csv", "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=["quote", "author", "tags"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Saved {len(rows)} rows to quotes.csv")
except requests.RequestException as exc:
    print("Request failed:", exc)
