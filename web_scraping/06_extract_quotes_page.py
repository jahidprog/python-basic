"""Exercise 6: Extract quote text, author, and tags from one practice page."""
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
try:
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")

    for item in soup.select("div.quote"):
        text_el = item.select_one("span.text")
        author_el = item.select_one("small.author")
        tags = [tag.get_text(strip=True) for tag in item.select(".tags .tag")]
        if text_el and author_el:
            print({
                "quote": text_el.get_text(strip=True),
                "author": author_el.get_text(strip=True),
                "tags": tags,
            })
except requests.RequestException as exc:
    print("Request failed:", exc)
