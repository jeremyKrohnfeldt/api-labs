import json

def check_device(device):
    if device ["online"]:
        return device["callsign"] + " is online"
    else:
        return device["callsign"] + " is offline"
    
# Open the JSON file in read mode
with open("devices.json", "r") as file:
    # Convert the JSON array into a Python list
    devices = json.load(file)

# Create variable to count the number of devices that are online
online_count = 0

# Loop through each device dictionary in the list.
for device in devices:
    status = check_device(device)
    print(status)

    if device["online"]:
        online_count += 1

print("Total online devices:", online_count)

#Save the modified Python List back to the JSON file
with open("devices.json", "w") as file:
    json.dump(devices, file, indent=4)