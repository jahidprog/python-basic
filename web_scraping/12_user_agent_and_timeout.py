"""Exercise 12: Send a User-Agent and set a timeout."""
import requests

url = "https://httpbin.org/headers"
headers = {
    "User-Agent": "WebScrapingPractice/1.0 (learning project)",
    "Accept": "text/html,application/json",
}

try:
    response = requests.get(url, headers=headers, timeout=(5, 15))
    response.raise_for_status()
    print(response.text)
except requests.RequestException as exc:
    print("Request failed:", exc)
