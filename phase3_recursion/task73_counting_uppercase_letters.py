def count_upper(s):
    if len(s) == 0:
        return 0
    if s[0].isupper():
        return 1 + count_upper(s[1:])
    else:
        return count_upper(s[1:])

sentence = input("Enter a string: ")
upper_count = count_upper(sentence)
print("✅ Number of uppercase letters:", upper_count)
