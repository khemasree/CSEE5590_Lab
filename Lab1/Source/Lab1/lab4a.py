# List of students attending python class
pythonlist={'Bob','Billy','Sara'}

# List of students attending web applications class
webApplicationlist={'John','James','Bob'}

# List of students attending both
attendingboth = pythonlist & webApplicationlist
print("The students attending both the classes are: ", attendingboth)

# List of students not common in both the classes
notcommon=pythonlist ^ webApplicationlist
print("The students who are not common in both the classes are: ", notcommon)
