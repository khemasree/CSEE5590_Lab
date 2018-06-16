import numpy as ny

# Generating the array of size 15 starting from 0 to 20
x=ny.random.randint(0,20,size=15)

# Print the array
print("Randomly Generated array is :" ,x)

# Using bincount to get the frequent items in the list
freqitem=ny.bincount(x)

# Print the items that appear frequently in the list
print("Most frequent item in the list is :",ny.argmax(freqitem))