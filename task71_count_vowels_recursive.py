def count_vowels(s):
    s = s.lower()
    if len(s) == 0:
        return 0
    if s[0] in 'aeiou':
        return 1 + count_vowels(s[1:])
    else:
        return count_vowels(s[1:])

# Input
sentence = input("Enter a string: ")
vowel_count = count_vowels(sentence)
print("✅ Number of vowels:", vowel_count)
