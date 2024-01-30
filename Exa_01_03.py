#Convert temperature from Celcius to Farenheit
temp=input("Enter temperature in Celcius:")
try:
    temp_celc=float(temp)
    temp_Fare= ((temp_celc)*(9/5))+32
except:
    print("OOps, enter a valid number")
    exit()
print("Temperature in Farenheit is:", temp_Fare)