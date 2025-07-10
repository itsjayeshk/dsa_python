def sum_array(arr):
    return sum(arr)

def max_element(arr):
    return max(arr)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Main code
n = int(input("Enter the number of elements in array: "))
arr = []

for i in range(n):
    element = int(input("Enter an element in array: "))
    arr.append(element)

print("Sum of all elements:", sum_array(arr))
print("Maximum element:", max_element(arr))

for num in arr:
    if is_prime(num):
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")


   
