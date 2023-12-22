import requests
import json

url = "https://www.fruityvice.com/api/fruit/all"
response = requests.get(url)

# Parse the JSON data received from the API response using json.loads() and store it in the results variable.
results = json.loads(response.text)
# print(results)

print(response.status_code)
print(response.headers)
print(response.json())


# response = requests.post((https://api.example.com/submit), data={(key): (value)})