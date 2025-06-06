print("Welcome to the Tip Calculator!")
print("Calculate your tip and what the split would be!")

total_bill = float(input("What was the total bill? $"))
tip_perc = int(input("what percentage of the bill would you like to tip? 0%, 5%, 10%, 12%, 15%, or 20%?"))
numOfAttendees = int(input("How many people are splitting the bill equally? "))

tip = (tip_perc/100) * total_bill
total = tip + total_bill
split = total /numOfAttendees
final_split = round(split, 2)

print(f"The tip is {tip} and the total (billl + tip) is {total}.")
print(f"Each person splitting will pay {final_split}.")