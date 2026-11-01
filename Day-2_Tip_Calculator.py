print("Welcome to the Tip Calculator!")
bill_amount = float(input("What was the total bill?\n$"))
tip_count = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
people = int(input("How much people to split the bill?\n"))

total_tip = (bill_amount + bill_amount * (tip_count % 100)) / people

print(f"Each person should pay: ${total_tip:.2f}")