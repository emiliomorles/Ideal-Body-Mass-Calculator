# Ideal Body Mass Calculator
height = float(input("enter your height in m (example: 1.83): "))
weight = float(input("enter your weight in kg (example: 70): "))

bmi = (weight / (height ** 2))
bmi_result = float(("%.2f" % bmi))
bmi_result = round(bmi_result)

if bmi_result < 18.5:
  print(f"Your BMI is {bmi_result}, you are underweight.")
elif bmi_result >= 18.5 and bmi_result < 25:
  print(f"Your BMI is {bmi_result}, you have a normal weight.\nCongratulations!")
elif bmi_result >= 25 and bmi_result < 30:
  print(f"Your BMI is {bmi_result}, you are slightly overweight.")
elif bmi_result >= 30 and bmi_result < 35:
  print(f"Your BMI is {bmi_result}, you are obese.")
else:
  print("You are clinically obese.")