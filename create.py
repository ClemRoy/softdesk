
import requests,json

endpoint = "http://127.0.0.1:8000/project/" 

data = {
    "title": "test create",
    "description" : "test create desc",
    "type" : "BE"
}

get_response = requests.get(endpoint)
print(get_response.text)