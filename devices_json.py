import json

# Open the JSON file in read mode
with open("devices.json", "r") as file:
    # Convert the JSON array into a Python list
    devices = json.load(file)

# Create variable to count the number of devices that are online
online_count = 0

# Loop through each device dictionary in the list.
for device in devices:
    if device["uid"] == "bravo-2":
        device["callsign"] = "BRAVO-TEST"
    # Check whether this device is online
    if device["online"]:
        # Add 1 to the online count
        online_count += 1
        # Only print devices whose online status is True
        print(device["callsign"], "is online")

print("Total online devices:", online_count)

#Save the modified Python List back to the JSON file
with open("devices.json", "w") as file:
    json.dump(devices, file, indent=4)