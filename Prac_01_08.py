#Given a list of integers, find the sum of all positive numbers.
def sum_positive(num_list):
    sum =0
    for num in num_list:
        if num>=0:
            sum =num + sum
        else:
            sum = sum
    return "The sum of positive number is:", sum

print(sum_positive([-1, 4, 5, -10, 12]))