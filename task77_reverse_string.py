def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]


text = input("Enter a string: ")
reversed_text = reverse_string(text)
print("Reversed string:", reversed_text)
