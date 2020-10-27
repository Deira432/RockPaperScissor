# RockPaperScissor 

from time import sleep
import random
user_name = input("Enter your name : ")

print(f"Hello {user_name}, Lets begin the game...\n\n") ; sleep(1.5)
#Rules of the Game
print("Rules of the game are as follows : ") ; sleep(1)
print("   1. You will be playing against the computer") ; sleep(1)
print("   2. You have to select a number (1, 2, 3)") ; sleep(1)
print("   3. Each has their own value.  It is depicted below....") ; sleep(1)
print('       1 --> Rock ') ; sleep(0.5)
print('       2 --> Paper') ; sleep(0.5)
print('       3 --> Scissors') ; sleep(0.5)
print('   4. Make sure you give a correct input.. ') ; 
print('      Invalid input makes you lose a point...') ; sleep(1)
print('   5. Best out of three will be calculated...\n') ; sleep(1)
print('***************Lets start the game*************** \n\n')

human_point = 0
computer_point = 0
for i in range (0,3):

  user_input = int(input("Enter your option : "))
  if user_input == 1 :
    print(f"{user_name} selected Rock ")
  elif user_input == 2:
    print(f"{user_name} selected Paper ")
  elif user_input == 3:
    print(f"{user_name} selected Scissor ")
  else :
    print("Invalid input...You lose a point ")
    human_point -= 1 
    continue

  computer_input = random.randint(1,3)
  if computer_input == 1:
    print("Computer selected Rock\n")
  elif computer_input == 2:
    print("Computer Selected Paper\n")
  else:
    print("Computer selected Scissors\n")
  

  if computer_input == 1 and user_input == 1:
    print("It is a tie. One point each...")
    human_point += 1
    computer_point += 1
  elif computer_input == 1 and user_input == 2:
    print(f"{user_name} wins the set....One point for {user_name}")
    human_point += 1
  elif computer_input == 1 and user_input == 3:
    print("Computer wins the set.... One point for Computer")
    computer_point += 1
  elif computer_input == 2 and user_input == 1:
    print("Computer wins the set....One point for Computer")
    computer_point += 1
  elif computer_input == 2 and user_input == 2:
    print("It is a tie.  One point each ....")
    computer_point += 1   
    human_point += 1
  elif computer_input == 2 and user_input == 3:
    print(f"{user_name} wins the set....One point for {user_name}")
    human_point += 1
  elif computer_input == 3 and user_input == 1:
    print(f"{user_name} wins the set.... One point for {user_name}")
    human_point += 1
  elif computer_input == 3 and user_input == 2:
    print("Computer wins the set.... One point for Computer ")
    computer_point += 1
  elif computer_input == 3 and user_input == 3:
    print("It is a tie.  One point each ")
    human_point += 1
    computer_point += 1 
  
if human_point > computer_point :
  print(f"\n{user_name} wins.......")
  print(f"Computer : 'Nice game {user_name}'")
elif computer_point == human_point :
  print("\nIt is a tie.....")
  print(f"Computer : 'It has been a good play {user_name}...'")
else:
  print("\nComputer wins the Game....")
  print("Computer : 'Haha loser.....'")

print("\n\nThanks for playing my game....\n")
print("   * LAUGHS SACARASTICALLY *  ")
