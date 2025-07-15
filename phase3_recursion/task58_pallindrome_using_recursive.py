def reverse_num(n, rev=0):
    if n == 0:
        return rev
    else:
        return reverse_num(n//10,rev*10+n%10)
    
num = int(input("Enter a number: "))
rev = reverse_num(num)
if num == rev:
    print("✅ It is a palindrome number.")
else:
    print("❌ It is not a palindrome number.")   

