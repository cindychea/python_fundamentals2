def temperature_converter():
    print("What is the temperature in Fahrenheit?")
    return (int(input()) - 32) * 5/9

celsius_temp = temperature_converter()

print("The temperature is {:.0f} degrees Celsius.".format(celsius_temp))
    