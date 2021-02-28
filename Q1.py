# Write a function, add_up(), which takes one integer as input and returns the sum of the integers
# from zero to the input parameter.The function should return 0 if a non-integer is passed in.

def add_up(n):

    try:
        result = sum(range(n + 1))
    except TypeError:
        result = 0
    return result

n=int(input("Enter the number to be added upto : "))

print('Addition from 0 to', n, 'is', add_up(n))
