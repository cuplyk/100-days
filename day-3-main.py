#----------------If and Else

# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster!")
    
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


#------------------------Odd or Even

# chech_num = int(input("Which number do you want to check? "))

# modulo = chech_num % 2

# if modulo == 1:
#     print("This is an odd number")
# else:
#     print("This is an even number")

#-------------------------------------BMI Upgrade Calculator

# BMI Calculator

# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))

# bmi = round(weight / height ** 2)

# if bmi < 18.5:
#     print(f"You BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"You BMI is {bmi}, you have a normal weight.")
# elif bmi  < 30:
#     print(f"You BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#     print(f"You BMI is {bmi}, you are obese.")
# else:
#     print(f"You BMI is {bmi}, you are clinically obese.")

#----------------------------------Leap Year
# year_check = int(input("Which year do you want to check? "))

# if year_check % 4 == 0:
#     if year_check % 100 == 0:
#         if year_check % 400 ==0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")    


#----------------------------------   Rollercoaster  
# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster!")
    
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickes are $7.")
#     elif age >= 45 and age <= 55:
#         print("You can ride for free!")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")

#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3
#     print(f"Your final bill is ${bill}")
# else:
#      print("Sorry, you have to grow taller before you can ride.")


#---------------------Pizza Order

# print("Welcome to Python Pizza Deliveries")
# size = input("What pizza do you want? S, M, L\n")
# add_pepperoni = input("Do you want pepperoni? Y or N\n")
# extra_cheese = input("Do you want extra cheese? Y or N\n")

# bill = 0


# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3    
    
# if extra_cheese == "Y":
#     bill +=1

# print(f"Your final bill is ${bill}")


#-------------------------------Love Calculator
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")

# name_lower = name1 + name2
# name_lower = name_lower.lower()


# name_count_T = name_lower.count("t")
# name_count_R = name_lower.count("r")
# name_count_U = name_lower.count("u")
# name_count_E = name_lower.count("e")
# name_count_L = name_lower.count("l")
# name_count_O = name_lower.count("o")
# name_count_V = name_lower.count("v")
# name_count_E = name_lower.count("e")
# count_total_true = (name_count_T + name_count_R + name_count_U + name_count_E)
# count_total_love = (name_count_L +name_count_O + name_count_V + name_count_E)
# count_total = int(str(count_total_true) + str(count_total_love))

# if (count_total < 10) and (count_total > 90):
#     print(f"Your score is {count_total} you go together like coke and mentos.")
# elif count_total >= 40 and count_total <= 50:
#     print(f"Your score is {count_total}, you are alright together.")
# else:
#     print(f"Your score is {count_total}.")

#-----------------------------Treasure Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


pass1 = input('You\'re at a crossroad, where do you want to go? Type "Left" or "Right". \n').lower()
if pass1 == "left":
    pass2 = input('You\'re come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if pass2 == "wait":
        pass3 = input("You arrive at the island unharmed. There is a house with 3 dors. One red, one yellow and one blue. Witch color do you choose? \n").lower()
        if pass3 == "red":
            print("It is a room full of fire. Game over. \n")
        elif pass3 == "blue":
            print("You enter a room of beasts. Game over.\n")
        elif pass3 == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("Game over.")
    else:
        print("Attached by trout. Game over.")
else:
    print("Fall into a hole. Game Over.")









