"""Given a string, determine if it consists of all unique characters.
For example, the string 'abcde' has all unique characters and should return True.
The string 'aabcde' contains duplicate characters and should return False."""

def unique_characters(str):
    if str.isnumeric():
        return "Invalid Input"
    if str == "":
        return None
    else:
        for letter in str:
            if str.count(letter) != 1:
                return False
        return True


print(unique_characters('abcde'))
print(unique_characters('aabcde'))
print(unique_characters(""))
print(unique_characters('12344'))