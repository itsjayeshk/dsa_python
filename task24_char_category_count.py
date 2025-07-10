space = 0
digit = 0
spec = 0
alpha = 0
sent = input("Enter a sentence: ")

for i in sent:
    if i.isspace():
        space += 1
    elif i.isdigit():
        digit += 1
    elif i.isalpha():
        alpha += 1
    else:
        spec += 1

print("Space:", space)
print("Numbers:", digit)
print("Alphabets:", alpha)
print("Special char:", spec)