"""Exercise 15: Fetch JSON from a public practice API."""
import requests

url = "https://jsonplaceholder.typicode.com/posts"
try:
    response = requests.get(url, params={"_limit": 5}, timeout=15)
    response.raise_for_status()
    posts = response.json()

    for post in posts:
        print(f'ID: {post["id"]} | Title: {post["title"]}')
        print(post["body"], "\n")
except requests.RequestException as exc:
    print("Request failed:", exc)
except ValueError:
    print("The server response was not valid JSON.")
