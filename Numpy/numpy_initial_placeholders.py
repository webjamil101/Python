# ====================================================================
# NumPy Initial Placeholder Functions
# This document demonstrates how to create new arrays filled with
# placeholder values like zeros, ones, or a specific constant.
# ====================================================================

import numpy as np

# --------------------------------------------------------------------
# 1. np.zeros() - Create an array filled with zeros
# --------------------------------------------------------------------
# The primary use case for `np.zeros()` is to pre-allocate an array
# of a known size, which can be more efficient than dynamically
# resizing an array later. The default data type is float64.

# Create a 1D array of 5 zeros
zeros_1d = np.zeros(5)
print("1D array of zeros:")
print(zeros_1d)

# Create a 2D array (matrix) of zeros with shape (3, 4)
zeros_2d = np.zeros((3, 4))
print("\n2D array of zeros:")
print(zeros_2d)

# Create an array of zeros with a specific data type
zeros_int = np.zeros((2, 3), dtype=np.int32)
print("\n2D integer array of zeros:")
print(zeros_int)
print("-" * 40)


# --------------------------------------------------------------------
# 2. np.ones() - Create an array filled with ones
# --------------------------------------------------------------------
# Similar to `np.zeros()`, this is useful for pre-allocating an array.
# It can also be a starting point for operations, e.g., creating a
# matrix of ones to scale.

# Create a 1D array of 3 ones
ones_1d = np.ones(3)
print("1D array of ones:")
print(ones_1d)

# Create a 2D array of ones with shape (2, 5) and a specified dtype
ones_2d = np.ones((2, 5), dtype=np.uint8)
print("\n2D array of ones with dtype uint8:")
print(ones_2d)
print("-" * 40)


# --------------------------------------------------------------------
# 3. np.empty() - Create an uninitialized array
# --------------------------------------------------------------------
# `np.empty()` creates an array without initializing its values. This
# means its contents are whatever was in that memory location previously.
# This function is significantly faster than `np.zeros()` or `np.ones()`
# because it skips the step of filling the array with a constant value.
# Use it only when you know you will immediately overwrite all the values.

# Create an uninitialized 2D array of shape (2, 2)
empty_arr = np.empty((2, 2))
print("2D uninitialized array:")
print(empty_arr)
# The values here will be random and should not be relied upon.
print("-" * 40)


# --------------------------------------------------------------------
# 4. np.full() - Create an array filled with a specific value
# --------------------------------------------------------------------
# `np.full()` provides a more general way to create an array with a
# custom fill value.

# Create a 3x3 array filled with the value 7
full_arr = np.full((3, 3), 7)
print("3x3 array filled with the value 7:")
print(full_arr)

# Create an array of shape (2, 4) filled with a specific string
full_string_arr = np.full((2, 4), 'hello', dtype='U5')
print("\n2x4 array filled with the string 'hello':")
print(full_string_arr)
print("-" * 40)

