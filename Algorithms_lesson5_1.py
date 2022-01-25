"""Selection Sort
Implement the selection sort algorithm that is sorting in descending order.
"""


def selection(arr):
    for i in range(len(arr)):
        max_index = i
        for j in range(i+1,len(arr)):
            if arr[j] > arr[max_index]:
                 max_index = j

        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr

print(selection([2,1,4,3,6,8]))