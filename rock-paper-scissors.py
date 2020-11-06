import random
print("#######################")
print("# ROCK PAPER SCISSORS #")
print("#######################")
r = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

p = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

s = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [1, 2, 3]
npc = random.choice(rps)
player_choice = input("Type '1' for rock, '2' for paper, '3' for scissors\n>>")
player1 = int(player_choice)

print("#######################")
print("You throw:")
if player1 == 1:
  print("Rock!\n"+(r))
if player1 == 2:
  print("Paper!\n"+(p))
if player1 == 3:
  print("Scissors!\n"+(s))

print("Computer throws:")
if npc == 3:
  print("Scissors!\n"+(s))
if npc == 2:
  print("Paper!\n"+(p))
if npc == 1:
  print("Rock!\n"+(r))

if player1 >= 4 or player1 <0:
  print("Invalid input, you lose!")
elif player1 == npc:
  print("Draw!")
elif player1 == 1 and npc == 2:
  print("You Lose!")
elif player1 == 1 and npc == 3:
  print("You Win!")
elif player1 == 2 and npc == 1:
  print("You Win!")
elif player1 == 2 and npc == 3:
  print("You Lose!")
elif player1 == 3 and npc == 1:
  print("You Lose!")
elif player1 == 3 and npc == 2:
  print("You Win!")


