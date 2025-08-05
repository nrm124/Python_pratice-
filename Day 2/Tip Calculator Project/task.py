

print("Welcome to Tip calculator !")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How Much tip would you like to give? 10%, 12%, or 15%?"))
total_people = int(input("how many people to split the bill"))
percentage = tip_percentage/100 * total_bill + total_bill
bill_per_person =  round(percentage/total_people, 2)
print(f"Each person should pay: $ {bill_per_person}" )