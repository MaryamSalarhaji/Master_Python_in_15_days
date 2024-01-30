#Calculate the sum of two numbers entered by the user
num_1 = input("Enter number1:")
num_2 = input("Enter number2:")

try:
    num_1_f = float(num_1)
    num_2_f = float(num_2)
    total = num_1_f + num_2_f
except:
    print("Enter a valid number")
    exit()

print("The sum is:", total)

