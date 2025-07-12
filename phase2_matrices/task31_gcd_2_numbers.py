def gcd_of_number(n,m):
    arr1 = []
    arr2 = []
    arr3 = []
    for i in range(1, n):
        if n % i == 0:
            arr1.append(i)
    for j in range(1, m):
        if m % j == 0:
            arr2.append(j)

    for element in arr1:
        if element in arr2 and element not in arr3:
            arr3.append(element)        
    
    max_element = max(arr3)

    return max_element


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Highest gcd:", gcd_of_number(num1,num2))


