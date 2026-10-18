"""Exercise 8: Practice CSS selectors with quote cards."""
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
try:
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")

    print("First quote card:")
    first = soup.select_one("div.quote")
    print(first.get_text(" ", strip=True) if first else "No quote cards found")

    print("\nAll author names:")
    for author in soup.select("small.author"):
        print(author.get_text(strip=True))
except requests.RequestException as exc:
    print("Request failed:", exc)
