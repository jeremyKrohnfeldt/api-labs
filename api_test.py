import requests

response = requests.get("https://httpbin.org/get")
data = response.json()

print(data)
print("Available response keys:", data.keys())


print(type(data.keys()))
print(type(data.values()))
print(type(data.items()))

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

print(type(data))
print(data.keys())

device = {
    "uid": "alpha-1",
    "callsign": "ALPHA-1",
    "online": True
}

response = requests.post(
    "https://httpbin.org/post",
    json=device
)
data = response.json()

device_from_api = data["json"]

print(device_from_api)
print(data["json"]["callsign"])

status = check_device(device_from_api)
print(status)


