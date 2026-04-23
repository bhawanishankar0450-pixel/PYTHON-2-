#Modules (Temperature)

import Temperature_Module as TM

print("----------------------------------------------------------")
print("Which conversion do you want to perform?")
print("1.Celcius to Fahrenheit\n2.Fahrenheit to Celcius\n3.Celcius to Kelvin")
option = int(input(":"))
print("----------------------------------------------------------")

match option:
    case 1:
        Celcius = float(input("Enter celcius to convert to fahrenheit: "))
        print(f"{Celcius} C in Fahrenheit = {TM.fahrenheit(Celcius)}")

    case 2:
        Fahrenheit = float(input("Enter celcius to convert to fahrenheit: "))
        print(f"{Fahrenheit} F in Celcius = {TM.celcius(Fahrenheit)}")

    case 3:
        celcius = float(input("Enter celcius to convert to Kelvin: "))
        print(f"{celcius} C in Kelvin = {TM.kelvin(celcius)}")

    case _:
        raise ValueError("Invalid Input")