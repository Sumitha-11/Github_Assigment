"""
Split in Half
Given a string. Split it into two equal parts. Swap these parts and return the result.
If the string has odd characters, the first part should be one character greater than the second part.
Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.

"""
def swap(str):
    length = len(str)
    if length % 2 != 0:
        str1 = str[:(length//2)+1]
        str2 = str[(length//2)+1:]
        return str2+str1
    else:
        str1 = str[:(length//2)]
        str2 = str[(length//2):]
        return str2+str1

print(swap('bbbbbcaaaaa'))
print(swap('bbbbaaaa'))
