devices = [
    {
        "uid": "alpha-1",
        "callsign": "ALPHA-1",
        "online": True
    },
    {
        "uid": "bravo-1",
        "callsign": "BRAVO-1",
        "online": True
    },
    {
        "uid": "charlie-1",
        "callsign": "CHARLIE-1",
        "online": False
    }
]

print("\n--- DEVICE STATUS ---")

for device in devices:
    print(device["callsign"])