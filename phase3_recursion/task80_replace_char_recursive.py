def replace_char(s, j, k):
    if len(s) == 0:
        return 0
    if s[0] == j:
        k == j
        s[0] == k
        return 1 + replace_char(s[1:], j, k)
    else:
        return replace_char(s[1:], j, k)

sentence = input("Enter a string: ")
elem1 = input("Enter the character to replace (Case sensitive): ")
elem2 = input("Enter the character to be replaced with(Case sensitive): ")

rep = replace_char(sentence, elem1, elem2)
print("Replaced string: " ,replace_char)
