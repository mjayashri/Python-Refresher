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

user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors. \n"))

rock_paper_scissor = [rock, paper, scissors]

print(rock_paper_scissor[int(user_choice)])
print("Computer Chose \n")

computer_chose = random.randint(0, 2)
print(rock_paper_scissor[computer_chose])

if user_choice == 0 and computer_chose == 2:
    print("you win")
elif computer_chose == 2 and user_choice == 0:
    print("you lose")
elif user_choice > computer_chose:
    print("you win")
elif computer_chose > user_choice:
    print("you lose")
elif computer_chose == user_choice:
    print("Its a draw")
else:
    print("invalid number, you lose!")















