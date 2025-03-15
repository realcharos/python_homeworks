import numpy as np

# 1
vector = np.arange(10, 50)
print(vector)

# 2
matrix_3x3 = np.arange(9).reshape(3, 3)
print(matrix_3x3)

# 3
identity_matrix = np.eye(3)
print(identity_matrix)

# 4
random_array = np.random.random((3, 3, 3))
print(random_array)

# 5
array_10x10 = np.random.random((10, 10))
min_value = np.min(array_10x10)
max_value = np.max(array_10x10)
print(min_value, max_value)

# 6
random_vector = np.random.random(30)
mean_value = np.mean(random_vector)
print(mean_value)

# 7
matrix_5x5 = np.random.random((5, 5))
normalized_matrix = (matrix_5x5 - np.min(matrix_5x5)) / (np.max(matrix_5x5) - np.min(matrix_5x5))
print(normalized_matrix)

# 8
matrix_A = np.random.random((5, 3))
matrix_B = np.random.random((3, 2))
product_AB = np.dot(matrix_A, matrix_B)
print(product_AB)

# 9
matrix_X = np.random.random((3, 3))
matrix_Y = np.random.random((3, 3))
dot_product = np.dot(matrix_X, matrix_Y)
print(dot_product)

# 10
matrix_4x4 = np.random.random((4, 4))
transpose_matrix = matrix_4x4.T
print(transpose_matrix)

# 11
matrix_3x3_det = np.random.random((3, 3))
determinant = np.linalg.det(matrix_3x3_det)
print(determinant)

# 12
A = np.random.random((3, 4))
B = np.random.random((4, 3))
product_AB2 = np.dot(A, B)
print(product_AB2)

# 13
matrix_3x3 = np.random.random((3, 3))
vector_3x1 = np.random.random((3, 1))
matrix_vector_product = np.dot(matrix_3x3, vector_3x1)
print(matrix_vector_product)

# 14
A_system = np.random.random((3, 3))
b_system = np.random.random((3, 1))
x_solution = np.linalg.solve(A_system, b_system)
print(x_solution)

# 15
matrix_5x5_sum = np.random.random((5, 5))
row_sums = np.sum(matrix_5x5_sum, axis=1)
column_sums = np.sum(matrix_5x5_sum, axis=0)
print(row_sums)
print(column_sums)
