import random
Rock =''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper ='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

Scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
gaming_images =[Rock,Paper,Scissor]

my_choice=int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors:"))


print(gaming_images[my_choice])


computer_choicee=random.randint(0,2)

print("Computer`s choice is:")


print(gaming_images[computer_choicee])




if my_choice >= 3 or my_choice < 0:
    print("You added an invalid number! Try again, You lose!")
elif my_choice == 0 and computer_choicee == 2:
    print("You win!")
elif computer_choicee == 0 and my_choice == 2:
    print("You lose!")
elif computer_choicee > my_choice:
    print("You lose!")
elif my_choice > computer_choicee:
    print("You win!")
elif my_choice == computer_choicee:
    print("it is a draw!")


