def bubble_sort(n, arr, ele, index = 0):
    is_present = True
    if n % 2 == 0:
        if ele > arr[n / 2]:
            bubble_sort(n, arr, ele, index = (n / 2))
            return True
        elif ele < arr[n / 2]:
            bubble_sort(n / 2, arr, ele, index = 0)
            return True
        else:
            return False
    else: 
        if ele > arr[(n + 1) / 2]:
            bubble_sort(n, arr, ele, index = ((n + 1) / 2))
            return True
        elif ele < arr[(n + 1) / 2]:
            bubble_sort((n + 1) / 2, arr, ele, index = 0)
            return True
        else:
            return False

arr = []
n = int(input("Enter the number of elements you want in array: "))
for i in range(n):
    element = int(input("Enter the element: "))
    arr.append(element)
arr.sort()
ele = int(input("Enter the element you want to search: "))
bubble_sort(n, arr, ele, index = 0)

    