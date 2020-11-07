import random

print("#####################################")
print("######   Password Generator!   ######")
print("#####################################")
print("######   2020   |  By @Cmlohr  ######")
print("#####################################")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to my Password Generator!")

##### Input fields
print("Type the number of inputs for each question.")
nr_letters = int(input("How many letters?\n>>"))
nr_string = int(input("How many symbols?\n>>"))
nr_numbers = int(input("How many numbers?\n>>"))

#####  Choice Randomization  #####
letter_pick = random.choices(letters, k=nr_letters)
num_pick = random.choices(numbers, k=nr_numbers)
symbol_pick = random.choices(symbols, k=nr_string)

##### Combining input lists #####
letter_pick += num_pick
symbol_pick += letter_pick

##### Shuffle and join into single string
random.shuffle(symbol_pick)
mypass = "".join(symbol_pick)

print(f"Your new password is: {mypass}")
