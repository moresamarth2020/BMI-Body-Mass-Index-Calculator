def bmi_calculator():
    print("----- BMI CALCULATOR -----\n")

    weight = float(input("Enter your weight (in kg): "))
    height = float(input("Enter your height (in meters): "))

    bmi = weight / (height ** 2)

    print(f"\nYour BMI is: {bmi:.2f}")

    if bmi < 18.5:
        status = "Underweight"
    elif 18.5 <= bmi < 25:
        status = "Normal weight"
    elif 25 <= bmi < 30:
        status = "Overweight"
    else:
        status = "Obese"

    print(f"Health Status: {status}")

bmi_calculator()
