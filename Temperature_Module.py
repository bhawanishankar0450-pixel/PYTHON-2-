def fahrenheit(celcius):

    result = (celcius * 9/5) + 32

    return(f"{result:.2f}F")


def celcius(farenheit):

    result = (farenheit - 32) * 5/9

    return(f"{result:.2f}C")


def kelvin(celcius):

    result = celcius + 273.15

    return(f"{result:.2f}K")