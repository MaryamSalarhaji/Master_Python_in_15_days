#Given a list of numbers, find the maximum and minimum values.
num_list=list()

while True:
    number = input("Please enter a number:")
    if number== 'done':
        break
    try:
        number_int = int(number)
        num_list.append(number_int)
    except:
        print("Enter a valid number")
    continue

maximum = max(num_list)
minimum = min(num_list)

print("The list of number is:", num_list)

print("The maximum is:", maximum)
print("The minimum is:", minimum)
