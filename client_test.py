import requests

url = "http://127.0.0.1:8000/solve"

data = {
    "problem": "I feel confused about my career"
}

response = requests.post(url, json=data)

print(response.json())