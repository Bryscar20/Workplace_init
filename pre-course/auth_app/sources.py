import json
import requests

url = "https://api.nasa.gov/planetary/apod?api_key=I5zlMkrXLLvEXm3MFi0F7kZN00sVSTnnVIt0AqIz"


data = requests.get(url)
print(data.text, end='\n')