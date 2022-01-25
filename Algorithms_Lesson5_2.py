"""
Bubble Sort
Implement the bubble sort algorithm that is sorting in descending order.

"""
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i -1):
            if arr[j+1] > arr[j]:
                arr[j+1] , arr[j] = arr[j] ,arr[j+1]
    return arr


print(bubble_sort([2, 1, 4, 3, 6, 8]))