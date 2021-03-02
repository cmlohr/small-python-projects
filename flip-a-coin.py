  
print("""
#################
## FLIP A COIN ##
#################
""")

import random

while True:
    try: 
        test_seed = int(input("Create a seed number: "))
        random.seed(test_seed)
        test_seed = random.randint(0, 5999)
        if test_seed > 2999:
          print("Heads")
        elif test_seed < 2999:
          print("Tails")
        else:
            print("""
Your coin landed on its side!
The odds of this happening to a nickel is 1 out of 6000 tosses
or 0.0167%
""")
    except ValueError:
        print("Please enter a number")
        
