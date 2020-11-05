print("################################")
print("###     Love Calculator!     ###")
print("################################")
lower_name1 = name1.lower()
lower_name2 = name2.lower()
ourstring = lower_name1 + lower_name2

t = ourstring.count("t")
r = ourstring.count("r")
u = ourstring.count("u")
e = ourstring.count("e")
true = t + r + u + e
l = ourstring.count("l")
o = ourstring.count("o")
v = ourstring.count("v")
e = ourstring.count("e")
love = l + o + v + e


truelove = str(true) + str(love)

score = int(truelove)

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")