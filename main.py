rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
print("Welcome to the Rock, Paper, Scissors Game")
choise = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
choises = [rock,paper,scissors]

c1 = choises[choise]
print(c1)
iac = random.randint(0,2)
ia = choises[iac]
print("Computer chose:")
print(ia)

if choise == 0 and iac == 0:
  print("Draw")
elif choise == 1 and iac == 1:
  print("Draw")
elif choise == 2 and iac == 2:
  print("Draw")
elif choise == 0 and iac == 2:
  print("You Win")
elif choise == 1 and iac == 2:
  print("You Lose")
elif choise == 2 and iac == 0:
  print("You Lose")
elif choise == 0 and iac == 1:
  print("You Lose")
elif choise == 1 and iac == 0:
  print("You Win")
elif choise == 2 and iac == 1:
  print("You Win")
else:
  print("ERROR")
