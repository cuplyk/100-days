# num_char = len(input('What is your name?'))
# new_num_char = str(num_char)
# print("You name has " + new_num_char + " caracter.")

#-----------------------------Data Types Exercise

# two_digital_number = input("Type a two digit number: ")

# first_digit = two_digital_number[0]
# second_digit = two_digital_number[1]

# result = (int(first_digit) + int(second_digit))
# print(result)


#----------------------------OPERATIONS 

# Pemdas
# Parentheses = ()
# Exponents = **
# Multiplication *
# Division /
# Additional +
# Subtraction -

# ---------------print( 3 * (3 + 3 / 3 - 3))


# BMI Calculator

# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))

# bmi = weight /(height**2)
# bmi_as_int = int(bmi)

# print(bmi_as_int)

# print(round(2.88888888888, 2))


# -------------------------Your Life in Weeks
# age = int(input("What is your current age?"))

# days = 365 * age
# weeks = 52 * age
# months = 12 * age

# print(f"You have {days} days, {weeks} weeks, and {months} months left.")


# age = input("What is your current age?")

# age_as_int = int(age)

# years_remaining = 90 - age_as_int
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining * 12 

# you_age = f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months left."

# print(you_age)


# -------------------Calculator

print("Welcome to the tip calculator.")
#Input from user
bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip wuld you like to give? 10,12, or 15?"))
split_the_bill = int(input("How many people to split the bill?"))
#The operations
bil_with_tip = percentage / 100
total_tip_amount = bill * bil_with_tip
total_bill = bill + total_tip_amount
bill_per_person = total_bill / split_the_bill
finall_amount = round(bill_per_person, 2)

print(f"Eachi person should pay: ${finall_amount}")
