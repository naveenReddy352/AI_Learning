import json

from monitoring_api import get_monitoring_data # Import the function to get monitoring data
from server_analyzer import analyze_server # Import the function to analyze server data

data = get_monitoring_data()
critical, high,normal = analyze_server(data) # Analyze the server data to get critical and healthy servers

report = {
    "critical_servers": len(critical),
    "high_servers": len(high),
    "servers_needing_attention":[
        server["server"]
        for server in critical
    ]
}

with open("health_report.json", "w") as file: # Open the file in write mode
    json.dump(report, file, indent=4) # Write the report data to the file with indentation for readability

print(report)

#Error count per application
applications = {}
for server in data:
    app = server["application"]
    if app not in applications:
        applications[app] = 0
    
    applications[app] += server["error_count"]

print("Error count per application: ")
print(applications)

with open("management_summary.json","w") as file:
    summary = {
        "total_servers": len(data),
        "critical_servers": len(critical),
        "applications_affected":[
           # need top 2 applications
           app for app in sorted(applications, key=applications.get, reverse=True)[:2]
        ]
    }
    json.dump(summary, file, indent=4) # Write the summary data to the file with indentation for readability
