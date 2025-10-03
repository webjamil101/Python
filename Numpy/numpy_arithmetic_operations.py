# ====================================================================
# NumPy Arithmetic Operations
# ====================================================================

import numpy as np

# Create sample arrays for demonstration
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([1, 2, 3, 4, 5])

# Create a 2D array and a scalar
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
scalar = 10

# Create another 2D array for matrix multiplication
matrix2 = np.array([[1, 2],
                    [3, 4],
                    [5, 6]])

print("Initial 1D Arrays:")
print("arr1:", arr1)
print("arr2:", arr2)
print("-" * 30)
print("Initial 2D Matrix:")
print(matrix)
print("-" * 30)

# --------------------------------------------------------------------
# 1. Element-wise Arithmetic Operations
# --------------------------------------------------------------------

# These operations are performed on corresponding elements of the arrays.
# The arrays must have the same shape.

# Addition
addition_result = arr1 + arr2
print("Element-wise Addition (arr1 + arr2):")
print(addition_result)

# Subtraction
subtraction_result = arr1 - arr2
print("Element-wise Subtraction (arr1 - arr2):")
print(subtraction_result)

# Multiplication
multiplication_result = arr1 * arr2
print("Element-wise Multiplication (arr1 * arr2):")
print(multiplication_result)

# Division
division_result = arr1 / arr2
print("Element-wise Division (arr1 / arr2):")
print(division_result)

# Exponentiation
exponentiation_result = arr1 ** 2
print("Element-wise Exponentiation (arr1 ** 2):")
print(exponentiation_result)
print("-" * 30)

# --------------------------------------------------------------------
# 2. Broadcasting
# --------------------------------------------------------------------

# Broadcasting allows NumPy to perform operations on arrays of different shapes,
# as long as they are compatible. The smaller array is "stretched" to match
# the shape of the larger array.

# Add a scalar to a 2D array
scalar_addition = matrix + scalar
print("Broadcasting: Adding a scalar to a matrix:")
print(scalar_addition)

# Add a 1D array to a 2D matrix (broadcasting along rows)
row_vector = np.array([1, 0, -1])
matrix_row_addition = matrix + row_vector
print("Broadcasting: Adding a 1D array to each row of a matrix:")
print(matrix_row_addition)
print("-" * 30)

# --------------------------------------------------------------------
# 3. Matrix Multiplication
# --------------------------------------------------------------------

# Matrix multiplication is a more complex operation with specific rules.
# The number of columns in the first matrix must equal the number of rows
# in the second matrix.

# The '@' operator is the modern and preferred way for matrix multiplication.
dot_product_result = matrix @ matrix2
print("Matrix Multiplication (matrix @ matrix2):")
print(dot_product_result)

# The np.dot() function also performs matrix multiplication.
dot_product_result_func = np.dot(matrix, matrix2)
print("Matrix Multiplication (np.dot(matrix, matrix2)):")
print(dot_product_result_func)
print("-" * 30)

# --------------------------------------------------------------------
# 4. Other Common Mathematical Functions
# --------------------------------------------------------------------

# NumPy provides a wide range of universal functions (ufuncs) for element-wise
# operations.

# Square root of each element
sqrt_result = np.sqrt(matrix)
print("Square Root of each element in matrix:")
print(sqrt_result)

# Sum of all elements in an array
sum_result = np.sum(arr1)
print("Sum of all elements in arr1:", sum_result)

# Sum along a specific axis (axis=0 for columns, axis=1 for rows)
sum_axis0 = np.sum(matrix, axis=0)
print("Sum of each column in matrix (axis=0):", sum_axis0)

sum_axis1 = np.sum(matrix, axis=1)
print("Sum of each row in matrix (axis=1):", sum_axis1)

# Exponential function
exp_result = np.exp(arr2)
print("Exponential of each element in arr2:")
print(exp_result)

# ====================================================================
# NumPy Arithmetic Operations
# ====================================================================

import numpy as np

# Create sample arrays for demonstration
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([1, 2, 3, 4, 5])

# Create a 2D array and a scalar
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
scalar = 10

# Create another 2D array for matrix multiplication
matrix2 = np.array([[1, 2],
                    [3, 4],
                    [5, 6]])

print("Initial 1D Arrays:")
print("arr1:", arr1)
print("arr2:", arr2)
print("-" * 30)
print("Initial 2D Matrix:")
print(matrix)
print("-" * 30)

# --------------------------------------------------------------------
# 1. Element-wise Arithmetic Operations (Using Operators)
# --------------------------------------------------------------------

# These operations are performed on corresponding elements of the arrays.
# The arrays must have the same shape.

# Addition
addition_result = arr1 + arr2
print("Element-wise Addition (arr1 + arr2):")
print(addition_result)

# Subtraction
subtraction_result = arr1 - arr2
print("Element-wise Subtraction (arr1 - arr2):")
print(subtraction_result)

# Multiplication
multiplication_result = arr1 * arr2
print("Element-wise Multiplication (arr1 * arr2):")
print(multiplication_result)

# Division
division_result = arr1 / arr2
print("Element-wise Division (arr1 / arr2):")
print(division_result)

# Exponentiation
exponentiation_result = arr1 ** 2
print("Element-wise Exponentiation (arr1 ** 2):")
print(exponentiation_result)
print("-" * 30)

# --------------------------------------------------------------------
# 2. Element-wise Arithmetic Operations (Using NumPy Functions)
# --------------------------------------------------------------------

# NumPy provides universal functions (ufuncs) that perform the same
# element-wise operations as the operators.

# Addition using np.add()
add_func_result = np.add(arr1, arr2)
print("Element-wise Addition (np.add(arr1, arr2)):")
print(add_func_result)

# Subtraction using np.subtract()
subtract_func_result = np.subtract(arr1, arr2)
print("Element-wise Subtraction (np.subtract(arr1, arr2)):")
print(subtract_func_result)

# Multiplication using np.multiply()
multiply_func_result = np.multiply(arr1, arr2)
print("Element-wise Multiplication (np.multiply(arr1, arr2)):")
print(multiply_func_result)

# Division using np.divide()
divide_func_result = np.divide(arr1, arr2)
print("Element-wise Division (np.divide(arr1, arr2)):")
print(divide_func_result)

# Exponentiation using np.power()
power_func_result = np.power(arr1, 2)
print("Element-wise Exponentiation (np.power(arr1, 2)):")
print(power_func_result)
print("-" * 30)

# --------------------------------------------------------------------
# 3. Broadcasting
# --------------------------------------------------------------------

# Broadcasting allows NumPy to perform operations on arrays of different shapes,
# as long as they are compatible. The smaller array is "stretched" to match
# the shape of the larger array.

# Add a scalar to a 2D array
scalar_addition = matrix + scalar
print("Broadcasting: Adding a scalar to a matrix:")
print(scalar_addition)

# Add a 1D array to a 2D matrix (broadcasting along rows)
row_vector = np.array([1, 0, -1])
matrix_row_addition = matrix + row_vector
print("Broadcasting: Adding a 1D array to each row of a matrix:")
print(matrix_row_addition)
print("-" * 30)

# --------------------------------------------------------------------
# 4. Matrix Multiplication
# --------------------------------------------------------------------

# Matrix multiplication is a more complex operation with specific rules.
# The number of columns in the first matrix must equal the number of rows
# in the second matrix.

# The '@' operator is the modern and preferred way for matrix multiplication.
dot_product_result = matrix @ matrix2
print("Matrix Multiplication (matrix @ matrix2):")
print(dot_product_result)

# The np.dot() function also performs matrix multiplication.
dot_product_result_func = np.dot(matrix, matrix2)
print("Matrix Multiplication (np.dot(matrix, matrix2)):")
print(dot_product_result_func)
print("-" * 30)

# --------------------------------------------------------------------
# 5. Other Common Mathematical Functions
# --------------------------------------------------------------------

# NumPy provides a wide range of universal functions (ufuncs) for element-wise
# operations.

# Square root of each element
sqrt_result = np.sqrt(matrix)
print("Square Root of each element in matrix:")
print(sqrt_result)

# Sum of all elements in an array
sum_result = np.sum(arr1)
print("Sum of all elements in arr1:", sum_result)

# Sum along a specific axis (axis=0 for columns, axis=1 for rows)
sum_axis0 = np.sum(matrix, axis=0)
print("Sum of each column in matrix (axis=0):", sum_axis0)

sum_axis1 = np.sum(matrix, axis=1)
print("Sum of each row in matrix (axis=1):", sum_axis1)

# Exponential function
exp_result = np.exp(arr2)
print("Exponential of each element in arr2:")
print(exp_result)
