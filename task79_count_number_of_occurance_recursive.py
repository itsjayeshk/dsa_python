def spec_char(s, j):
    if len(s) == 0:
        return 0
    if s[0] == j:
        return 1 + spec_char(s[1:], j)
    else:
        return spec_char(s[1:], j)

sentence = input("Enter a string: ")
elem = input("Enter the character to count (Case sensitive): ")

count = spec_char(sentence, elem)
print("✅ Number of occurrences of", elem, "is:", count)
