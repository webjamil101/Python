# ====================================================================
# NumPy Array Copying
# This document demonstrates the difference between views and copies
# in NumPy, and the proper way to create a true copy of an array.
# ====================================================================

import numpy as np

# Create a sample array
original_arr = np.array([1, 2, 3, 4, 5])
print("Original Array:")
print(original_arr)
print("-" * 40)


# --------------------------------------------------------------------
# 1. Views vs. Copies
# --------------------------------------------------------------------
# A "view" is a new array object that looks at the same data as the
# original array. Changes made to the view will affect the original.
# A "copy" is a new array object with its own, independent copy of
# the data. Changes to the copy will not affect the original.

# Example of a View (Slicing)
# When you slice an array, NumPy often creates a view, not a copy.
view_arr = original_arr[1:4]
print("Created a view by slicing the original array:")
print(view_arr)

# Modify an element in the view
view_arr[0] = 99
print("\nAfter modifying the view:")
print(f"  View array: {view_arr}")
print(f"  Original array: {original_arr}")
print("\nNotice the original array was also changed!")
print("-" * 40)


# --------------------------------------------------------------------
# 2. Creating a True Copy with .copy()
# --------------------------------------------------------------------
# To ensure you have an independent copy of the data, use the .copy()
# method. This is the explicit way to create a deep copy.

# Reset the original array for the next example
original_arr = np.array([1, 2, 3, 4, 5])

# Create a true copy using the .copy() method
copy_arr = original_arr.copy()
print("Created a true copy using .copy():")
print(copy_arr)

# Modify an element in the copy
copy_arr[0] = 101
print("\nAfter modifying the copy:")
print(f"  Copy array: {copy_arr}")
print(f"  Original array: {original_arr}")
print("\nNotice the original array remains unchanged this time.")
print("-" * 40)


# --------------------------------------------------------------------
# 3. Checking if an Array is a View or a Copy
# --------------------------------------------------------------------
# The .base attribute of an array will be None if the array is a copy.
# If it's a view, the .base attribute will be the original array.

# Checking the view
if view_arr.base is original_arr:
    print("view_arr.base is the original array, so it's a VIEW.")
else:
    print("view_arr.base is NOT the original array.")

# Checking the copy
if copy_arr.base is None:
    print("copy_arr.base is None, so it's a COPY.")
else:
    print("copy_arr.base is NOT None.")
