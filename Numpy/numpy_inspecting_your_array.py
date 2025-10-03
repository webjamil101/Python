# ====================================================================
# NumPy Array Inspection: A Comprehensive Guide
# ====================================================================

import numpy as np

# Create a sample 1D array
arr_1d = np.arange(10, dtype=np.int32)

# Create a sample 2D array
arr_2d = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]], dtype=np.float64)

# --------------------------------------------------------------------
# 1. Basic Array Properties
# --------------------------------------------------------------------

print("--- Inspecting the 1D Array ---")
print("Original 1D Array:")
print(arr_1d)

# .shape: Returns a tuple with the dimensions of the array.
print(f"Shape: {arr_1d.shape}")

# .ndim: Returns the number of dimensions (axes) of the array.
print(f"Number of dimensions: {arr_1d.ndim}")

# .size: Returns the total number of elements in the array.
print(f"Total number of elements: {arr_1d.size}")

# .dtype: Returns the data type of the elements in the array.
print(f"Data type of elements: {arr_1d.dtype}")
print("-" * 30)


print("--- Inspecting the 2D Array ---")
print("Original 2D Array:")
print(arr_2d)

# .shape: For a 2D array, it returns (rows, columns).
print(f"Shape: {arr_2d.shape}")

# .ndim: For a 2D array, the number of dimensions is 2.
print(f"Number of dimensions: {arr_2d.ndim}")

# .size: The total number of elements (3 rows * 3 columns).
print(f"Total number of elements: {arr_2d.size}")

# .dtype: The data type we explicitly specified.
print(f"Data type of elements: {arr_2d.dtype}")
print("-" * 30)

# --------------------------------------------------------------------
# 2. Memory and Item Information
# --------------------------------------------------------------------

# .itemsize: The size in bytes of each element in the array.
print(f"Item size of 1D array (np.int32): {arr_1d.itemsize} bytes/element")
print(f"Item size of 2D array (np.float64): {arr_2d.itemsize} bytes/element")

# .nbytes: The total number of bytes consumed by the array's elements.
# This is equivalent to `arr.size * arr.itemsize`.
print(f"Total memory of 1D array: {arr_1d.nbytes} bytes")
print(f"Total memory of 2D array: {arr_2d.nbytes} bytes")
print("-" * 30)

# --------------------------------------------------------------------
# 3. Array Information Summary
# --------------------------------------------------------------------
# You can get a concise summary of the array's properties using a loop.
print("--- Array Information Summary ---")
for arr, name in [(arr_1d, "arr_1d"), (arr_2d, "arr_2d")]:
    print(f"\nProperties for '{name}':")
    print(f"  Shape: {arr.shape}")
    print(f"  Dimensions: {arr.ndim}")
    print(f"  Data type: {arr.dtype}")
    print(f"  Item size: {arr.itemsize} bytes")
    print(f"  Total elements: {arr.size}")
    print(f"  Total memory: {arr.nbytes} bytes")
