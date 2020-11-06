print("#################")
print("## FLIP A COIN ##")
print("#################")

import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)


test_seed = random.randint(0, 1)
if test_seed == 1:
  print("Heads")
else:
  print("Tails")
