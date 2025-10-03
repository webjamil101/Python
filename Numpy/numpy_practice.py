import numpy as np
import sys # For checking object size (memory usage)
import os # For cleaning up saved files

print("--- Python NumPy: Practice Code ---")

# --- 1. What is NumPy? Why use it? ---
print("\n--- 1. What is NumPy? Why use it? ---")
print("NumPy provides the `ndarray` (N-dimensional array) object, which is a fast and efficient way to store and manipulate large datasets.")
print("Key benefits:")
print(" - **Performance:** NumPy operations are often implemented in C/Fortran, making them much faster than Python lists for numerical tasks.")
print(" - **Memory Efficiency:** NumPy arrays consume less memory than Python lists for the same data.")
print(" - **Convenience:** Provides a vast collection of high-level mathematical functions to operate on these arrays.")
print(" - **Foundation for Data Science:** It's the core library for Pandas, Matplotlib, SciPy, Scikit-learn, etc.")

# Comparison: Python List vs. NumPy Array (Memory and Speed Concept)
list_data = list(range(1_000_000))
array_data = np.arange(1_000_000)

print(f"\nMemory Usage (conceptually):")
print(f"Size of Python list (1M elements): {sys.getsizeof(list_data)} bytes")
print(f"Size of NumPy array (1M elements): {sys.getsizeof(array_data)} bytes (significantly smaller!)")

# Speed (conceptually, uncomment to run timing)
# import time
# start = time.time()
# list_sum = sum(list_data)
# end = time.time()
# print(f"Time for list sum: {end - start:.6f} seconds")

# start = time.time()
# array_sum = np.sum(array_data)
# end = time.time()
# print(f"Time for array sum: {end - start:.6f} seconds (much faster!)")


# --- 2. Creating NumPy Arrays (ndarrays) ---
print("\n--- 2. Creating NumPy Arrays (ndarrays) ---")

# 2.1 From Python Lists or Tuples
arr1d = np.array([1, 2, 3, 4, 5])
print(f"1D Array from list: {arr1d}")
print(f"Type of arr1d: {type(arr1d)}")
print(f"Data type of elements: {arr1d.dtype}") # int64 by default on most systems

arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n2D Array from list of lists:\n{arr2d}")

arr_float = np.array([1.0, 2.5, 3.7])
print(f"\nArray with float dtype: {arr_float} (dtype: {arr_float.dtype})")

# Specify dtype explicitly
arr_int32 = np.array([1, 2, 3], dtype=np.int32)
print(f"Array with explicit int32 dtype: {arr_int32} (dtype: {arr_int32.dtype})")

# 2.2 Zeros, Ones, Empty Arrays
arr_zeros = np.zeros((3, 4)) # 3 rows, 4 columns
print(f"\nArray of zeros (3x4):\n{arr_zeros}")

arr_ones = np.ones((2, 2))
print(f"\nArray of ones (2x2):\n{arr_ones}")

arr_empty = np.empty((2, 3)) # Contains uninitialized (random) data
print(f"\nEmpty array (2x3):\n{arr_empty}") # Content will vary

# 2.3 Arange and Linspace (like Python's range but for arrays)
arr_range = np.arange(10) # 0 to 9
print(f"\nArray from arange(10): {arr_range}")

arr_range_step = np.arange(0, 10, 2) # Start, Stop (exclusive), Step
print(f"Array from arange(0, 10, 2): {arr_range_step}")

arr_linspace = np.linspace(0, 1, 5) # Start, Stop (inclusive), Number of elements
print(f"Array from linspace(0, 1, 5): {arr_linspace}")

# 2.4 Random Arrays
# `np.random.rand()`: Uniform distribution (0 to 1)
arr_rand = np.random.rand(2, 3)
print(f"\nRandom array (uniform):\n{arr_rand}")

# `np.random.randn()`: Standard normal distribution (mean 0, variance 1)
arr_randn = np.random.randn(2, 2)
print(f"Random array (normal):\n{arr_randn}")

# `np.random.randint(low, high, size)`: Random integers
arr_randint = np.random.randint(0, 10, size=(3, 3)) # Integers from 0 (inclusive) to 10 (exclusive)
print(f"Random integers (0-9, 3x3):\n{arr_randint}")


# --- 3. Array Attributes ---
print("\n--- 3. Array Attributes ---")
my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\nMy array:\n{my_array}")
print(f"Number of dimensions (ndim): {my_array.ndim}")
print(f"Shape (rows, columns): {my_array.shape}")
print(f"Total number of elements (size): {my_array.size}")
print(f"Data type of elements (dtype): {my_array.dtype}")
print(f"Item size (bytes per element): {my_array.itemsize}")
print(f"Total bytes consumed: {my_array.nbytes}")


# --- 4. Array Indexing and Slicing ---
print("\n--- 4. Array Indexing and Slicing ---")
arr = np.array([10, 20, 30, 40, 50, 60, 70])
print(f"\n1D array: {arr}")
print(f"Element at index 0: {arr[0]}")
print(f"Element at index -1 (last): {arr[-1]}")
print(f"Slice from index 2 to 5 (exclusive): {arr[2:5]}") # [30, 40, 50]
print(f"Slice from beginning to index 3 (exclusive): {arr[:3]}") # [10, 20, 30]
print(f"Slice from index 4 to end: {arr[4:]}") # [50, 60, 70]
print(f"Slice with step (every 2nd element): {arr[::2]}") # [10, 30, 50, 70]

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\n2D array:\n{arr2d}")
print(f"Element at row 0, col 1: {arr2d[0, 1]}") # 2
print(f"First row: {arr2d[0, :]}") # [1, 2, 3]
print(f"First column: {arr2d[:, 0]}") # [1, 4, 7]
print(f"Slice rows 0-1, columns 1-2:\n{arr2d[0:2, 1:3]}") # [[2, 3], [5, 6]]

# 4.1 Boolean Indexing
print("\n--- 4.1 Boolean Indexing ---")
arr_bool = np.array([10, 5, 20, 15, 25, 8])
print(f"Array for boolean indexing: {arr_bool}")
filter_condition = (arr_bool > 10)
print(f"Boolean mask (elements > 10): {filter_condition}")
print(f"Elements greater than 10: {arr_bool[filter_condition]}") # [20, 15, 25]

# 4.2 Fancy Indexing
print("\n--- 4.2 Fancy Indexing ---")
arr_fancy = np.array(['a', 'b', 'c', 'd', 'e'])
indices = [0, 2, 4]
print(f"Array for fancy indexing: {arr_fancy}")
print(f"Elements at indices {indices}: {arr_fancy[indices]}") # ['a', 'c', 'e']

arr2d_fancy = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(f"\n2D array for fancy indexing:\n{arr2d_fancy}")
rows = [0, 2]
cols = [1, 0]
# Selects (0,1) and (2,0) -> 20 and 70
print(f"Elements at (rows, cols): {arr2d_fancy[rows, cols]}")


# --- 5. Array Reshaping ---
print("\n--- 5. Array Reshaping ---")
arr_reshape = np.arange(12) # 0 to 11
print(f"Original array (1D): {arr_reshape}")

reshaped_arr = arr_reshape.reshape(3, 4) # Reshape to 3 rows, 4 columns
print(f"Reshaped to (3,4):\n{reshaped_arr}")

# Using -1 to infer dimension
reshaped_auto_col = arr_reshape.reshape(4, -1) # 4 rows, auto-calculate columns
print(f"Reshaped to (4, -1):\n{reshaped_auto_col}")

# Flattening an array (back to 1D)
flat_arr_ravel = reshaped_arr.ravel() # Returns a view if possible (faster)
print(f"Flattened using ravel(): {flat_arr_ravel}")

flat_arr_flatten = reshaped_arr.flatten() # Always returns a copy (slower but safer)
print(f"Flattened using flatten(): {flat_arr_flatten}")


# --- 6. Array Concatenation and Splitting ---
print("\n--- 6. Array Concatenation and Splitting ---")
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(f"\nArray A:\n{a}")
print(f"Array B:\n{b}")

# Concatenate along rows (axis=0) - vertical stack
concat_rows = np.concatenate((a, b), axis=0)
print(f"\nConcatenated along rows (axis=0):\n{concat_rows}")
# Equivalent to np.vstack((a, b))
print(f"vstack((A,B)):\n{np.vstack((a,b))}")

# Concatenate along columns (axis=1) - horizontal stack
concat_cols = np.concatenate((a, b), axis=1)
print(f"\nConcatenated along columns (axis=1):\n{concat_cols}")
# Equivalent to np.hstack((a, b))
print(f"hstack((A,B)):\n{np.hstack((a,b))}")

# Splitting arrays
arr_split = np.arange(16).reshape(4, 4)
print(f"\nArray to split:\n{arr_split}")

# Split into 2 equal parts horizontally (along rows)
split_h = np.split(arr_split, 2, axis=0)
print(f"\nSplit horizontally (axis=0):\n{split_h[0]}\n---\n{split_h[1]}")

# Split into 4 equal parts vertically (along columns)
split_v = np.split(arr_split, 4, axis=1)
print(f"\nSplit vertically (axis=1) (first 2 parts):\n{split_v[0]}\n---\n{split_v[1]}")


# --- 7. Basic Operations ---
print("\n--- 7. Basic Operations ---")
arr_ops1 = np.array([1, 2, 3])
arr_ops2 = np.array([4, 5, 6])
print(f"\nArray 1: {arr_ops1}")
print(f"Array 2: {arr_ops2}")

# Element-wise arithmetic
print(f"Addition: {arr_ops1 + arr_ops2}") # [5 7 9]
print(f"Subtraction: {arr_ops2 - arr_ops1}") # [3 3 3]
print(f"Multiplication: {arr_ops1 * arr_ops2}") # [4 10 18]
print(f"Division: {arr_ops2 / arr_ops1}") # [4.  2.5 2. ]
print(f"Exponentiation: {arr_ops1 ** 2}") # [1 4 9]

# Matrix multiplication (dot product)
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
print(f"\nMatrix A:\n{matrix_a}")
print(f"Matrix B:\n{matrix_b}")
print(f"Matrix multiplication (A @ B):\n{matrix_a @ matrix_b}")
# Equivalent: np.dot(matrix_a, matrix_b)
print(f"Matrix multiplication (np.dot(A, B)):\n{np.dot(matrix_a, matrix_b)}")


# Comparison operations (element-wise)
print(f"\nArray 1 > 2: {arr_ops1 > 2}") # [False False True]
print(f"Array 1 == Array 2: {arr_ops1 == arr_ops2}") # [False False False]

# Universal Functions (ufuncs): apply a function element-wise
arr_ufunc = np.array([0, np.pi/2, np.pi])
print(f"\nArray for ufuncs: {arr_ufunc}")
print(f"np.sin(arr_ufunc): {np.sin(arr_ufunc)}")
print(f"np.exp(arr_ufunc): {np.exp(arr_ufunc)}")
print(f"np.sqrt(arr_ops2): {np.sqrt(arr_ops2)}")


# --- 8. Aggregate Functions ---
print("\n--- 8. Aggregate Functions ---")
data_agg = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\nData for aggregation:\n{data_agg}")

print(f"Sum of all elements: {data_agg.sum()}")
print(f"Minimum of all elements: {data_agg.min()}")
print(f"Maximum of all elements: {data_agg.max()}")
print(f"Mean of all elements: {data_agg.mean()}")
print(f"Standard deviation of all elements: {data_agg.std():.2f}")

# Aggregation along an axis
print(f"\nSum along rows (axis=0): {data_agg.sum(axis=0)}") # Sum of columns
print(f"Sum along columns (axis=1): {data_agg.sum(axis=1)}") # Sum of rows

print(f"Max along rows (axis=0): {data_agg.max(axis=0)}")
print(f"Min along columns (axis=1): {data_agg.min(axis=1)}")

print(f"Index of max element (flattened): {data_agg.argmax()}") # Returns flattened index
print(f"Index of max element along rows (axis=0): {data_agg.argmax(axis=0)}")
print(f"Index of max element along columns (axis=1): {data_agg.argmax(axis=1)}")


# --- 9. Broadcasting ---
print("\n--- 9. Broadcasting ---")
print("Broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations.")
print("It automatically 'stretches' smaller arrays to match the shape of larger arrays, provided they are compatible.")

arr_broad = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 10
print(f"\nArray for broadcasting:\n{arr_broad}")
print(f"Scalar: {scalar}")
print(f"Array + Scalar:\n{arr_broad + scalar}") # Scalar is broadcast to all elements

row_vector = np.array([100, 200, 300])
print(f"\nRow vector: {row_vector}")
print(f"Array + Row Vector (broadcast):\n{arr_broad + row_vector}")

# Example of incompatible shapes (will raise ValueError)
# col_vector = np.array([[10], [20]]) # Shape (2,1)
# print(f"Array + Col Vector:\n{arr_broad + col_vector}") # This would work.
# print(f"Array (2,3) + Incompatible Array (2,2) - will error:\n")
# try:
#    incompatible_arr = np.array([[1,2], [3,4]])
#    print(arr_broad + incompatible_arr)
# except ValueError as e:
#    print(f"Caught expected error: {e}")


# --- 10. Linear Algebra (Brief) ---
print("\n--- 10. Linear Algebra (Brief) ---")
# Dot product (already covered with `@`)
vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])
print(f"\nDot product of {vec1} and {vec2}: {np.dot(vec1, vec2)}")

# Inverse of a matrix
try:
    square_matrix = np.array([[1, 2], [3, 4]])
    inv_matrix = np.linalg.inv(square_matrix)
    print(f"\nOriginal matrix:\n{square_matrix}")
    print(f"Inverse matrix:\n{inv_matrix}")
    print(f"Original dot Inverse (should be identity):\n{np.dot(square_matrix, inv_matrix)}")
except np.linalg.LinAlgError:
    print("Matrix is singular and cannot be inverted.")


# --- 11. Saving and Loading Arrays ---
print("\n--- 11. Saving and Loading Arrays ---")
filename_npy = "my_numpy_array.npy"
filename_npz = "my_multiple_arrays.npz"

data_to_save = np.arange(100).reshape(10, 10)
print(f"\nSaving array to '{filename_npy}':\n{data_to_save[:2, :2]}...")
np.save(filename_npy, data_to_save)
print(f"Array saved to '{filename_npy}'.")

loaded_data = np.load(filename_npy)
print(f"Loaded array from '{filename_npy}':\n{loaded_data[:2, :2]}...")

# Saving multiple arrays in a single .npz file
array_x = np.linspace(0, 10, 50)
array_y = np.sin(array_x)
print(f"\nSaving multiple arrays to '{filename_npz}'.")
np.savez(filename_npz, x_data=array_x, y_data=array_y)
print(f"Multiple arrays saved to '{filename_npz}'.")

loaded_multiple = np.load(filename_npz)
print(f"Keys in loaded .npz: {list(loaded_multiple.keys())}")
print(f"Loaded x_data (first 5): {loaded_multiple['x_data'][:5]}")
print(f"Loaded y_data (first 5): {loaded_multiple['y_data'][:5]}")

# Clean up created files
if os.path.exists(filename_npy):
    os.remove(filename_npy)
if os.path.exists(filename_npz):
    os.remove(filename_npz)
print("\nCleaned up saved .npy and .npz files.")

print("\n--- End of Python NumPy Practice Code ---")



# ====================================================================
# Comprehensive NumPy Guide in Code
# This document covers the essential aspects of NumPy:
# creation, inspection, data types, subsetting, arithmetic,
# and saving/loading of arrays.
# ====================================================================

import numpy as np
import os

# --- 1. Array Creation ---
# NumPy provides multiple functions for creating arrays.

# Create a 1D array from a list
arr_1d = np.array([1, 2, 3, 4, 5])

# Create a 2D array (matrix)
arr_2d = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])

# Create an array of a specific shape with zeros
zeros_arr = np.zeros((2, 3))

# Create an array with a range of numbers
range_arr = np.arange(10, 20, 2)  # Start, stop (exclusive), step

# Create an array with evenly spaced numbers
linspace_arr = np.linspace(0, 1, 5) # Start, stop, number of elements

print("--- 1. Array Creation ---")
print("1D Array:", arr_1d)
print("2D Array (Matrix):\n", arr_2d)
print("Zeros Array:\n", zeros_arr)
print("Range Array:", range_arr)
print("Linspace Array:", linspace_arr)
print("-" * 40)


# --- 2. Array Inspection ---
# These attributes help you understand the array's properties.

print("--- 2. Array Inspection ---")
print("Inspecting a 2D array:")
print(f"  Shape (dimensions): {arr_2d.shape}")
print(f"  Number of dimensions: {arr_2d.ndim}")
print(f"  Total number of elements: {arr_2d.size}")
print(f"  Data type of elements: {arr_2d.dtype}")
print(f"  Size of each element: {arr_2d.itemsize} bytes")
print(f"  Total memory used: {arr_2d.nbytes} bytes")
print("-" * 40)


# --- 3. Data Types and Conversion ---
# The 'dtype' defines the type of data in the array.

# Create an array with a specific dtype
int32_arr = np.arange(5, dtype=np.int32)
print("--- 3. Data Types and Conversion ---")
print(f"Array with dtype np.int32: {int32_arr}")
print(f"  Data type: {int32_arr.dtype}")

# Convert an array to a different dtype using .astype()
float_arr = int32_arr.astype(np.float64)
print(f"Converted to np.float64: {float_arr}")
print(f"  Data type: {float_arr.dtype}")
print("-" * 40)


# --- 4. Subsetting and Slicing ---
# Accessing elements and creating sub-arrays.

print("--- 4. Subsetting and Slicing ---")
print("Original 1D Array:", arr_1d)

# Basic slicing: [start:end:step]
print(f"Slice from index 1 to 4 (exclusive): {arr_1d[1:4]}")
print(f"All elements with a step of 2: {arr_1d[::2]}")
print(f"Reverse the array: {arr_1d[::-1]}")

# Integer array indexing
indices = np.array([0, 4, 2])
print(f"Elements at indices [0, 4, 2]: {arr_1d[indices]}")

# Boolean masking
mask = arr_1d > 3
print(f"Boolean mask (arr_1d > 3): {mask}")
print(f"Elements greater than 3: {arr_1d[mask]}")
print("-" * 40)


# --- 5. Arithmetic Operations ---
# Operations are element-wise by default.

print("--- 5. Arithmetic Operations ---")
arr_a = np.array([1, 2, 3])
arr_b = np.array([4, 5, 6])
print("Arrays arr_a:", arr_a, " and arr_b:", arr_b)

# Element-wise operations using operators
print(f"Element-wise addition: {arr_a + arr_b}")
print(f"Element-wise multiplication: {arr_a * arr_b}")

# Element-wise operations using built-in functions (ufuncs)
print(f"np.add(arr_a, arr_b): {np.add(arr_a, arr_b)}")
print(f"np.multiply(arr_a, arr_b): {np.multiply(arr_a, arr_b)}")

# Broadcasting: Operation between arrays of different shapes
print("Broadcasting: arr_a + 10 =", arr_a + 10)

# Matrix multiplication using the @ operator
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
print("Matrix 1:\n", matrix1)
print("Matrix 2:\n", matrix2)
print("Matrix multiplication (matrix1 @ matrix2):\n", matrix1 @ matrix2)
print("-" * 40)


# --- 6. Saving and Loading Arrays ---
# Save data to disk for later use.

# File paths
binary_file = 'my_array.npy'
text_file = 'my_array.txt'

# Save a single array to a binary .npy file (NumPy's preferred format)
np.save(binary_file, arr_2d)
print(f"Saved array to '{binary_file}'")

# Load the array back from the binary file
loaded_binary_arr = np.load(binary_file)
print("Loaded array from binary file:\n", loaded_binary_arr)

# Save an array to a human-readable text file
np.savetxt(text_file, arr_2d, delimiter=',', fmt='%.2f')
print(f"Saved array to '{text_file}'")

# Load the array from the text file
loaded_text_arr = np.loadtxt(text_file, delimiter=',')
print("Loaded array from text file:\n", loaded_text_arr)
print("-" * 40)

# Clean up the created files
if os.path.exists(binary_file):
    os.remove(binary_file)
if os.path.exists(text_file):
    os.remove(text_file)
print("Cleaned up the created files.")
