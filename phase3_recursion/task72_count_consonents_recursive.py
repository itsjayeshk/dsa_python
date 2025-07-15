def count_conso(s):
    s = s.lower()
    if len(s) == 0:
        return 0
    if s[0].isalpha() and s[0] not in 'aeiou':
        return 1 + count_conso(s[1:])
    else:
        return count_conso(s[1:])

sentence = input("Enter a string: ")
conso_count = count_conso(sentence)
print("✅ Number of consonants:", conso_count)
