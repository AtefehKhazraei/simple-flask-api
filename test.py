import requests

BASE = "http://127.0.0.1:5000/"


#id video ro midim , title o like o views bar migardone
# input()
response = requests.patch(BASE + "video/3", {})
print(response.json())