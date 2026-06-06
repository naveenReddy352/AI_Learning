severity = input("Enter the severity: ")

if severity == "High":
    print("Escalate Immediately")
elif severity == "Medium":
    print("Assign to support team")
else:
    print("Monitor issue")
