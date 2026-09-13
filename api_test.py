import requests

response = requests.get("https://httpbin.org/get")
data = response.json()
headers = data["headers"]

print("Request URL:", data["url"])
print("Source IP:", data["origin"])
print("User-Agent:", headers["User-Agent"])

print("Available response keys:", data.keys())


print(type(data))
print(type(data.keys()))
print(type(data.values()))
print(type(data.items()))

print("url" in data)
print("origin" in data)
print("banana" in data)

if "origin" in data:
    print("The API provided an origin:", data["origin"])

print(data["origin"])
print(data.get("origin"))
print(data.get("banana"))

def say_hello(name):
    message = "Hello, " + name
    return message

greeting = say_hello("Jeremy")

print(greeting)
print(type(greeting))

def introduce(name, role="TAK Admin"):
    return name + " is a " + role

print(introduce("Jeremy", "Developer"))
print(introduce("Jeremy"))


def check_device(device):
    if device["online"]:
        return device["callsign"] + " is online"
    else:
        return device["callsign"] + " is offline"

devices = [
{
    "uid": "alpha-1",
    "callsign": "ALPHA-1",
    "online": True
},
{
    "uid": "bravo-1",
    "callsign": "BRAVO-1",
    "online": False
},
{
    "uid": "charlie-1",
    "callsign": "CHARLIE-1",
    "online": True
}
]

online_count = 0

for device in devices:
    status = check_device(device)
    print(status)

    if device ["online"]:
        online_count += 1
print("Total online devices:", online_count)