# If bill was £150.00, split between 5 people with 12% tip

# Each person should pay (150 / 5) * 1.12

# round the result to 2 decimal places

print("Welcome to the tip calaulator!")
bill = float(input("What was the total bill £"))
tip = int(input("How much tip would you like to give? 10, 15, 20"))
people = int(input("How many people split the bill"))
tip_as_percent = tip / 100 
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay {final_amount} pounds")