"""Exercise 5: Extract life-tagged quotes from every local HTML file."""
from pathlib import Path
from bs4 import BeautifulSoup
import csv

data_dir = Path("scraped_data")
html_files = sorted(data_dir.glob("*.html"))
life_quotes = []

if not html_files:
    print(f"No .html files found in: {data_dir.resolve()}")
    print("Put your saved files (for example, quotes1.html, quotes2.html) in this folder.")
else:
    for file_path in html_files:
        with file_path.open("r", encoding="utf-8") as file:
            soup = BeautifulSoup(file.read(), "lxml")

        for quote in soup.select("div.quote"):
            tags = [tag.get_text(strip=True) for tag in quote.select(".tags .tag")]
            if "life" not in tags:
                continue

            quote_el = quote.select_one("span.text")
            author_el = quote.select_one("small.author")
            if quote_el and author_el:
                life_quotes.append({
                    "quote": quote_el.get_text(strip=True),
                    "author": author_el.get_text(strip=True),
                    "source_file": file_path.name,
                })

    print(f"Scanned {len(html_files)} HTML file(s).")
    print(f"Found {len(life_quotes)} life quote(s).")
    for item in life_quotes:
        print(f'{item["quote"]} — {item["author"]} [{item["source_file"]}]')

    if life_quotes:
        output = Path("life_quotes.csv")
        with output.open("w", newline="", encoding="utf-8-sig") as file:
            writer = csv.DictWriter(file, fieldnames=["quote", "author", "source_file"])
            writer.writeheader()
            writer.writerows(life_quotes)
        print(f"Saved results to {output.resolve()}")
