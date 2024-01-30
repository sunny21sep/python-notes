# print("Hello World!")
# print("I Love Pizza")


# variable = a reusable container for storing a value
#                   a variable behaves as if it were the value it contains

# # Different ways of printing integer in between sentence 
# age = 21  

# print("You are " + str(age) + " years old")
# print("You are", age, "years old")
# print(f"You are {age} years old")

# # INTEGER
# age = 21
# players = 2
# quantity = 5

# print(f"You are {age} years old")
# print(f"There are {players} players online")
# print(f"You would like to buy {quantity} items")

# # FLOAT
# gpa = 3.2
# distance = 2.5
# price = 10.99

# print(f"Your gpa is {gpa}")
# print(f"You ran {distance}Km")
# print(f"The price is Rs{price}")

# # STRING
# name = "Bro"
# food = "pizza"
# email = "Bro123@gmail.com"

# print(f"Hello {name}")
# print(f"You like {food}")
# print(f"Your email is: {email}")

# # BOOLEAN
# online = True
# for_sale = False
# running = False

# print(f"Are you online?: {online}")
# print(f"Is the item for sale?: {for_sale}")
# print(f"Game running: {running}")

# # Define var. in one line
# x, y, z = 1, 2, 3
# a = b = c = 1

# print(x)
# print(y)
# print(z)
# print(a)
# print(b)
# print(c)


# type casting = The process of converting a value of one data type to another
#                          (string, integer, float, boolean)
#                          Explicit vs Implicit

# name = "Bro"
# age = 21
# gpa = 1.9
# student = True

# print(type(name))
# print(type(age))
# print(type(gpa))
# print(type(student)) 

# In Boolean Conversion , anything except 0 is True

# age = float(age)
# print(age)

# gpa = int(gpa)
# print(gpa)

# student = str(student)
# print(student)

# name = bool(name)
# print(name)

# # Implicit Typecasting
# x = 2
# y = 2.0
# x = x / y

# print(x)


# name = input("Enter your name: ")

# age = input("Enter your age: ")
# age = int(age)

# age = int(input("Enter your age: "))
# age = age + 1

# print(f"Hello {name}")
# print(f"You are {age} years old")

# ------------------------------------------------
# EXERCISE 1 MAD LIBS
# ------------------------------------------------
adjective1 = input("Enter an adjective: ")
noun = input("Enter a noun: ")
adjective2 = input("Enter an adjective: ")
verb = input("Enter a verb: ")
adjective3 = input("Enter an adjective: ")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw {noun}.")
print(f"{noun} was {adjective2} and {verb}ing.")
print(f"I was {adjective3}!")

# ------------------------------------------------
# EXERCISE 2 AREA CALC
# ------------------------------------------------
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

#area = length * width
#print(f"The area is: {area}cm^2")

# ------------------------------------------------
# EXERCISE 3 SHOPPING CART
# ------------------------------------------------
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${round(total, 2)}")

print("Sunny")
