# ====================================================================
# NumPy Array Creation
# This document covers the fundamental ways to create new arrays
# from existing Python objects or using NumPy's built-in functions.
# ====================================================================

import numpy as np

# --------------------------------------------------------------------
# 1. Creating Arrays from Existing Data
# --------------------------------------------------------------------
# The most common way to create an array is from a Python list or tuple
# using the np.array() function.

# Create a 1D array from a list
list_1d = [1, 2, 3, 4, 5]
arr_from_list = np.array(list_1d)
print("1D Array from a list:")
print(arr_from_list)

# Create a 2D array (matrix) from a nested list
list_2d = [[10, 20, 30],
           [40, 50, 60]]
arr_from_nested_list = np.array(list_2d)
print("\n2D Array from a nested list:")
print(arr_from_nested_list)

# You can also specify the data type (dtype)
arr_with_dtype = np.array([1, 2, 3], dtype=np.float64)
print("\nArray with a specified data type (float64):")
print(arr_with_dtype)
print("-" * 40)


# --------------------------------------------------------------------
# 2. Creating Arrays with Placeholder Values
# --------------------------------------------------------------------
# These functions are useful for pre-allocating memory when the size
# of the array is known but the values are not yet computed.

# np.zeros(): Creates an array filled with zeros
zeros_arr = np.zeros((3, 4)) # Shape is a tuple (rows, columns)
print("Array of zeros (3x4):")
print(zeros_arr)

# np.ones(): Creates an array filled with ones
ones_arr = np.ones((2, 5))
print("\nArray of ones (2x5):")
print(ones_arr)

# np.full(): Creates an array filled with a specified value
full_arr = np.full((2, 2), 99)
print("\nArray filled with a specific value (99):")
print(full_arr)

# np.empty(): Creates an uninitialized array
empty_arr = np.empty((3, 3)) # Contains random, uninitialized values
print("\nEmpty array (uninitialized):")
print(empty_arr)
print("-" * 40)


# --------------------------------------------------------------------
# 3. Creating Arrays from Number Ranges
# --------------------------------------------------------------------
# These functions are ideal for creating sequences of numbers.

# np.arange(): Creates an array with a range of numbers
# Syntax: np.arange(start, stop, step)
range_arr = np.arange(10, 30, 5) # Start=10, Stop=30 (exclusive), Step=5
print("Array from a range (arange):")
print(range_arr)

# np.linspace(): Creates an array with evenly spaced numbers
# Syntax: np.linspace(start, stop, num)
linspace_arr = np.linspace(0, 1, 5) # 5 elements from 0 to 1
print("\nArray with evenly spaced numbers (linspace):")
print(linspace_arr)
print("-" * 40)


# --------------------------------------------------------------------
# 4. Creating Special Arrays
# --------------------------------------------------------------------

# np.identity(): Creates a square identity matrix
identity_matrix = np.identity(3)
print("3x3 Identity Matrix:")
print(identity_matrix)

# np.eye(): Creates a 2D array with ones on the diagonal and zeros elsewhere
eye_matrix = np.eye(4, k=1) # 4x4 matrix with diagonal offset by 1
print("\n4x4 Matrix with a shifted diagonal (eye):")
print(eye_matrix)

# np.diag(): Extracts a diagonal or creates a diagonal matrix
diag_arr = np.array([1, 2, 3])
diag_matrix = np.diag(diag_arr)
print("\nDiagonal matrix from a 1D array:")
print(diag_matrix)
print("-" * 40)

# asking for help in numpy 
np.info(np.array)  # Get detailed information about np.array function
np.info(np.zeros)  # Get detailed information about np.zeros function
np.info(np.ones)   # Get detailed information about np.ones function
np.info(np.empty)  # Get detailed information about np.empty function
np.info(np.full)  # Get detailed information about np.full function
np.info(np.arange)  # Get detailed information about np.arange function
np.info(np.linspace)  # Get detailed information about np.linspace function
np.info(np.identity)  # Get detailed information about np.identity function
np.info(np.eye)  # Get detailed information about np.eye function
np.info(np.diag)  # Get detailed information about np.diag function
np.info(np.sort)  # Get detailed information about np.sort function
np.info(np.argsort)  # Get detailed information about np.argsort function
np.info(np.unique)  # Get detailed information about np.unique function
np.info(np.concatenate)  # Get detailed information about np.concatenate function
np.info(np.vstack)  # Get detailed information about np.vstack function
np.info(np.hstack)  # Get detailed information about np.hstack function
np.info(np.split)  # Get detailed information about np.split function
np.info(np.reshape)  # Get detailed information about np.reshape function
np.info(np.transpose)  # Get detailed information about np.transpose function
np.info(np.ravel)  # Get detailed information about np.ravel function
np.info(np.flatten)  # Get detailed information about np.flatten function
np.info(np.concatenate)  # Get detailed information about np.concatenate function
# ====================================================================
# NumPy np.info() Command
# This document demonstrates the use of the np.info() function, which
# provides detailed information about NumPy functions, arrays, and
# objects directly from the console. It's a quick way to access a
# summary of the docstring and other relevant details.
# ====================================================================

import numpy as np

# --------------------------------------------------------------------
# 1. Using np.info() on a NumPy Function
# --------------------------------------------------------------------
# This is the most common use case. It acts as a help utility,
# printing the function's signature, docstring, and file location.

print("--- np.info() on np.sum ---")
np.info(np.sum)
print("-" * 60)

# The output from np.info(np.sum) includes:
# - A brief summary of the function's purpose.
# - The function's signature: 'def sum(a, axis=None, dtype=None, ...):'
# - A detailed explanation of the parameters (a, axis, dtype, etc.).
# - Examples of how to use the function.
# - The file path where the function is defined.

# --------------------------------------------------------------------
# 2. Using np.info() on a NumPy Array or Object
# --------------------------------------------------------------------
# When used on an array, it provides a summary of the object's type,
# shape, and data type.

# Create a sample array
arr = np.array([[10, 20], [30, 40]], dtype=np.int32)

print("--- np.info() on a 2D array ---")
np.info(arr)
print("-" * 60)

# The output for an array includes:
# - Its class name: "class: numpy.ndarray"
# - Its shape: "shape: (2, 2)"
# - Its data type: "dtype: int32"
# - The total number of elements.
# - The size of each element in bytes.

# --------------------------------------------------------------------
# 3. Using np.info() with a string
# --------------------------------------------------------------------
# You can also pass a string to get information about a module or function
# within that module. This is useful for getting help without having
# the object in your current namespace.

print("--- np.info() on 'numpy.arange' ---")
np.info('numpy.arange')
print("-" * 60)

# --------------------------------------------------------------------
# 4. A Helper function to make it easier to read.
# --------------------------------------------------------------------
# You can wrap np.info in your own function for better formatting
def show_info(obj):
    print(f"\nInformation for {str(obj)}:")
    print("-" * 20)
    np.info(obj)
    print("\n" + "=" * 40 + "\n")

# Using the helper function
show_info(np.sqrt)
show_info(np.ones((2,2)))
show_info('np.dot')
np.info(np.ndarray.dtype)