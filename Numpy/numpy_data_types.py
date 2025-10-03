# ====================================================================
# NumPy Data Types (dtypes)
# ====================================================================

import numpy as np

# A NumPy array is a grid of values, all of the same type. This type is
# referred to as the data type or 'dtype'. Understanding dtypes is
# crucial for memory efficiency and correct operations.

print("--- 1. Creating Arrays with Specific Data Types ---")
# When you create an array, NumPy infers the dtype by default.
arr_int = np.array([1, 2, 3])
arr_float = np.array([1.0, 2.5, 3.7])
arr_bool = np.array([True, False, True])

print(f"Inferred integer array dtype: {arr_int.dtype}")
print(f"Inferred float array dtype: {arr_float.dtype}")
print(f"Inferred boolean array dtype: {arr_bool.dtype}")
print("-" * 30)

# You can explicitly specify the data type using the 'dtype' parameter.
# Common dtypes include:
# - int8, int16, int32, int64: Signed integers of various sizes.
# - uint8, uint16, uint32, uint64: Unsigned integers.
# - float16, float32, float64: Floating-point numbers.
# - complex64, complex128: Complex numbers.
# - bool: Boolean (True/False) values.
# - object: For storing Python objects (less efficient).

arr_explicit_int8 = np.array([1, 2, 3], dtype=np.int8)
print(f"Explicitly set int8 array: {arr_explicit_int8} (dtype: {arr_explicit_int8.dtype})")

arr_explicit_float32 = np.array([1.1, 2.2, 3.3], dtype=np.float32)
print(f"Explicitly set float32 array: {arr_explicit_float32} (dtype: {arr_explicit_float32.dtype})")

# Dtypes can also be specified as a single character or string:
# 'i' for integer, 'f' for float, 'b' for boolean, 'c' for complex, 'S' for string
arr_string = np.array(['a', 'b', 'c'], dtype='S')
print(f"Explicitly set string array: {arr_string} (dtype: {arr_string.dtype})")
print("-" * 30)


print("--- 2. Checking and Changing Data Types ---")
# The `.dtype` attribute is used to check the data type of an array.
print(f"Current dtype of arr_float: {arr_float.dtype}")

# The `.astype()` method creates a new array with the converted dtype.
# It does not modify the original array.
arr_float_to_int = arr_float.astype(np.int64)
print(f"Original float array: {arr_float}")
print(f"Converted to int array: {arr_float_to_int} (dtype: {arr_float_to_int.dtype})")

# Note: Converting a float to an integer truncates the decimal part.
print("-" * 30)


print("--- 3. Data Type Operations and Behavior ---")
# Dtypes affect how operations are performed and the resulting dtype.
# The dtype of the result is generally the "larger" or "more complex" of the
# two dtypes involved.
a = np.array([1, 2, 3], dtype=np.int8)
b = np.array([4.1, 5.2, 6.3], dtype=np.float32)

# Performing an operation between an int8 and a float32 results in a float32 array.
result = a + b
print(f"Array a (dtype: {a.dtype}): {a}")
print(f"Array b (dtype: {b.dtype}): {b}")
print(f"Result of a + b: {result} (dtype: {result.dtype})")

# Dtypes are important for memory usage.
# int8 takes up 1 byte per element, while int64 takes up 8 bytes.
arr_int8 = np.arange(1000, dtype=np.int8)
arr_int64 = np.arange(1000, dtype=np.int64)
print(f"Memory used by 1000 int8 elements: {arr_int8.nbytes} bytes")
print(f"Memory used by 1000 int64 elements: {arr_int64.nbytes} bytes")
print("-" * 30)

# --------------------------------------------------------------------
# 4. Summary of Key NumPy Dtypes
# --------------------------------------------------------------------
# - Integers: `np.int8`, `np.int16`, `np.int32`, `np.int64`
# - Unsigned Integers: `np.uint8`, `np.uint16`, `np.uint32`, `np.uint64`
# - Floats: `np.float16`, `np.float32`, `np.float64`
# - Booleans: `np.bool_`
# - Strings: `np.string_`
# - Complex Numbers: `np.complex64`, `np.complex128`
# - Datetime: `np.datetime64`
# - Timedelta: `np.timedelta64`
# ====================================================================
# NumPy Data Types (dtypes)
# ====================================================================

import numpy as np

# A NumPy array is a grid of values, all of the same type. This type is
# referred to as the data type or 'dtype'. Understanding dtypes is
# crucial for memory efficiency and correct operations.

print("--- 1. Creating Arrays with Specific Data Types ---")
# When you create an array, NumPy infers the dtype by default.
arr_int = np.array([1, 2, 3])
arr_float = np.array([1.0, 2.5, 3.7])
arr_bool = np.array([True, False, True])

print(f"Inferred integer array dtype: {arr_int.dtype}")
print(f"Inferred float array dtype: {arr_float.dtype}")
print(f"Inferred boolean array dtype: {arr_bool.dtype}")
print("-" * 30)

# You can explicitly specify the data type using the 'dtype' parameter.
# Common dtypes include:
# - int8, int16, int32, int64: Signed integers of various sizes.
# - uint8, uint16, uint32, uint64: Unsigned integers.
# - float16, float32, float64: Floating-point numbers.
# - complex64, complex128: Complex numbers.
# - bool: Boolean (True/False) values.
# - object: For storing Python objects (less efficient).

arr_explicit_int8 = np.array([1, 2, 3], dtype=np.int8)
print(f"Explicitly set int8 array: {arr_explicit_int8} (dtype: {arr_explicit_int8.dtype})")

arr_explicit_float32 = np.array([1.1, 2.2, 3.3], dtype=np.float32)
print(f"Explicitly set float32 array: {arr_explicit_float32} (dtype: {arr_explicit_float32.dtype})")

# Dtypes can also be specified as a single character or string:
# 'i' for integer, 'f' for float, 'b' for boolean, 'c' for complex, 'S' for string
arr_string = np.array(['a', 'b', 'c'], dtype='S')
print(f"Explicitly set string array: {arr_string} (dtype: {arr_string.dtype})")
print("-" * 30)


print("--- 2. Checking and Changing Data Types with .astype() ---")
# The `.dtype` attribute is used to check the data type of an array.
print(f"Current dtype of arr_float: {arr_float.dtype}")

# The `.astype()` method creates a new array with the converted dtype.
# It does not modify the original array.

# Example 1: Converting floats to integers
float_arr = np.array([1.5, 2.8, 3.1, -4.9])
print(f"Original float array: {float_arr}")
int_arr = float_arr.astype(np.int32)
print(f"Converted to int32 (truncates decimal part): {int_arr}")

# Example 2: Converting integers to floats
int_arr2 = np.array([10, 20, 30])
print(f"Original integer array: {int_arr2}")
float_arr2 = int_arr2.astype(np.float64)
print(f"Converted to float64: {float_arr2}")

# Example 3: Converting to boolean
# Non-zero values are converted to True, zero is converted to False.
mixed_arr = np.array([0, 1, -5, 100])
print(f"Original array: {mixed_arr}")
bool_arr = mixed_arr.astype(np.bool_)
print(f"Converted to boolean: {bool_arr}")

# Example 4: Converting strings to numbers
string_arr = np.array(['1.1', '2.2', '3.3'])
print(f"Original string array: {string_arr}")
float_arr3 = string_arr.astype(np.float32)
print(f"Converted to float32: {float_arr3}")

print("-" * 30)


print("--- 3. Data Type Operations and Behavior ---")
# Dtypes affect how operations are performed and the resulting dtype.
# The dtype of the result is generally the "larger" or "more complex" of the
# two dtypes involved.
a = np.array([1, 2, 3], dtype=np.int8)
b = np.array([4.1, 5.2, 6.3], dtype=np.float32)

# Performing an operation between an int8 and a float32 results in a float32 array.
result = a + b
print(f"Array a (dtype: {a.dtype}): {a}")
print(f"Array b (dtype: {b.dtype}): {b}")
print(f"Result of a + b: {result} (dtype: {result.dtype})")

# Dtypes are important for memory usage.
# int8 takes up 1 byte per element, while int64 takes up 8 bytes.
arr_int8 = np.arange(1000, dtype=np.int8)
arr_int64 = np.arange(1000, dtype=np.int64)
print(f"Memory used by 1000 int8 elements: {arr_int8.nbytes} bytes")
print(f"Memory used by 1000 int64 elements: {arr_int64.nbytes} bytes")
print("-" * 30)

# --------------------------------------------------------------------
# 4. Summary of Key NumPy Dtypes
# --------------------------------------------------------------------
# - Integers: `np.int8`, `np.int16`, `np.int32`, `np.int64`
# - Unsigned Integers: `np.uint8`, `np.uint16`, `np.uint32`, `np.uint64`
# - Floats: `np.float16`, `np.float32`, `np.float64`
# - Booleans: `np.bool_`
# - Strings: `np.string_`
# - Complex Numbers: `np.complex64`, `np.complex128`
# - Datetime: `np.datetime64`
# - Timedelta: `np.timedelta64`
