import random

# random_int = random.randint(0, 5)
# print(random_int)

# randomFloat = random.random() * 5
# print(randomFloat)

# love_score = random.randint(1, 100)
# print(f"Your score is {love_score}.")

#----------------------------------Heads or Tails
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# eandom_side = random.randint(0, 1)
# if eandom_side == 1:
#     print("Heads")
# else:
#     print("Tails")

#---------------

# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", 
# "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire",
#  "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont",
#   "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",
#    "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", 
#    "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota",
#     "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
#      "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming",
#       "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# states_of_america[2]

# states_of_america.extend(["Budapest", ["Jack"]])

#------------------

# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# # Split string method
# names_to_give = input("Give me everybody's names, seperated by a comma. ")
# names = names_to_give.split(", ")

# # random_name_len = len(names)

# # random_choice = random.randint(0, random_name_len - 1)
# # person_who_will_pay = names[random_choice]

# person_who_will_pay = random.choice(names)
# print(f"{person_who_will_pay} is going to buy the meal today!")

#---------------------------------------Treasure Map
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")

# horizontal = int(position[0])
# vertical = int(position[1])
# #Method 1
# # selected_row = map[vertical -1]
# # selected_row[horizontal -1] = "X"
# #Method 2
# map[vertical -1][horizontal -1] = "X"

# print(f"{row1}\n{row2}\n{row3}")


#-------------rock-paper-scissors-game
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
game_images = [rock, paper, scissors]
user_choise = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors"))
print(game_images[user_choise])

computer_choice = random.randint(0, 2)
print(f"Computer chose: ")
print(game_images[computer_choice])

if user_choise >= 3 or user_choise < 0:
      print("You typed an invalid number, you lose!")
elif user_choise == 0 and computer_choice == 2:
      print("You win!")
elif computer_choice == 0 and user_choise == 2:
      print("You lose")
elif computer_choice > user_choise:
      print("You lose")
elif user_choise > computer_choice:
      print("You win!")
elif computer_choice == user_choise:
      print("It is a draw")
