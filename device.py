device = {
    "uid": "alpha-1",
    "callsign": "ALPHA-1",
    "latitude": 31.4638,
    "longitude": -100.4370,
    "altitude": 5000,
    "online": True
}

print(device)
print(device["uid"])
print(device["callsign"])
print(device["latitude"])
print(device["altitude"])
print(device["online"])

device["online"] = False
print(device["online"])

