num = int(input("Enter a number: "))
freq = [0] * 10

while num > 0:
    dig = num % 10
    freq[dig] += 1
    num = num // 10

for i in range(10):
    print(f"Frequency of {i}: {freq[i]}")