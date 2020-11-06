print("###################")
print("## BILL ROULETTE ##")
print("###################")
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")

items = len(names)
choice = random.randint(0, items - 1)
payee = names[choice]
print(payee + " is going to buy the meal today!")