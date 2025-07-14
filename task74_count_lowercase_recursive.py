def count_lower(s):
    if len(s) == 0:
        return 0
    if s[0].islower():
        return 1 + count_lower(s[1:])
    else:
        return count_lower(s[1:])

sentence = input("Enter a string: ")
lower_count = count_lower(sentence)
print("✅ Number of lowercase letters:", lower_count)
