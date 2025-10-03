import numpy as np
import sys # For inspecting memory usage
import os # For cleaning up saved files

print("--- NumPy Arrays: Practice Code ---")

# --- 1. What is a NumPy Array (`ndarray`)? ---
print("\n--- 1. What is a NumPy Array (`ndarray`)? ---")
print("A NumPy array, formally called an `ndarray`, is a multi-dimensional container of items of the same type and size.")
print("It's the fundamental data structure in NumPy and the primary reason for NumPy's efficiency in numerical operations.")
print("Key characteristics:")
print(" - **Homogeneous:** All elements in an `ndarray` must be of the same data type (e.g., all integers, all floats).")
print(" - **Fixed Size:** Once created, the size of an `ndarray` cannot be changed (though you can create new ones).")
print(" - **Fast Operations:** Operations on `ndarrays` are often implemented in C, making them much faster than Python lists for large numerical datasets.")
print(" - **Memory Efficient:** Stores data more compactly than Python lists.")


# --- 2. Creating NumPy Arrays ---
print("\n--- 2. Creating NumPy Arrays ---")

# 2.1 From Python Lists/Tuples (`np.array()`)
list_1d = [1, 2, 3, 4, 5]
array_1d = np.array(list_1d)
print(f"\nArray from 1D list: {array_1d}")
print(f"Type: {type(array_1d)}")
print(f"Data Type (dtype): {array_1d.dtype}") # Often int64 or int32 depending on system

list_2d = [[10, 11, 12], [13, 14, 15]]
array_2d = np.array(list_2d)
print(f"\nArray from 2D list (list of lists):\n{array_2d}")

# Explicitly specifying data type (`dtype`)
array_float = np.array([1, 2, 3], dtype=np.float64)
print(f"\nArray with explicit float64 dtype: {array_float} (dtype: {array_float.dtype})")

array_bool = np.array([True, False, True])
print(f"Array with boolean dtype: {array_bool} (dtype: {array_bool.dtype})")


# 2.2 Arrays with Initial Placeholders (`np.zeros`, `np.ones`, `np.empty`)
arr_zeros = np.zeros((2, 3)) # 2 rows, 3 columns, all zeros
print(f"\nArray of zeros (2x3):\n{arr_zeros}")

arr_ones = np.ones((4,)) # A 1D array of 4 ones
print(f"Array of ones (1D, size 4): {arr_ones}")

arr_full = np.full((2, 2), 7) # All elements are 7
print(f"Array filled with 7s (2x2):\n{arr_full}")

arr_empty = np.empty((2, 2)) # Contains uninitialized (garbage) data, fast to create
print(f"\nEmpty array (2x2):\n{arr_empty}") # Content will vary


# 2.3 Arrays from Numerical Ranges (`np.arange`, `np.linspace`)
arr_arange = np.arange(0, 10, 2) # Start (inclusive), Stop (exclusive), Step
print(f"\nArray from arange(0, 10, 2): {arr_arange}")

arr_linspace = np.linspace(0, 1, 5) # Start (inclusive), Stop (inclusive), Number of elements
print(f"Array from linspace(0, 1, 5): {arr_linspace}")


# 2.4 Random Arrays (`np.random`)
arr_rand_uniform = np.random.rand(2, 2) # Random floats from uniform distribution [0, 1)
print(f"\nRandom array (uniform, 2x2):\n{arr_rand_uniform}")

arr_rand_normal = np.random.randn(3, 1) # Random floats from standard normal distribution
print(f"Random array (normal, 3x1):\n{arr_rand_normal}")

arr_rand_int = np.random.randint(5, 10, size=(2, 3)) # Random integers from 5 (inclusive) to 10 (exclusive)
print(f"Random integers (5-9, 2x3):\n{arr_rand_int}")


# --- 3. Array Attributes ---
print("\n--- 3. Array Attributes ---")
my_array = np.array([[10, 20, 30], [40, 50, 60]])
print(f"\nMy array:\n{my_array}")

print(f"Number of dimensions (`ndim`): {my_array.ndim}") # 2 for a 2D array
print(f"Shape (`shape`): {my_array.shape}") # (rows, columns) -> (2, 3)
print(f"Total number of elements (`size`): {my_array.size}") # 2 * 3 = 6
print(f"Data type of elements (`dtype`): {my_array.dtype}") # int64
print(f"Size of each element in bytes (`itemsize`): {my_array.itemsize}") # 8 bytes for int64
print(f"Total bytes consumed by the array (`nbytes`): {my_array.nbytes}") # 6 * 8 = 48 bytes


# --- 4. Array Indexing and Slicing ---
print("\n--- 4. Array Indexing and Slicing ---")
arr_indexing = np.arange(10, 100, 10) # [10 20 30 40 50 60 70 80 90]
print(f"\n1D array: {arr_indexing}")
print(f"Element at index 0: {arr_indexing[0]}") # 10
print(f"Element at index 3: {arr_indexing[3]}") # 40
print(f"Last element: {arr_indexing[-1]}") # 90

print(f"Slice from index 2 to 5 (exclusive): {arr_indexing[2:5]}") # [30 40 50]
print(f"Slice from start to index 4 (exclusive): {arr_indexing[:4]}") # [10 20 30 40]
print(f"Slice from index 5 to end: {arr_indexing[5:]}") # [60 70 80 90]
print(f"Slice with step (every 2nd element): {arr_indexing[::2]}") # [10 30 50 70 90]


arr_2d_indexing = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
print(f"\n2D array:\n{arr_2d_indexing}")
print(f"Element at row 1, column 2: {arr_2d_indexing[1, 2]}") # 7
print(f"First row: {arr_2d_indexing[0, :]}") # [1 2 3 4]
print(f"Second column: {arr_2d_indexing[:, 1]}") # [2 6 10]
print(f"Slice rows 0 to 1, columns 2 to 3:\n{arr_2d_indexing[0:2, 2:4]}") # [[3 4], [7 8]]
print(f"Specific elements (diagonal-like): {arr_2d_indexing[[0, 1, 2], [0, 1, 2]]}") # [1 6 11]

# 4.1 Boolean Indexing
print("\n--- 4.1 Boolean Indexing ---")
data = np.array([10, 5, 20, 15, 25, 8])
print(f"Original data for boolean indexing: {data}")
condition = (data > 12)
print(f"Boolean condition (data > 12): {condition}")
print(f"Elements satisfying condition: {data[condition]}") # [20 15 25]

# Using boolean indexing to modify values
data[data < 10] = 0
print(f"Data after setting elements < 10 to 0: {data}") # [10  0 20 15 25  0]


# 4.2 Fancy Indexing
print("\n--- 4.2 Fancy Indexing ---")
arr_fancy = np.array(['A', 'B', 'C', 'D', 'E'])
indices = np.array([0, 2, 4]) # Array of indices
print(f"Original array: {arr_fancy}")
print(f"Elements at specific indices {indices}: {arr_fancy[indices]}") # ['A' 'C' 'E']

# Fancy indexing for 2D arrays (selecting specific rows/columns)
arr_fancy_2d = np.arange(1, 17).reshape(4, 4)
print(f"\n2D array for fancy indexing:\n{arr_fancy_2d}")
selected_rows = arr_fancy_2d[[0, 2]] # Select row 0 and row 2
print(f"Selected rows 0 and 2:\n{selected_rows}")


# --- 5. Array Reshaping ---
print("\n--- 5. Array Reshaping ---")
arr_to_reshape = np.arange(1, 13) # 1D array from 1 to 12
print(f"\nOriginal 1D array: {arr_to_reshape}")

# `reshape()`: Returns a new array with a new shape (doesn't modify original)
reshaped_2d = arr_to_reshape.reshape(3, 4) # 3 rows, 4 columns
print(f"Reshaped to (3,4):\n{reshaped_2d}")

# Using -1 to automatically calculate a dimension
reshaped_auto_row = arr_to_reshape.reshape(-1, 3) # Auto-calculate rows, 3 columns
print(f"Reshaped to (-1, 3):\n{reshaped_auto_row}")

# Adding a new axis (`np.newaxis` or `None`)
arr_add_axis = np.array([1, 2, 3])
print(f"\nOriginal array shape: {arr_add_axis.shape}") # (3,)
arr_row_vector = arr_add_axis[np.newaxis, :] # Make it a row vector (1 row, 3 columns)
print(f"As row vector (np.newaxis): {arr_row_vector}, shape: {arr_row_vector.shape}") # [[1 2 3]], (1, 3)
arr_col_vector = arr_add_axis[:, np.newaxis] # Make it a column vector (3 rows, 1 column)
print(f"As col vector (np.newaxis):\n{arr_col_vector}, shape: {arr_col_vector.shape}") # [[1],[2],[3]], (3, 1)

# `ravel()` vs `flatten()`: Flattening an array back to 1D
arr_flat = reshaped_2d.ravel() # Returns a view (if possible) or a copy. Changes to view affect original.
print(f"\nFlattened using ravel(): {arr_flat}")

arr_flat_copy = reshaped_2d.flatten() # Always returns a copy. Changes to copy do NOT affect original.
print(f"Flattened using flatten(): {arr_flat_copy}")


# --- 6. Array Concatenation and Splitting ---
print("\n--- 6. Array Concatenation and Splitting ---")
arr_a = np.array([[1, 2], [3, 4]])
arr_b = np.array([[5, 6], [7, 8]])
print(f"\nArray A:\n{arr_a}")
print(f"Array B:\n{arr_b}")

# Concatenation along rows (vertical stacking, axis=0)
concat_v = np.concatenate((arr_a, arr_b), axis=0)
print(f"\nConcatenated vertically (axis=0):\n{concat_v}")
print(f"Same using np.vstack():\n{np.vstack((arr_a, arr_b))}")

# Concatenation along columns (horizontal stacking, axis=1)
concat_h = np.concatenate((arr_a, arr_b), axis=1)
print(f"\nConcatenated horizontally (axis=1):\n{concat_h}")
print(f"Same using np.hstack():\n{np.hstack((arr_a, arr_b))}")

# Splitting arrays
arr_to_split = np.arange(1, 10).reshape(3, 3)
print(f"\nArray to split:\n{arr_to_split}")

# Split horizontally (into 3 arrays, each with 1 row)
split_h_result = np.split(arr_to_split, 3, axis=0)
print(f"\nSplit horizontally (axis=0):\n{split_h_result[0]}\n---\n{split_h_result[1]}\n---\n{split_h_result[2]}")

# Split vertically (into 3 arrays, each with 1 column)
split_v_result = np.split(arr_to_split, 3, axis=1)
print(f"\nSplit vertically (axis=1):\n{split_v_result[0]}\n{split_v_result[1]}\n{split_v_result[2]}")


# --- 7. Element-wise Operations (Vectorization) ---
print("\n--- 7. Element-wise Operations (Vectorization) ---")
# NumPy's greatest strength is performing operations on entire arrays quickly.
arr_op1 = np.array([1, 2, 3, 4])
arr_op2 = np.array([5, 6, 7, 8])
print(f"\nArray 1: {arr_op1}")
print(f"Array 2: {arr_op2}")

print(f"Addition (element-wise): {arr_op1 + arr_op2}") # [ 6  8 10 12]
print(f"Multiplication (element-wise): {arr_op1 * arr_op2}") # [ 5 12 21 32]
print(f"Division: {arr_op2 / arr_op1}") # [5.   3.   2.33 2.  ]
print(f"Powers: {arr_op1 ** 2}") # [ 1  4  9 16]

# Comparison operations also work element-wise
print(f"Array 1 > Array 2: {arr_op1 > arr_op2}") # [False False False False]
print(f"Array 1 == 3: {arr_op1 == 3}") # [False False True False]

# Universal Functions (Ufuncs): math functions applied element-wise
arr_ufunc = np.array([-1, 0, 1, 2.5, 4])
print(f"\nArray for Ufuncs: {arr_ufunc}")
print(f"Absolute values: {np.abs(arr_ufunc)}")
print(f"Square root: {np.sqrt(arr_ufunc)}") # RuntimeWarning for negative number
print(f"Exponential: {np.exp(arr_ufunc)}")
print(f"Sine: {np.sin(arr_ufunc)}")


# --- 8. Aggregation Functions ---
print("\n--- 8. Aggregation Functions ---")
data_agg = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(f"\nData for aggregation:\n{data_agg}")

print(f"Sum of all elements: {np.sum(data_agg)}")
print(f"Mean of all elements: {np.mean(data_agg)}")
print(f"Maximum element: {np.max(data_agg)}")
print(f"Minimum element: {np.min(data_agg)}")
print(f"Standard Deviation: {np.std(data_agg):.2f}")

# Aggregation along a specific axis
# `axis=0` performs operation down the columns
print(f"\nSum along columns (axis=0): {np.sum(data_agg, axis=0)}") # [120 150 180]
print(f"Mean along columns (axis=0): {np.mean(data_agg, axis=0)}") # [40. 50. 60.]

# `axis=1` performs operation across the rows
print(f"\nSum along rows (axis=1): {np.sum(data_agg, axis=1)}") # [ 60 150 240]
print(f"Max along rows (axis=1): {np.max(data_agg, axis=1)}") # [30 60 90]

# `argmin()` and `argmax()` return indices of min/max
print(f"Index of max element (flattened): {np.argmax(data_agg)}") # 8 (value 90)
print(f"Indices of max elements along columns (axis=0): {np.argmax(data_agg, axis=0)}") # [2 2 2] (row index for max in each col)


# --- 9. Broadcasting Rules ---
print("\n--- 9. Broadcasting Rules ---")
print("Broadcasting allows NumPy to perform operations on arrays of different shapes by effectively 'stretching' the smaller array.")
print("This happens without making copies of data, making it very efficient.")
print("Rules: Dimensions are compatible if they are equal, or one of them is 1.")

A = np.array([[1, 2, 3], [4, 5, 6]]) # Shape (2, 3)
B = np.array([10, 20, 30])           # Shape (3,)
C = 5                                # Scalar
D = np.array([[100], [200]])         # Shape (2, 1)

print(f"\nArray A (2,3):\n{A}")
print(f"Array B (3,):\n{B}")
print(f"Scalar C:\n{C}")
print(f"Array D (2,1):\n{D}")

print(f"\nA + C (scalar broadcasting):\n{A + C}")
print(f"\nA + B (row vector broadcasting):\n{A + B}")
print(f"\nA + D (column vector broadcasting):\n{A + D}")

# An example where broadcasting doesn't work (incompatible shapes)
try:
    E = np.array([1, 2]) # Shape (2,)
    print(f"\nAttempting A (2,3) + E (2,):")
    print(A + E) # This will raise a ValueError
except ValueError as e:
    print(f"Caught expected error: {e} (Shapes (2,3) and (2,) are not broadcast compatible)")


# --- 10. Saving and Loading Arrays ---
print("\n--- 10. Saving and Loading Arrays ---")
# `.npy` format (single array)
array_to_save = np.random.rand(5, 5)
npy_filename = "saved_array.npy"

print(f"\nSaving a single array to '{npy_filename}'.")
np.save(npy_filename, array_to_save)
print(f"Array saved: {array_to_save[:2, :2]}...")

loaded_array = np.load(npy_filename)
print(f"Loaded array from '{npy_filename}':\n{loaded_array[:2, :2]}...")

# `.npz` format (multiple arrays)
array1 = np.arange(10)
array2 = np.linspace(0, 1, 5)
npz_filename = "multiple_arrays.npz"

print(f"\nSaving multiple arrays to '{npz_filename}'.")
np.savez(npz_filename, arr1=array1, arr2=array2)
print("Multiple arrays saved.")

loaded_npz = np.load(npz_filename)
print(f"Keys in loaded .npz file: {list(loaded_npz.keys())}")
print(f"Loaded 'arr1': {loaded_npz['arr1']}")
print(f"Loaded 'arr2': {loaded_npz['arr2']}")

# Clean up created files
if os.path.exists(npy_filename):
    os.remove(npy_filename)
if os.path.exists(npz_filename):
    os.remove(npz_filename)
print("\nCleaned up saved .npy and .npz files.")

print("\n--- End of NumPy Arrays Practice Code ---")