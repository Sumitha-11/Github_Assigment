"""Below The Arithmetical Mean
When given a list, the program should return a list of all the elements below the original list’s
arthimetic mean. The arithmetical mean is the sum of all elements divided by the number of elements.
Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]
"""

def arthimetic_mean(arr):
    lst = []
    AM = sum(arr) / len(arr)
    for i in arr:
        if i < AM :
            lst.append(i)
    return lst

print(arthimetic_mean([1, 3, 5, 6, 4, 10, 2, 3]))

