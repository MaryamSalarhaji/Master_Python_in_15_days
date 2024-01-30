#Write a Python program to calculate the area of a rectangle given its length and width.
length = input("Enter a length of rectangle:")
width = input("Enter a width of rectangle:")
try:
    length_f = float(length)
    width_f = float(width)
    area = length_f * width_f
except:
    print("oops, enter a valid number")
    exit()
print("The area of the rectangle is:", area)