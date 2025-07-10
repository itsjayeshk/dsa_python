space = 0
sent = input("Enter a sentence: ")

for i in sent:
    if i.isspace():
        space += 1

print("Space:", space)