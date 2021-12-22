"""Find max number from 3 values, entered manually from a keyboard.
Example: 124, 21, 32. Result = 124."""

def max_num(a,b,c):

    if (a>b)and(a>c):
        return a

    elif (b>a)and(b>c):
        return b
    return c

a=int(input("Enter number a :"))
b=int(input("Enter number b :"))
c=int(input("Enter number c :"))
print(max_num(a,b,c))



