def convert_cel_to_far(celsius):
    return round(celsius * 9/5 + 32, 2)

def convert_far_to_cel(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 2)

f_temp = float(input("Enter a temperature in degrees F: "))
print(f"{f_temp} degrees F = {convert_far_to_cel(f_temp)} degrees C")

c_temp = float(input("Enter a temperature in degrees C: "))
print(f"{c_temp} degrees C = {convert_cel_to_far(c_temp)} degrees F")