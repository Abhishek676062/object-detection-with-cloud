import requests
import json

url = "https://api.imagga.com/v2/tags"
querystring = {"image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDRDB2-E8ZmlPAxkhR2eu7Pk3aae36fMHTDw&usqp=CAU"}
headers = {
    'accept': "application/json",
    'authorization': "Basic YWNjXzhiMDFmMjA2ZTNlNjMxODo2NTg0OGU5YTJhYjk3OTNjZjU1NDBjYzVjMzM3YmEyNQ=="
}

responce = requests.request("GET", url, headers=headers, params=querystring)
data = json.loads(responce.text.encode("ascii"))

for i in range(6):
    tag =data["result"]["tags"][i]["tag"]["en"]
    print(tag)