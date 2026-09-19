# Experiment: API request
#
# Install requests first:
# pip install requests

import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url, timeout=10)

print("Status:", response.status_code)
print("Data:", response.json())
