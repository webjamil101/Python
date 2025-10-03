# ====================================================================
# NumPy Array Manipulation
# This document covers key functions for changing the shape, size,
# and structure of NumPy arrays.
# ====================================================================

import numpy as np

# Create a sample array for all demonstrations
arr = np.arange(12)
print("Original 1D Array:")
print(arr)
print("-" * 40)

# --------------------------------------------------------------------
# 1. Reshaping Arrays
# --------------------------------------------------------------------
# Reshaping changes the dimensions of an array without changing its data.
# The number of elements must remain the same.

# .reshape(): Returns a new array with the specified shape.
reshaped_arr = arr.reshape(3, 4)
print("Reshaped 2D Array (3x4):")
print(reshaped_arr)

# Using -1 to automatically infer a dimension's size
reshaped_arr_auto = arr.reshape(2, -1)
print("\nReshaped Array with one dimension inferred (2x6):")
print(reshaped_arr_auto)

# .ravel(): Returns a flattened view of the array (changes to the view
#           will affect the original array).
print("\nFlattened array using .ravel():")
print(reshaped_arr.ravel())

# .flatten(): Returns a flattened copy of the array (changes to the copy
#             will NOT affect the original).
flattened_copy = reshaped_arr.flatten()
flattened_copy[0] = 999
print("\nFlattened array using .flatten() (original array is unchanged):")
print(reshaped_arr)
print("-" * 40)


# --------------------------------------------------------------------
# 2. Transposing Arrays
# --------------------------------------------------------------------
# Transposing swaps the rows and columns of a 2D array.

# .T attribute: The most common way to transpose.
transposed_arr = reshaped_arr.T
print("Original 2D Array:")
print(reshaped_arr)
print("\nTransposed Array:")
print(transposed_arr)
print("-" * 40)


# --------------------------------------------------------------------
# 3. Joining Arrays
# --------------------------------------------------------------------
# These functions combine multiple arrays into a single new array.

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print("Arrays to join:")
print("arr1:\n", arr1)
print("arr2:\n", arr2)

# np.concatenate(): Joins arrays along an existing axis.
# By default, axis=0 (joins rows).
concatenated_arr = np.concatenate((arr1, arr2))
print("\nConcatenated along axis=0:")
print(concatenated_arr)

# Join along axis=1 (joins columns).
concatenated_arr_axis1 = np.concatenate((arr1, arr2), axis=1)
print("\nConcatenated along axis=1:")
print(concatenated_arr_axis1)

# np.vstack(): Stacks arrays vertically (row-wise). Equivalent to concatenate with axis=0.
vstacked_arr = np.vstack((arr1, arr2))
print("\nVertically stacked (vstack):")
print(vstacked_arr)

# np.hstack(): Stacks arrays horizontally (column-wise). Equivalent to concatenate with axis=1.
hstacked_arr = np.hstack((arr1, arr2))
print("\nHorizontally stacked (hstack):")
print(hstacked_arr)
print("-" * 40)


# --------------------------------------------------------------------
# 4. Splitting Arrays
# --------------------------------------------------------------------
# Splits a single array into multiple smaller arrays.

# np.split(): Splits an array into multiple sub-arrays.
# You must specify the number of splits or the indices at which to split.
arr_to_split = np.arange(16).reshape(4, 4)
print("Array to split:")
print(arr_to_split)

# Split into 2 equal-sized arrays along axis=0 (rows)
split_rows = np.split(arr_to_split, 2, axis=0)
print("\nSplit into 2 arrays along rows:")
print(split_rows)

# np.hsplit(): Splits an array horizontally (column-wise).
hsplit_arr = np.hsplit(arr_to_split, 2)
print("\nHorizontally split into 2 arrays:")
print(hsplit_arr)
print("-" * 40)


# --------------------------------------------------------------------
# 5. Adding and Removing Elements
# --------------------------------------------------------------------
# Note: These operations return new arrays and can be computationally expensive.

arr_mod = np.array([1, 2, 3, 4, 5])
print("Original Array for modification:", arr_mod)

# np.append(): Appends values to the end of an array.
appended_arr = np.append(arr_mod, [6, 7])
print("\nArray after appending [6, 7]:", appended_arr)

# np.insert(): Inserts values into an array at a specific index.
# Syntax: np.insert(array, index, values)
inserted_arr = np.insert(arr_mod, 2, 99)
print("Array after inserting 99 at index 2:", inserted_arr)

# np.delete(): Deletes values from an array at a specific index or slice.
deleted_arr = np.delete(arr_mod, [1, 3])
print("Array after deleting elements at indices 1 and 3:", deleted_arr)
print("-" * 40) 