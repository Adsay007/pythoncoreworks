#find BMI 
# formula = weight/height raise to 2

weight = float(input("Enter Weight in Kg : "))
heightCm = float(input("Enter Height Cm : "))
heightM= heightCm/100

bmi = weight/(heightM**2)

print(f"Bmi is : {bmi}")