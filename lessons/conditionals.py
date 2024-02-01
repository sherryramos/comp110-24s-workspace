"""Demonstrate behavior of conditionals."""

user_input: str = input("Pick a number: ")
print(type(user_input))
user_number: int = int(user_input)
print (type(user_number))

# if user_number is less than 10, print "small"

if user_number < 10:
    print("small")
else: # user_number >= 10
    print("numero big")

# if user_number is even, print "even"
if user_number % 2 == 0:
    print("even")
else: # user_number is odd
    print("odd")

if user_number > 10:
    print("\U0001F978")

print(user_number)

michis: int = 10
print(user_input + " + " + str(michis) + " donuts!")
print(f"I ate { michis } donuts!")

name: str = "Michi"
age_turning: int = 19
print(f"Hi {name}, you are almost {age_turning}!")

age: int = 21
msg: str = f"You are {age}!"
print(msg)