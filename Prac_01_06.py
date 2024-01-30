#Calculate the compound interest for a given principal amount, interest rate, and time period.
P = input("Enter a principle amount:")
r = input("Enter interest rate:")
t = input("Enter a time period:")
try:
    P_float = float(P)
    r_float = float(r)
    t_float = float(t)
    power = pow((1+r_float/100), t_float)
    compound_amount = P_float * power
except:
    print("Enter a valid number!")
    exit()

compound_interest = compound_amount-P_float

print("The principle amount is", compound_amount)