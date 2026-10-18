"""Exercise 4: Extract links and their text."""
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
try:
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")

    for link in soup.select("a[href]"):
        label = link.get_text(" ", strip=True) or "[no link text]"
        absolute_url = urljoin(response.url, link["href"])
        print(f"{label} -> {absolute_url}")
except requests.RequestException as exc:
    print("Request failed:", exc)
