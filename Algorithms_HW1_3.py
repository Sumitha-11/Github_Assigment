"""
Count odd and even numbers. Count odd and even digits of the whole number.
Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).

"""

def count_odd_even_num(n):
    even = 0
    odd = 0
    while n > 0:
        num = n % 10
        n = n // 10
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    print("count of even number:", even)
    print("count of odd number:", odd)

(count_odd_even_num(34560))
