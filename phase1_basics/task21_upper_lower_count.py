lower = 0
higher = 0
sent = input("Enter a sentence: ")

for i in sent:
    if i.islower():
        lower += 1
    elif i.isupper():
        higher += 1

print("Lower:", lower)
print("Higher:", higher)