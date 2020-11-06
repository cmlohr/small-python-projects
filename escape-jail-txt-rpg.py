print('''
   88            88 88  
   ""            "" 88  
                    88  
   88 ,adPPYYba, 88 88  
   88 ""     `Y8 88 88  
   88 ,adPPPPP88 88 88  
   88 88,    ,88 88 88  
   88 `"8bbdP"Y8 88 88  
  ,88                   
888P"                   
''')
print("##########################")
print("##### ESCAPE TXT RPG #####")
print("##########################")
print("######  by @Cmlohr  ######")
print("                        ")
print("    Welcome Prisoner    ")
print("You were falsely accused \nand sentenced to life in\n         prison.")
print("Your mission is to escape") 
print("      or die trying.       ") 
print("##########################")
print("##########################")
fork1 = input("  Tonight is the night!\nYou\'re dank cell spills into\n  a dimly lit corridor.\n     It seems quiet.\n    You must choose:\n     Left or Right?\n>>")
fork = fork1.lower()
if fork == "right":
  print("##########################\n     You were caught!\nYou were sent to solitary\n       confinement.\n      -Game Over-")
elif fork == "left":
  fork2 = input("##########################\nYou sneak past the cells of\nsleeping inmates.  You come\n to the cat walk, ahead of\n you is a guard on patrol.\n   'wait' or 'attack'?\n>>")
waiting = fork2.lower()
if waiting == "wait":
  alpha = input("##########################\n  Your patience pays off!\n The guard turns and goes\nthe other way allowing you\n the opportunity to sneak\npast.  You make your way\n   to the control room.\nAhead of you are three non\ndescript doors with white\n         labels:\n | 'A1' | 'A2' | 'A3' |\n      Which door?\n>>")
elif waiting == "attack":
  print("##########################\n          FOOL!\nThe guard is over zelious\n  and feels threatened.\n      You have died.\n      -Game Over-")

alpha_door = alpha.lower()
if alpha_door == "a1":
  print("##########################\n Luck is not on your side.\n  You've walked into the\n   guard's dinning hall.\nYou manage to talk yourself\n into keeping your life in\n   exchange for solitary\n       confinement.\n        But still.\n      -Game Over-")
elif alpha_door == "a2":
  print("##########################\nYou've found the motorpool!\n You hear someone coming!\n       Think Fast!\n   You climb into the\nundercarrage of the prison\nbus. It's a long wait till\n morning, but it pays off!\nOn a routine trip the bus\n pulls out of the prison,\n   taking you with it.\n         FREEDOM!\n##########################\n        Congrats!\n         You Win!\n  Thank you for playing!")
elif alpha_door == "a3":
  print("##########################\n        ~CLICK!~\n Your in a utility closet\nThe door locked behind you.\n  You are found in the\nmorning by a trustee and\n reported to the guards.\nYou\'re thrown into solitary\nconfinement for attempting\n   to escape. You never\nsee the light of day agian.\n      -Game Over-")

print('''
   88            88 88  
   ""            "" 88  
                    88  
   88 ,adPPYYba, 88 88  
   88 ""     `Y8 88 88  
   88 ,adPPPPP88 88 88  
   88 88,    ,88 88 88  
   88 `"8bbdP"Y8 88 88  
  ,88                   
888P"                   
''')
print("##########################")
print("##### ESCAPE TXT RPG #####")
print("##########################")
print("######  by @Cmlohr  ######")
print("                        ")
print("    Welcome Prisoner    ")
print("You were falsely accused \nand sentenced to life in\n         prison.")
print("Your mission is to escape") 
print("      or die trying.       ") 
print("##########################")
print("##########################")
fork1 = input("  Tonight is the night!\nYour dank cell spills into\n  a dimly lit corridor.\n     It seems quiet.\n    You must choose:\n     Left or Right?\n>>")
fork = fork1.lower()
if fork == "right":
  print("##########################\n     You were caught!\nYou were sent to solitary\n       confinement.\n      -Game Over-")
elif fork == "left":
  fork2 = input("##########################\nYou sneak past the cells of\nsleeping inmates.  You come\n to the cat walk, ahead of\n you is a guard on patrol.\n   'wait' or 'attack'?\n>>")
waiting = fork2.lower()
if waiting == "wait":
  alpha = input("##########################\n  Your patience pays off!\n The guard turns and goes\nthe other way allowing you\n the opportunity to sneak\npast.  You make your way\n   to the control room.\nAhead of you are three non\ndescript doors with white\n         labels:\n | 'A1' | 'A2' | 'A3' |\n      Which door?\n>>")
elif waiting == "attack":
  print("##########################\n          FOOL!\nThe guard is over zelious\n  and feels threatened.\n      You have died.\n      -Game Over-")

alpha_door = alpha.lower()
if alpha_door == "a1":
  print("##########################\n Luck is not on your side.\n  You've walked into the\n   guard's dinning hall.\nYou manage to talk yourself\n into keeping your life in\n   exchange for solitary\n       confinement.\n        But still.\n      -Game Over-")
elif alpha_door == "a2":
  print("##########################\nYou've found the motorpool!\n You hear someone coming!\n       Think Fast!\n   You climb into the\nundercarrage of the prison\nbus. It's a long wait till\n morning, but it pays off!\nOn a routine trip the bus\n pulls out of the prison,\n   taking you with it.\n         FREEDOM!\n##########################\n        Congrats!\n         You Win!\n  Thank you for playing!")
elif alpha_door == "a3":
  print("##########################\n        ~CLICK!~\n Your in a utility closet\nThe door locked behind you.\n  You are found in the\nmorning by a trustee and\n reported to the guards.\nYou\'re thrown into solitary\nconfinement for attempting\n   to escape. You never\nsee the light of day agian.\n      -Game Over-")

