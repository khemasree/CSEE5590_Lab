# Take the input from user
sen=input("PLease enter a sentence")

# Split the sentence into words
words=sen.split()

# Sort the words list
words.sort()

# create an empty dictionary
wordsdic=dict()

# iterate through each word and add them to the dictionary, and if it is already there then skip
for i in words:
    if i in wordsdic:
        wordsdic[i]+=1
    else:
        wordsdic[i] = 1
print(wordsdic)

