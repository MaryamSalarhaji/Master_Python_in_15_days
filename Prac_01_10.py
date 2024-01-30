# Implement a program that swaps the values of two variables.
a= int(input("Enter a number:"))
b= int(input("Enter a number:"))

def swap (a, b):
    a, b = b, a
    return "The swap of a is:", a, "The swap of b is:", b

print(swap(a, b))