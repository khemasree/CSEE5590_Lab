import random

a=random.randint(0,9)
userguess=False
while userguess==False :
    user_input = int(input("Guess the digit:"))
    if user_input==a:
        userguess=True
        print("Your answer is perfect, congratulations!")
    if user_input > a :
        print("Your answer is higher than required")
    elif user_input < a :
        print("Your answer is lower than required")
