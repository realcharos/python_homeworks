import numpy as np

# Task 1
def fahrenheit_to_celsius(F):
    return (F - 32) * 5 / 9

f_to_c = np.vectorize(fahrenheit_to_celsius)
temperatures_f = np.array([32, 68, 100, 212, 77])
temperatures_c = f_to_c(temperatures_f)

print("Celsius temperatures:", temperatures_c)
