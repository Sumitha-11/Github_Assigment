"""
Even First
Your input is an array of integers, and you have to reorder its entries so that the even entries appear first.
You are required to solve it without allocating additional storage (operate with the input array).
Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

"""

def even_first(arr):
    index = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even_num = arr[i]
            arr.remove(arr[i])
            arr.insert(index,even_num)
            index += 1
    return (arr)

print(even_first([7, 3, 5, 6, 4, 10, 3, 2]))
print(even_first([12, 34, 45, 9, 8, 90, 3]))
print(even_first([0,1,2,3,4,5,6,7,8]))


