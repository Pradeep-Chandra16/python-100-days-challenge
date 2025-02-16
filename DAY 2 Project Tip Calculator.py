print("Welcome to the tip Calculator!")
bill = float(input("What was the total bill? Rs.\n"))
tip = int(input("What percentage of tip would you like to give? 10 12 or 15 : \n"))
people = int(input("How many people to split the bill between?\n"))
tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill/people
final_amount = round(bill_per_person, 2)
print(f"Each person has to pay: \nRs.{final_amount}") 

