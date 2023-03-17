

n = int(input("The integer n : \n"))
words = {}

for i in range(0,n):
    word = input("Your Word : \n")
    if words.get(word):
        words[word] += 1
    else:
        words[word] = 1
        

print(f"{len(words)} ")


print(" ".join(map(lambda x: str(x), words.values())))