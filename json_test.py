import json

#Open the JSON file and read its contents
#The file itself contains JSON text.
with open("device.json", "r") as file:
    #Read the contents of the file, Python sees this as a str.
    json_text = file.read()
#Confirm that we have a Python str.
print(type(json_text))

# Parse the JSON string into a Python object.
# In this case, the JSON represents one object, so Python creates a dictionary (dict).
device = json.loads(json_text)

# Confirm that the JSON was converted into a Python dictionary.
print(type(device))
# Print the entire Python dictionary.
print(device)
# Access a specific value from the dictionary using its key.
print(device["callsign"])

