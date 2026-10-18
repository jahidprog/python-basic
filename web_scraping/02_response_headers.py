"""Exercise 2: Inspect HTTP response headers."""
import requests

url = "https://quotes.toscrape.com/"
try:
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    print("Status:", response.status_code)
    print("\nSelected headers:")
    for name in ("content-type", "content-length", "server", "date"):
        print(f"{name}: {response.headers.get(name, '(not provided)')}")
except requests.RequestException as exc:
    print("Request failed:", exc)
