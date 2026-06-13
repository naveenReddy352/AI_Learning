import requests #Import the requests library to make HTTP requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/todos") #Get the data from the API endpoint

    print(response.status_code)
except Exception as e:
    print("API Call Failed:",e)

data = response.json() #Retrieve the JSON data from the response, 
#converting it into a Python object (list of dictionaries)
print(data[0]) #Print the first item in the data list

incidents = response.json() 
for incident in incidents[:5]: #Iterate through the first 5 incidents in the list
    print("Incident:",incident["id"])
    print("Description:",incident["title"])
    print("- - - - - - - - - - - -")


for incident in incidents: 
    if incident["completed"] == False: #Check if the incident is not completed
        print("Incident:",incident["id"])
        print("Description:",incident["title"])
        print("- - - - - - - - - - - -")


