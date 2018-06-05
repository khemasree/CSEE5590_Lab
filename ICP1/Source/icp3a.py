import random

user_input=int(input("Guess the digit:"))

a=random.randint(0,9)
if user_input > a :
    print("Your answer is higher than required")
elif user_input < a :
    print("Your answer is lower than required")
else :
    print("Your answer is perfect, congratulations!")