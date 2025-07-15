def count_num(s):
    if len(s) == 0:
        return 0
    if s[0].isdigit():
        return 1 + count_num(s[1:])
    else:
        return count_num(s[1:])

sentence = input("Enter a string: ")
num_count = count_num(sentence)
print("✅ Number of Numbers:", num_count)
