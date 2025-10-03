# ====================================================================
# NumPy Array Slicing
# This document covers the fundamental ways to slice and access
# elements from NumPy arrays using a variety of techniques.
# ====================================================================

import numpy as np

# --------------------------------------------------------------------
# 1. Basic Slicing (1D Arrays)
# --------------------------------------------------------------------
# Slicing in NumPy works similarly to Python lists, using the syntax
# [start:stop:step].

arr_1d = np.arange(10, 20)
print("Original 1D Array:")
print(arr_1d)

# Slice from index 3 up to (but not including) index 7
print("\nSlice from index 3 to 7:", arr_1d[3:7])

# Slice from the beginning up to index 5
print("Slice from start to index 5:", arr_1d[:5])

# Slice from index 5 to the end
print("Slice from index 5 to end:", arr_1d[5:])

# Slice from start to end with a step of 2
print("Slice with a step of 2:", arr_1d[::2])

# Reverse the array using a negative step
print("Reversed array:", arr_1d[::-1])
print("-" * 40)


# --------------------------------------------------------------------
# 2. Slicing Multi-Dimensional Arrays (2D Arrays)
# --------------------------------------------------------------------
# For multi-dimensional arrays, you can provide a slice for each dimension.
# The syntax is arr[row_slice, column_slice].

arr_2d = np.array([[10, 11, 12, 13],
                   [20, 21, 22, 23],
                   [30, 31, 32, 33],
                   [40, 41, 42, 43]])
print("Original 2D Array:")
print(arr_2d)

# Select a single element (row 1, column 2)
print("\nElement at (1, 2):", arr_2d[1, 2])

# Select the entire second row
print("Second row:", arr_2d[1, :])

# Select the entire third column
print("Third column:", arr_2d[:, 2])

# Select a sub-array (a slice of rows and columns)
# Rows from index 1 to 3, columns from index 1 to 3
sub_array = arr_2d[1:3, 1:3]
print("Sub-array (rows 1-2, columns 1-2):")
print(sub_array)

# Using a single index for a dimension returns a lower-dimensional array
# This returns the second row as a 1D array.
print("\nSecond row as a 1D array:", arr_2d[1])
print("-" * 40)


# --------------------------------------------------------------------
# 3. Advanced Slicing Techniques
# --------------------------------------------------------------------
# NumPy also supports more advanced ways of selecting elements.

# Boolean Masking: Use a boolean array to select elements that meet a condition.
# The mask must have the same shape as the array being sliced.
mask = arr_2d > 25
print("Boolean Mask (arr_2d > 25):")
print(mask)
print("Elements greater than 25:")
print(arr_2d[mask])

# Integer Array Indexing: Use a list or array of integers as indices.
# This is useful for selecting non-contiguous or repeated elements.
rows = np.array([0, 2, 3])
cols = np.array([1, 0, 3])
print("\nElements at (0,1), (2,0), and (3,3):")
print(arr_2d[rows, cols])
print("-" * 40)


# --------------------------------------------------------------------
# 4. Slicing with Ellipsis (...)
# --------------------------------------------------------------------
# The ellipsis (...) is a shortcut for selecting all of the other dimensions.
# It is most useful for high-dimensional arrays.

arr_3d = np.arange(27).reshape(3, 3, 3)
print("Original 3D Array:")
print(arr_3d)

# Select all elements in the first "slice" along the first dimension
print("\nFirst slice along the first dimension (same as arr_3d[0, :, :]):")
print(arr_3d[0, ...])

# Select all elements in the second "slice" along the last dimension
print("\nSecond slice along the last dimension (same as arr_3d[:, :, 1]):")
print(arr_3d[..., 1])
