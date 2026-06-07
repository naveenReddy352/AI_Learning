import json

with open("incidents.json", "r") as file: # Open the file in read mode
    incidents = json.load(file) # Load the JSON data into a Python object

# Print the incidents
for incident in incidents:
    print("ID: ", incident["incident_id"])
    print("Application: ", incident["application"])
    print("Priority: ", incident["priority"])
    print("Status: ", incident["status"])
    print("_ _ _ _ _ _ _ _ _")

open_count = 0
for incident in incidents:
    if incident["status"] == "open":
        open_count += 1

print("Total open incidents: ", open_count)

count = 0
for incident in incidents:
    if incident["priority"] in ["High","Critical"]:
        count += 1

print("Total high and critical incidents: ", count)

applications = {}

for incident in incidents:
    app = incident["application"]
    if app not in applications:
        applications[app] = 0
    
    applications[app] += 1


print("Incidents per application: ")
print(applications)

print("Incidents Summary: ")
summary = {
    "total_incidents": len(incidents),
    "open_incidents": open_count,
    "critical_incidents": count
}

with open("dashboard.json","w") as file: # Open the file in write mode
    json.dump(summary, file, indent=4) # Write the summary data to the file with indentation for readability

print(summary)

paymentApp_count = 0
for incident in incidents:
    if incident["application"] == "Payments" and incident["status"] == "open":
        paymentApp_count += 1

print("Total open incidents in Payments application: ", paymentApp_count)