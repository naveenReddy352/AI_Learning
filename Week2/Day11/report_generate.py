import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos") #Get the data from the API endpoint

incidents = response.json() #Retrieve the JSON data from the response, 
#converting it into a Python object (list of dictionaries)

open_incidents = []
total = len(incidents) #Calculate the total number of incidents
open_incidents_count = 0
for incident in incidents:
    if incident["completed"] == False: #Check if the incident is not completed
        open_incidents_count += 1
        open_incidents.append(incident) #Add the open incident to the list of open incidents

closed_incidents = total - open_incidents_count
first_ten_open = open_incidents[:10] #Get the first 10 open incidents

with open("critical_report.json", "w") as file: # Open the file in write mode
    json.dump(open_incidents, file, indent=4) # Write the open incidents data to the file with indentation for readability

with open("dashboard.json", "w") as file:
    summary = {
        "total_incidents": total,
        "open_incidents": open_incidents_count,
        "closed_incidents": closed_incidents
    }
    json.dump(summary, file, indent=4) # Write the summary data to the file with indentation for readability

with open("first_ten_open.json", "w") as file:
    json.dump(first_ten_open, file, indent=4) # Write the first ten open incidents data to the file with indentation for readability


print("Report generated")
