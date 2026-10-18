"""Exercise 13: Handle common request errors."""
import requests

url = "https://quotes.toscrape.com/"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
except requests.Timeout:
    print("The request timed out. Try again later.")
except requests.HTTPError as exc:
    print("The server returned an HTTP error:", exc)
except requests.ConnectionError:
    print("Could not connect. Check your internet connection.")
except requests.RequestException as exc:
    print("Other request error:", exc)
else:
    print("Success:", response.status_code)
