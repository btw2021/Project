
#     Data Types
#...1. String
#print("Hello"[4]) #--this is called subscript 
#print("Hello " + "345")
#..2. Integer 
#print(123 + 456)
#..3. Float
#3125.6
#..4. Boolean
#True
#False

# Data type Excercise 

# street_name = "Abbey Road"
# print(street_name[4] + street_name[7])  # the result would be yo 

#Type Error, checking and type conversion 

# num_char = len(input("What is your name? "))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.") # corrected by using type function
# print("Your name has " + num_chart + " characters.") # data type Error

#Excercise 
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# two_digit_number = input("Type a two digit number: ")
# first_digit = two_digit_number[0]
# second_digit = two_digit_number[1]
# result = int(first_digit) + int(second_digit)
# print(result)

#Math Operation 
# operations are based on PEMDASLR - parentheses, exponents, multiplicattion, division, addition, subtraction
# print (3 * 3 + 3 / 3 - 3) # example 1
# print(3 * (3 + 3) / 3 -3 ) # example 2

# BMI Calculator 
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# bmi = int(weight) / float(height) ** 2
# bmi_as_int = int(bmi)
# print(bmi_as_int)

#.... Number manipulation
     # the round() filter
# print(round(8 / 3))
# print(round(8 / 3, 2)) # rounding to two digits
# print(8 // 3) 

# result = 4 / 2
# result /= 2 # we can use +=, -+, */ or /=
# print(result)

# F string helps to avoid converting data types and writing long codes.
# score = 0
# height = 1.8
# isWinning = True
# print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

# name = input("What is your name? ") # example 1
# print(f"Hello, {name}")
# name = input("What is your name? ") # example 2
# print("Hello, " + name)

# age = 12  # example 3
# print(f"You are {age} years old")

# Excercise: Your life in weeks
# example out put you have 12410 days, 1768 weeks and 408 months left.

# age = input("what is your current age? ")

# age_as_int = int(age)
# years_remaining = 90 - age_as_int
# days_remaining = years_remaining * 365 
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining * 12

# message = f"You have {days_remaining} days,or {weeks_remaining} weeks,or {months_remaining} months or {years_remaining} years left."
# print(message)

# Excercise Tip Calculator

# print("Welcome to the tip calculator")
# # print("Welcome to the Payroll calculator!")
# bill = float(input("What was the total bill? $"))

# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill?"))
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)
# print(f"Each person should pay: ${final_amount}")

# Pyroll calculator project 
n = 1
while n < 5:

    print("Welcome to the payroll calculator!")
    #Employee Name
    employee = input("Employee Name: ")
    # Hours Worked 
    hours_worked = float(input("Hour Worked: "))
    extra_hours_worked = float(input("Extra Hour Worked: "))
    # Payment Rates 
    pay_rate = float(input("Pay Rate $: ")) 
    extra_hours_rate = 1.5 * pay_rate
    #Payements
    reg_pay = hours_worked * pay_rate  
    ext_pay = extra_hours_worked * extra_hours_rate
    gross_pay = reg_pay + ext_pay
    # Tax Rates
    fed_tax_rate = 0.10
    state_rate = 0.03
    fica_rate = 0.07

    #Total tax
    fed_tax = round(pay_rate * fed_tax_rate, 2)
    state_tax = round(pay_rate * state_rate, 2) 
    fica_tax = round(pay_rate * fica_rate, 2)
    total_tax = round(fed_tax + state_tax + fica_tax, 2)
    net_pay = round(gross_pay - total_tax, 2)

    print(f"Your gross payment is {gross_pay} dollars.")
    print(f"Your Total Federal tax is {pay_rate * fed_tax_rate} dollar.")
    print(f"Your State tax is {pay_rate * state_rate} dollar.")
    print(f"Your FICA payment is {fica_tax} dollar.")
    # print(f"Your FICA payment is {pay_rate * fica_rate} dollar.")
    print(f"Your total tax payed is {total_tax} dollar.")
    print(f"Your net payment is {net_pay} dollar.")
    print(f"Thank you dear {employee}!") 

    n += 1

    


  
















