# ====================================================================
# NumPy Subsetting: A Comprehensive Guide
# ====================================================================

import numpy as np

# Create a sample 1D array
arr_1d = np.arange(10)
print("Original 1D Array:")
print(arr_1d)
print("-" * 30)

# --------------------------------------------------------------------
# 1. Basic Indexing and Slicing (1D Arrays)
# --------------------------------------------------------------------

# Access a single element
print("Element at index 5:", arr_1d[5])

# Slice from the beginning up to (but not including) index 4
print("Slice from start to index 4:", arr_1d[:4])

# Slice from index 4 to the end
print("Slice from index 4 to end:", arr_1d[4:])

# Slice from index 2 to 7 (exclusive), with a step of 2
print("Slice from index 2 to 7 with step 2:", arr_1d[2:7:2])

# Reverse the array using slicing
print("Reversed array:", arr_1d[::-1])
print("-" * 30)

# --------------------------------------------------------------------
# 2. Integer Array Indexing (1D Arrays)
# --------------------------------------------------------------------

# Create an array of indices
indices = np.array([0, 8, 3])
print("Original 1D Array:", arr_1d)
print("Indices to retrieve:", indices)
print("Elements at specified indices:", arr_1d[indices])

# Accessing the same element multiple times
indices_repeated = np.array([1, 1, 3, 3, 3])
print("Elements at repeated indices:", arr_1d[indices_repeated])
print("-" * 30)

# --------------------------------------------------------------------
# 3. Boolean Array Indexing (Masking) (1D Arrays)
# --------------------------------------------------------------------

# Create a boolean mask based on a condition
mask = arr_1d > 5
print("Original 1D Array:", arr_1d)
print("Boolean Mask (arr_1d > 5):", mask)
print("Elements where the mask is True:", arr_1d[mask])

# A more direct way to apply the condition
print("Elements greater than 5:", arr_1d[arr_1d > 5])

# Combining conditions using logical operators
# Note: Use & for 'and', | for 'or'
print("Elements > 3 AND < 8:", arr_1d[(arr_1d > 3) & (arr_1d < 8)])
print("-" * 30)

# --------------------------------------------------------------------
# 4. Subsetting Multi-Dimensional Arrays (2D Arrays)
# --------------------------------------------------------------------

# Create a sample 2D array
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("Original 2D Array:")
print(arr_2d)
print("-" * 30)

# Basic Indexing: [row, column]
print("Element at row 1, column 2:", arr_2d[1, 2])

# Slicing a row
print("Second row:", arr_2d[1, :])

# Slicing a column
print("Third column:", arr_2d[:, 2])

# Slicing a sub-array (rows 0-1, columns 1-2)
print("Sub-array of rows 0-1 and columns 1-2:")
print(arr_2d[0:2, 1:3])
print("-" * 30)

# Integer Array Indexing (2D Arrays)
# Access elements at specified (row, col) pairs
row_indices = np.array([0, 1, 2])
col_indices = np.array([0, 1, 0])
print("Original 2D Array:")
print(arr_2d)
print("Elements at (0,0), (1,1), (2,0):", arr_2d[row_indices, col_indices])
print("-" * 30)

# Boolean Array Indexing (2D Arrays)
print("Elements greater than 5:")
print(arr_2d[arr_2d > 5])
