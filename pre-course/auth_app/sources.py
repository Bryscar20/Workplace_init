import json
import requests

url_api = "https://api.themoviedb.org/3/movie/550?api_key=4c20948fcb0bf4dd17dfd9e4b05423bc"


data  = requests.get(url_api)

n_Data = json.loads(data.text)
print(n_Data["overview"])


