vowels = 0
consonants = 0
sent = input("Enter a sentence: ").lower()

for i in sent:
    if i.isalpha():
        if i in 'aeiou':
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)