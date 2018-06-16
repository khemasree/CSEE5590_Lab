import re

# Take input from user
password = input("Please enter your password")
flag = 0

# While true repeat the loop, and if any of the condition is not set then break the loop
while(True):
 if (len(password) > 6 and len(password) < 16):

    if not re.search("[A-Z]", password):
       print("Password must contain at least one upper character ")
       break

    elif not re.search("[0-9]", password):
       print("Password must contain at least one digit")
       break

    elif not re.search("[@$!*]", password):
       print("Password must contain at least one special character")
       break

    else:
       print("Password is valid")
       break

 else:
    print("Password length must be greater than 6 and less than 16")
    break


