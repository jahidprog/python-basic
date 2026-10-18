"""Exercise 3: Parse a page title with BeautifulSoup."""
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
try:
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")

    print("Page title:", soup.title.get_text(strip=True) if soup.title else "No title found")
    print("H1 headings:")
    for heading in soup.select("h1"):
        print("-", heading.get_text(" ", strip=True))
except requests.RequestException as exc:
    print("Request failed:", exc)
