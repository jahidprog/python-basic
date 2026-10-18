"""Exercise 7: Extract rows and cells from an HTML table.

Change URL to a page that contains an HTML table and permits automated access.
"""
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"
try:
    response = requests.get(
        url,
        headers={"User-Agent": "LearningScraper/1.0 (educational practice)"},
        timeout=15,
    )
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")
    table = soup.select_one("table.wikitable")

    if not table:
        print("No table.wikitable found. Inspect the page and adjust the selector.")
    else:
        for row in table.select("tr")[:10]:
            cells = [cell.get_text(" ", strip=True) for cell in row.select("th, td")]
            print(cells)
except requests.RequestException as exc:
    print("Request failed:", exc)
