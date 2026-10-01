bill_amount = input("Enter the bill amount: ")
answer=input("What was the service quality (bad, okay, good, excellent):")
values=[answer]
service_quality = answer
for i in values:
    if service_quality == "bad":
        tip_percentage = 0
    elif service_quality == "okay":
        tip_percentage = 0.15
    elif service_quality == "good":
        tip_percentage = 0.20
    elif service_quality == "excellent":
        tip_percentage = 0.25
        print(bill_amount * tip_percentage)
