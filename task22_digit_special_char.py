digit = 0
spec = 0
sent = input("Enter a sentence: ")

for i in sent:
    if i.isdigit():
        digit += 1
    elif not i.isalnum() and not i.isspace():
        spec += 1

print("Digit:", digit)
print("Special Char:", spec)