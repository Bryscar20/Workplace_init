import json
import requests

url = f"https://api.nasa.gov/DONKI/FLR?startDate=2000-01-01&endDate=2020-08-30&api_key=jO8sNqmLfQRsNK7I2G8AEp64gVn9n4QoQaVmoUh3"


data  = requests.get(url)

json_strings = data.json()

# json_string = json.dumps(json_strings, indent=2)
# print(type(json_string))
json_string = json.load(json_strings)
print(type(json_strings))