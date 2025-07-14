def count_special(s):
    if len(s) == 0:
        return 0
    if not s[0].isalnum():
        return 1 + count_special(s[1:])
    else:
        return count_special(s[1:])

sentence = input("Enter a string: ")
special_count = count_special(sentence)
print("✅ Number of special characters:", special_count)
