filepath = "C:\Hema files\Python\Sample1.txt"

num_words = 0

with open(filepath) as fp:
    for line in fp:
        words = line.split()
        num_words = len(words)
        print(line)
        print(num_words)