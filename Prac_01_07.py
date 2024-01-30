# Write a program that converts a given number of days  into years, weeks, and days.
days = input("Enter number of days:")
try:
    num_days = int(days)
except:
    print("Enter a valid number!")
    exit()
def years_weeks_days (num_days):
    years = int(num_days / 365)
    weeks = int(((num_days % 365) / 7))
    number_days = int(((num_days % 365) % 7))
    return "The number of year is:", years, "The number of weeks is:", weeks, "The number of days is:", number_days

print(years_weeks_days(num_days))
