print("################################")
print("#####    TIP CALCULATOR    #####")
print("################################")
print("#####   Coded by @Cmlohr   #####")
print("################################")
print("                                ")
bill = input("What was the total bill? \n")
tip = input("What percentage tip would you like to give? 10, 12 or 15? \n")
party = input("How many people to split the bill? \n")

bill = float(bill)
cal_tip = int(tip) / 100
party = int(party)
tip_total = bill * cal_tip
grand_total = tip_total + bill
split_total = round(grand_total / party, 2)
formated_total = "{:.2f}".format(split_total)

print("Each person should pay: $"+f"{formated_total}")