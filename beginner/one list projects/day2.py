#tip calculator

print("Welcome to the tip calculator!")
total_bill = int(input("What was the total bill?\n"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
people_amount = int(input("How many people to split the bill?\n"))
total_tip = int((total_bill*tip)/100)
bill_for_each = int((total_bill+total_tip)/people_amount)
print(f"Each person should pay: {bill_for_each}")