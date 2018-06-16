input = input("Please enter the sentence")

# Initialize all the variables with default values
individualwords=input.split()
wordset=individualwords
longestword = ''
reversesen = ''
print(wordset)

# For even number of words print the middle two words
if len(wordset) % 2 == 0 :
    print("Middle Words are: ["+individualwords[int(len(wordset)/2 - 1)]+","+individualwords[int(len(wordset)/2)]+"]")

# And for odd, Print the middle word
else:
    middleword=int(len(wordset)/2)
    print("Middle Word is: ["+individualwords[middleword]+"]")

# Reverse individual words in a sentence and append that to the variable created for storing the reversed sentence
for i in wordset:
    reverse = i[::-1]
    reversesen = reversesen+' '+ reverse

    # If the new word is greater than the longest word then reassign longest word to the new word
    if len(i) > len(longestword):
        longestword = i
print("The longest word is: " + longestword)
print("Sentence with reverse words is: " + reversesen)
