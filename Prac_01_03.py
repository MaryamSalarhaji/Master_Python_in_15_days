#Write a program to check if a number is even or odd.
number = input("Please enter a number:")
try:
    num_int = int(number)
except:
    print("Enter a valid number!")
    exit()

if num_int % 2 == 0:
    print("The given number is even")
else:
    print("The given number is odd")
