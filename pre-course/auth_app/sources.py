import json

items = []
with open("sources.json", "r") as f:
    for data in f:
        print(type(data))


# import json
# import requests

# url = "https://api.nasa.gov/DONKI/FLR?startDate=2000-01-01&endDate=2020-08-30&api_key=jO8sNqmLfQRsNK7I2G8AEp64gVn9n4QoQaVmoUh3"


# data  = requests.get(url)

# json_strings = data.json()

# # json_string = json.dumps(json_strings, indent=2)
# final_dictionary = json.loads(json_strings) 
# json_string = final_dictionary
# print(type(json_string))