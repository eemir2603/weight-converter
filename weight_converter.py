# Python Weight Converter

weight = float(input("Enter your weight: "))
unit = input("Is this weight in (K)g or (L)bs? ").upper()

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print (f"Your weight is: {weight:.2f} {unit} ")

elif unit == "L":
    weight = weight / 2.20590
    unit = "Kg"
    print (f"Your weight is: {weight:.2f} {unit} ")

else:
    print (f"{unit} is not valid ") 

exit()
