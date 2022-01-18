
"""
Increment a Number
Write a program that takes as input an array of digits encoding a nonnegative decimal integer D and updates the array to represent the integer D + 1.
For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].
"""
def increment_num(arr):
    length = len(arr)
    carry = 1

    for i in range(1, length + 1):
        if arr[-i] == 9 and carry == 1:
            carry = 1
            arr[-i] = 0
        else:
            arr[-i] += carry
            carry = 0

    if carry == 1:
        arr.insert(0,1)

    return arr



print(increment_num([1,7,8,9]))
print(increment_num([1,9,9]))
print(increment_num([1,2,9]))
print(increment_num([1,2,2]))
print(increment_num([9,9]))
print(increment_num([9]))