"""
Given an array of integers ,write a function to move all the zeros to the end while maintaining the
relative order of the others elements

input: 0 4 0 3 1 2
output: 4 3 1 2 0 0
"""

def move_zeros(arr):
    count = 0
    for i in arr:
        if i == 0:
            new = arr.remove(i)
            count += 1
    for i in range(count):
        arr.append(0)
    return (arr)

print(move_zeros([0,4,0,3,1,2]))
print(move_zeros([5,0,3,0,0,4,0]))

