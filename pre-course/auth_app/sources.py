import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()

for data in data:
    print(data["body"],"\n")