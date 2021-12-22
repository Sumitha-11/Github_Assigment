def reverse_number(n):
    rev_num = 0
    while n > 0:
        num = n % 10
        n = n // 10
        rev_num = rev_num * 10 + num
    return rev_num

print(reverse_number(3456))