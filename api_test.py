import requests


# -----------------------------
# 1. GET request
# -----------------------------

response = requests.get("https://httpbin.org/get")
data = response.json()

print("GET response:")
print(data)

print("\nAvailable response keys:")
print(data.keys())

print("\nResponse types:")
print(type(data))
print(type(data.keys()))
print(type(data.values()))
print(type(data.items()))

if "origin" in data:
    print("\nThe API provided an origin:", data["origin"])

print("Origin:", data["origin"])
print("Origin using get():", data.get("origin"))
print("Missing key:", data.get("banana"))


# -----------------------------
# 2. Functions
# -----------------------------

def say_hello(name):
    message = "Hello, " + name
    return message


greeting = say_hello("Jeremy")

print("\nFunction example:")
print(greeting)
print(type(greeting))


def introduce(name, role="TAK Admin"):
    return name + " is a " + role


print(introduce("Jeremy", "Developer"))
print(introduce("Jeremy"))


# -----------------------------
# 3. Device processing function
# -----------------------------

def check_device(device):
    if device["online"]:
        return device["callsign"] + " is online"
    else:
        return device["callsign"] + " is offline"


# -----------------------------
# 4. Process a local list
# -----------------------------

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

print("\nLocal device status:")

for device in devices:
    status = check_device(device)
    print(status)

    if device["online"]:
        online_count += 1

print("Total online devices:", online_count)


# -----------------------------
# 5. POST one device as JSON
# -----------------------------

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

print("\nDevice returned by API:")
print(device_from_api)

print("Callsign: ", device_from_api["callsign"])

status = check_device(device_from_api)
print(status)


# -----------------------------
# 6. POST multiple devices as JSON
# -----------------------------

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

response = requests.post(
    "https://httpbin.org/post",
    json=devices
)

data = response.json()

devices_from_api = data["json"]

print("\nDevices returned by API:")
print(devices_from_api)

print("Type of devices_from_api:", type(devices_from_api))
print("Type of first device:", type(devices_from_api[0]))
print("First device:", devices_from_api[0])


# -----------------------------
# 7. Process devices returned by API
# -----------------------------

print("\nAPI device status:")

for device in devices_from_api:
    status = check_device(device)
    print(status)

print("\nOffline devices:")
for device in devices_from_api:
    if not device["online"]:
        print(device["callsign"])

offline_count = 0

for device in devices_from_api:
    if not device["online"]:
        offline_count += 1

print("Total offline devices:", offline_count)

online_callsigns = [device["callsign"] for device in devices_from_api if device["online"]]
print("Online devices:", online_callsigns)

online_a_callsign = [
    device["callsign"]
    for device in devices_from_api
    if device["online"] and device["callsign"].startswith("A")
]
print("Online devices starting with 'A':", online_a_callsign)