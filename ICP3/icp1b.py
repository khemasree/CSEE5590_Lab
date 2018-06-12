# Take the input from user
input = input("Please enter a sentence")

# Initialize the variable to 0
count=0
#vowels="aeiou"

# create an empty set
setsam=set()

# iterate each word in the input and check for vowels
for i in input:
    # convert into lower case
    ilow = i.lower()

    # check for vowels and add it to the set, if already the word is not in the set
    if ilow == 'a' or ilow == 'e' or ilow == 'i' or ilow == 'o' or ilow == 'u':
        if ilow in setsam:
            count=count
        else:
            count = count+1
            setsam.add(ilow)
            #print(setsam)
print("The vowels are:", count)




