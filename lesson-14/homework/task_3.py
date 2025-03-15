import numpy as np
# Task 3
A = np.array([[4, 5, 6], [3, -1, 1], [2, 1, -2]])
b = np.array([7, 4, 5])

# Solve Ax = b
solution = np.linalg.solve(A, b)

print("Solution (x, y, z):", solution)
