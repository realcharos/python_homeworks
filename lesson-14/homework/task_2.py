import numpy as np
# Task 2
def power_function(x, p):
    return x ** p

# Use vectorize
power_func = np.vectorize(power_function)

# Input arrays
numbers = np.array([2, 3, 4, 5])
powers = np.array([1, 2, 3, 4])

# Compute power
result = power_func(numbers, powers)

print("Power results:", result)
