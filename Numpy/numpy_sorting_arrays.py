# ====================================================================
# NumPy Array Sorting
# This document covers the primary methods for sorting NumPy arrays,
# including in-place sorting, creating a sorted copy, and sorting
# multi-dimensional arrays along a specific axis.
# ====================================================================

import numpy as np

# Create a sample 1D array
arr_1d = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print("Original 1D Array:")
print(arr_1d)
print("-" * 40)

# --------------------------------------------------------------------
# 1. np.sort() - Returns a Sorted Copy
# --------------------------------------------------------------------
# This function is non-destructive; it returns a new, sorted array and
# leaves the original array unchanged. This is often the safest method.

sorted_copy = np.sort(arr_1d)
print("Sorted copy using np.sort():")
print(sorted_copy)
print("Original array remains unchanged:")
print(arr_1d)
print("-" * 40)

# --------------------------------------------------------------------
# 2. ndarray.sort() - In-place Sorting
# --------------------------------------------------------------------
# This is a method of the ndarray object itself. It sorts the array
# in-place, meaning the original array is modified directly and nothing
# is returned.

arr_1d.sort()
print("Array sorted in-place using arr.sort():")
print(arr_1d)
print("-" * 40)


# --------------------------------------------------------------------
# 3. Sorting Multi-Dimensional Arrays
# --------------------------------------------------------------------
# For multi-dimensional arrays, the `axis` parameter specifies which
# axis to sort along.
# - axis=0: Sorts each column.
# - axis=1: Sorts each row.
# - axis=None (default): Flattens the array and returns a single sorted array.

# Create a sample 2D array
arr_2d = np.array([[3, 1, 2],
                   [6, 4, 5]])
print("Original 2D Array:")
print(arr_2d)

# Sort along axis 0 (columns)
sorted_by_columns = np.sort(arr_2d, axis=0)
print("\nSorted by column (axis=0):")
print(sorted_by_columns)

# Sort along axis 1 (rows)
sorted_by_rows = np.sort(arr_2d, axis=1)
print("\nSorted by row (axis=1):")
print(sorted_by_rows)

# Sort flattened array
sorted_flattened = np.sort(arr_2d, axis=None)
print("\nSorted flattened array:")
print(sorted_flattened)
print("-" * 40)


# --------------------------------------------------------------------
# 4. np.argsort() - Sorting by Indices
# --------------------------------------------------------------------
# This function is very powerful. It returns the indices that would
# sort an array. You can then use these indices to reorder other
# related arrays or the original array itself.

values = np.array([30, 10, 20, 50, 40])
print("Original values:", values)

# Get the sorting indices
sorted_indices = np.argsort(values)
print("Indices that would sort the array:", sorted_indices)

# Use the indices to sort the original array
sorted_values_via_indices = values[sorted_indices]
print("Sorted values using argsort indices:", sorted_values_via_indices)
print("-" * 40)


# --------------------------------------------------------------------
# 5. Sorting a 2D Array by a Specific Column
# --------------------------------------------------------------------
# This is a common task in data analysis. We can use argsort to sort
# a 2D array based on the values in one of its columns.

data = np.array([[10, 20],
                 [5,  100],
                 [50, 5]])
print("Original 2D data:")
print(data)

# Sort the entire array based on the values in the first column (index 0)
sort_by_first_column = data[np.argsort(data[:, 0])]
print("\nSorted by first column:")
print(sort_by_first_column)

# Sort the entire array based on the values in the second column (index 1)
sort_by_second_column = data[np.argsort(data[:, 1])]
print("\nSorted by second column:")
print(sort_by_second_column)
