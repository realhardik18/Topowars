import requests

url = "https://countriesnow.space/api/v0.1/countries/capital"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
