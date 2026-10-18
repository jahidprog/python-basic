"""Exercise 1: Make a GET request and inspect the response."""
import requests

url = "https://quotes.toscrape.com/"
try:
    response = requests.get(url, timeout=15)
    print("Status code:", response.status_code)
    print("Final URL:", response.url)
    print("Content type:", response.headers.get("content-type"))
    response.raise_for_status()
    print("\nFirst 500 characters:\n")
    print(response.text[:500])
except requests.RequestException as exc:
    print("Request failed:", exc)
