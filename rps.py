import random
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

# Write your code below this line 👇
rps = [rock, paper, scissors]
player_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.:\n"))
cpu_choose = random.randint(0, 2)

if player_choose == cpu_choose:
    print(f"{rps[player_choose]}\n VS \n {rps[cpu_choose]}")
    print("It's a ~Draw!~")
elif player_choose == 0 and cpu_choose == 2:
    print(f"{rps[player_choose]}\n VS \n {rps[cpu_choose]}")
    print("You Won!")
elif player_choose == 1 and cpu_choose == 0:
    print(f"{rps[player_choose]}\n VS \n {rps[cpu_choose]}")
    print("You Won!")
elif player_choose == 2 and cpu_choose == 1:
    print(f"{rps[player_choose]}\n VS \n {rps[cpu_choose]}")
    print("You Won!")
else:
    print(f"{rps[player_choose]}\n VS \n {rps[cpu_choose]}")
    print("You Lose!")
