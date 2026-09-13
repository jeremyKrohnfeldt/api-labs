import requests

response = requests.get("https://httpbin.org/get")
data = response.json()
headers = data["headers"]

print("Request URL:", data["url"])
print("Source IP:", data["origin"])
print("User-Agent:", headers["User-Agent"])