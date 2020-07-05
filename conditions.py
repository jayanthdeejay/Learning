# Chapter 5: If Statements

cars = ['audi', 'bmw', 'tesla', 'toyota']

for car in cars:
    # tests equality
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'Audi'
print(car == 'audi') # returns False as string comparision is case sensitive
print(car.lower() == 'audi') # Ture

# test of inequality

animal = 'dog'
if animal != 'cat':
    print("Yes, Cats are not Dogs!")

# Numerical comparisions
print("\nNumerical Comparisions:")
age = 99
print(age == 99) # True
print(age != 64) # True
print(age > 25) # True
print(age < 30) # False
print(age > 100) # False
print(age < 65) # False
print(age <= 99) # True
print(age <= 98) # False
print(age >= 64) # True
print(age >= 128) # False

# Use 'and' and 'or' to use multiple conditions
personOneAge = 22
personTwoAge = 25
if personOneAge >= 18 and personTwoAge >= 18:
    print("Yes, they are legally allowed to marry")

personOneAge = 17
personOneLicensed = False
personTwoAge = 25
personTwoLicensed = True

if (personOneAge >= 18 and personOneLicensed) or (personTwoAge >= 18 and personTwoLicensed):
    print("Person is allowed to drive in the precense of the other")

# Check the precense of a value in a list using 'in' keyword
availableCources = ['algorithms', 'calculus', 'psychology', 'philosophy']
requestedCourseOne = 'zoology'
requestedCourseTwo = 'calculus'
if requestedCourseOne in availableCources:
    print('Student can take ' + requestedCourseOne + ' as it is available')
else:
    print('Student cannot take ' + requestedCourseOne + ' as it is not available')

if requestedCourseTwo in availableCources:
    print('Student can take ' + requestedCourseTwo + ' as it is available')
else:
    print('Student cannot take ' + requestedCourseTwo + ' as it is not available')

# Check if a value does not exist in a list using 'not in' keyword
guests = ['elon', 'bernie', 'trevor', 'chapelle']
user = 'donald'
if user not in guests:
    print(user.title() + ", Fuck Offfff! You are not on the guest list!")

# Boolean expression, we have already used them before we reached Otherwise
# checkout lines 42-45

# We have also used if else statements already. Checkout 54-62

# if elif else blocks

age = 14
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $5")
else:
    print("Your admission cost is $10")

# slightly different logic with less code
age = 2
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price))

# more elifs
age = 32
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price))

# You don't need an else block in the end. if, elifs are enough
# else can be too generic and can sometimes causing malicious code to pass undetected

# Exercise
age = 32
if age < 2:
    print("You're just a baby!\n")
elif age >= 2 and age < 4:
    print("You are a toddler!\n")
elif age >= 4 and age < 13:
    print("You are a kid!\n")
elif age >= 13 and age < 20:
    print("You are a teenager!\n")
elif age >= 20 and age < 65:
    print("You are an adult!\n")
elif age >= 65:
    print("You are an elder!\n")

# Special conditions
toppingsReq = ['mushrooms', 'peppers', 'cheese']
for topping in toppingsReq:
    print("Adding " + topping)
print("\nFinished making Pizza!\n")

toppingsReq = ['mushrooms', 'peppers', 'cheese']
for topping in toppingsReq:
    if topping == 'peppers':
        print("Sorry, we are out of peppers!")
    else:
        print("Adding " + topping)
print("\nFinished making Pizza!\n")

# Dealing with empty Lists
toppingsReq = []
if toppingsReq:
    for topping in toppingsReq:
        print("Adding " + topping)
    print("\nFinished making Pizza\n")
else:
    print("Are you sure you want a plain pizza?\n")

# Multiple lists
toppingsAvail = ['mushrooms', 'olives', 'peppers', 'pepperoni', 'pineapple', 'cheese']
toppingsReq = ['mushrooms', 'fries', 'cheese']

for topping in toppingsReq:
    if topping in toppingsAvail:
        print("Adding " + topping)
    else:
        print("Sorry, we don't have " + topping)
print("\nHoney, pizza is here!")
