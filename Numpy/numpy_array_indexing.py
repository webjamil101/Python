import numpy as np

# --- 1. Creating a NumPy Array ---

# A 1D array
arr1d = np.arange(10)  # [0 1 2 3 4 5 6 7 8 9]

# A 2D array (matrix)
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# A 3D array
arr3d = np.arange(27).reshape(3, 3, 3)

# --- 2. Array Indexing ---

# 1D array indexing
print("1D array element at index 5:", arr1d[5])

# 2D array indexing: [row, column]
print("2D array element at [1, 2]:", arr2d[1, 2])

# Negative indexing: from the end of the array
print("Last element of 1D array:", arr1d[-1])
print("Last row, last column of 2D array:", arr2d[-1, -1])

# --- 3. Array Slicing ---

# 1D array slicing: [start:stop:step]
print("First five elements:", arr1d[:5])
print("Elements from index 5 to the end:", arr1d[5:])
print("Elements from index 2 to 7:", arr1d[2:8])
print("Every other element:", arr1d[::2])
print("Reversed array:", arr1d[::-1])

# 2D array slicing
print("First two rows:\n", arr2d[:2])
print("First two columns:\n", arr2d[:, :2])
print("A sub-array (slice of a slice):\n", arr2d[:2, 1:])

# --- 4. Boolean Masking ---

# Select elements that satisfy a condition
bool_mask = arr1d > 5
print("Boolean mask:", bool_mask)
print("Elements greater than 5:", arr1d[bool_mask])

# A more direct way
print("Even numbers:", arr1d[arr1d % 2 == 0])

# Boolean masking in 2D
print("Elements in 2D array > 5:", arr2d[arr2d > 5])

# --- 5. Fancy Indexing ---

# Pass a list or array of indices to select multiple elements
indices = [0, 4, 8]
print("Elements at specific indices:", arr1d[indices])

# Fancy indexing in 2D: select rows 0 and 2
print("Rows 0 and 2:\n", arr2d[[0, 2]])

# --- 6. Other Operations ---

# Reshaping: change the dimensions of the array
reshaped_arr = arr1d.reshape(2, 5)
print("Reshaped 1D array to 2x5:\n", reshaped_arr)

# Transposing: swap rows and columns
transposed_arr = arr2d.T
print("Transposed 2D array:\n", transposed_arr)

# Universal functions (ufuncs): mathematical operations applied element-wise
print("Square of arr1d:", np.square(arr1d))
print("arr2d + 10:\n", arr2d + 10)