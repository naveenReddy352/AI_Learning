import json

def get_monitoring_data():
    with open("monitoring_data.json", "r") as file: # Open the file in read mode
        return json.load(file) # Load the JSON data into a Python object
