"""
Compute the sum of digits in all numbers from 1 to n. When a user enters a number n, find the sum of digits in all numbers from 1 to n.
Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

"""

def sum_of_digits(n):
    sum=0
    for i in range(1,n+1):
        sum = sum+i
    return sum

n=int(input("Enter a number:"))
print("Sum of digit:",sum_of_digits(n))