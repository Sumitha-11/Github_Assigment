"""
Two Lowest Elements
When given a list of elements, find the two lowest elements.
They can be equal to each other or different.
Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3
"""
#
# def lowest_elements(arr):
#     arr1 = sorted(arr)
#     return arr1[:2]
#
# print(lowest_elements([198, 3, 4, 9, 10, 9, 2]))

def lowest_elements(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr[:2]

print(lowest_elements([198, 3, 4, 9, 10, 2]))

