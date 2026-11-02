# Tempreature Convertor

unit = input("Is this tempreature in Celsius or Fahrenheit (C or F): ")
tempreature = float(input("Enter the tempreature: "))

if unit == 'C':
    tempreature = round((9 * tempreature) / 5 + 32, 1)
    print(f"The tempreature in Fahrenheit is {tempreature}°F")
elif unit == 'F':
    tempreature = round((tempreature - 32) * 5 / 9, 1)
    print(f"The tempreature in Celsius is {tempreature}°C")
else:
    print(f"{unit} is an invalid unit of measurement")