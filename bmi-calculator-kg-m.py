print("################################")
print("#####    BMI CALCULATOR    #####")
print("################################")
print("#####   Coded by @Cmlohr   #####")
print("################################")
print("                                ")

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

## Calculation
bmi = int(weight) / float(height) ** 2

## Conversion to float
bmi_float = float(bmi)

## Formating to the second decimal place
nbmi = "{:.2f}".format(bmi_float)

## Conditions for BMI
if bmi_float >= 35:
  print(f"{nbmi}"+" Clinically Obese")
elif bmi_float > 30:
  print(f"{nbmi}"+" Obese")
elif bmi_float > 25:
  print(f"{nbmi}"+" Overweight")
elif bmi_float >= 18.5:
  print(f"{nbmi}"+" Healthy Weight")
else:
  print(f"{nbmi}"+" Underweight")