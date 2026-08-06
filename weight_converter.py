# Python Weight Converter

weight = float(input("Enter your weight: "))
unit = input("Is this weight in (K)g or (L)bs? ").upper()

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "L":
    weight = weight / 2.20590
    unit = "Kg"
else:
    print (f"{unit} is not valid ") 

print (f"Your weight is: {weight:.2f} {unit} ")
exit()
