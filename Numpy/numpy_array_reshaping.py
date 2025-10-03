import numpy as np

print("--- NumPy Array Reshaping: Practice Code ---")

# --- 1. What is Array Reshaping? ---
print("\n--- 1. What is Array Reshaping? ---")
print("Reshaping an array means changing the number of elements along each dimension, while keeping the total number of elements constant.")
print("It allows you to transform a 1D array into a 2D matrix, a 2D matrix into a 3D tensor, and so on, or vice versa.")
print("The data itself is not changed or copied (unless explicitly requested or necessary, e.g., for non-contiguous arrays).")


# --- 2. `reshape()` Method ---
print("\n--- 2. `reshape()` Method ---")
print("The `reshape()` method returns a new array with the same data but a different shape.")
print("It does *not* modify the original array in-place.")

# 2.1 Reshaping a 1D array to a 2D array
arr_1d = np.arange(1, 13) # [ 1  2  3  4  5  6  7  8  9 10 11 12]
print(f"\nOriginal 1D array: {arr_1d} (shape: {arr_1d.shape})")

# Reshape to 3 rows, 4 columns
reshaped_2d = arr_1d.reshape(3, 4)
print(f"Reshaped to (3, 4):\n{reshaped_2d} (shape: {reshaped_2d.shape})")
# Output:
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# Reshape to 4 rows, 3 columns
reshaped_2d_alt = arr_1d.reshape(4, 3)
print(f"Reshaped to (4, 3):\n{reshaped_2d_alt} (shape: {reshaped_2d_alt.shape})")
# Output:
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

# 2.2 Using -1 to infer a dimension
print("\n--- 2.2 Using -1 to Infer a Dimension ---")
print("You can specify -1 for one of the dimensions, and NumPy will automatically calculate the correct size for that dimension.")
# Reshape to 2 rows, automatically calculate columns (12 elements / 2 rows = 6 columns)
auto_cols = arr_1d.reshape(2, -1)
print(f"Reshaped to (2, -1):\n{auto_cols} (shape: {auto_cols.shape})")
# Output:
# [[ 1  2  3  4  5  6]
#  [ 7  8  9 10 11 12]]

# Reshape to automatically calculate rows, 2 columns (12 elements / 2 columns = 6 rows)
auto_rows = arr_1d.reshape(-1, 2)
print(f"Reshaped to (-1, 2):\n{auto_rows} (shape: {auto_rows.shape})")
# Output:
# [[ 1  2]
#  [ 3  4]
#  [ 5  6]
#  [ 7  8]
#  [ 9 10]
#  [11 12]]

# 2.3 Reshaping to a 3D array
arr_3d_reshape = arr_1d.reshape(2, 3, 2) # 2 "pages", 3 rows, 2 columns
print(f"Reshaped to (2, 3, 2):\n{arr_3d_reshape} (shape: {arr_3d_reshape.shape})")
# Output:
# [[[ 1  2]
#   [ 3  4]
#   [ 5  6]]
#
#  [[ 7  8]
#   [ 9 10]
#   [11 12]]]

# 2.4 Important: Total elements must match!
print("\n--- 2.4 Error: Incompatible Shapes ---")
try:
    arr_1d.reshape(5, 3) # 5 * 3 = 15, but arr_1d has 12 elements
except ValueError as e:
    print(f"Caught expected error when reshaping to incompatible size: {e}")


# --- 3. Flattening Arrays (from N-D to 1D) ---
print("\n--- 3. Flattening Arrays ---")
print("Converting a multi-dimensional array back into a 1D array.")

# 3.1 `ravel()`: Returns a *view* (if possible) or a copy
# Changes to the view *will* affect the original array if it's a view.
original_2d = np.array([[10, 11, 12], [13, 14, 15]])
print(f"\nOriginal 2D array:\n{original_2d} (shape: {original_2d.shape})")

raveled_arr = original_2d.ravel()
print(f"Raveled array: {raveled_arr} (shape: {raveled_arr.shape})")

# Demonstrate view behavior (usually, but not guaranteed for complex cases)
print(f"Is raveled_arr a view? (original_2d.base is raveled_arr.base): {original_2d.base is raveled_arr.base}")
raveled_arr[0] = 99
print(f"Raveled array after modification: {raveled_arr}")
print(f"Original 2D array after raveled modification:\n{original_2d}") # Original IS modified!


# 3.2 `flatten()`: Always returns a *copy*
# Changes to the copied array will *not* affect the original.
original_2d = np.array([[10, 11, 12], [13, 14, 15]]) # Reset original
print(f"\nOriginal 2D array (reset):\n{original_2d} (shape: {original_2d.shape})")

flattened_arr = original_2d.flatten()
print(f"Flattened array: {flattened_arr} (shape: {flattened_arr.shape})")

# Demonstrate copy behavior
print(f"Is flattened_arr a view? (original_2d.base is flattened_arr.base): {original_2d.base is flattened_arr.base}")
flattened_arr[0] = 99
print(f"Flattened array after modification: {flattened_arr}")
print(f"Original 2D array after flattened modification:\n{original_2d}") # Original NOT modified!


# --- 4. Adding/Removing Single Dimensions ---
print("\n--- 4. Adding/Removing Single Dimensions ---")

# 4.1 `np.newaxis` or `None`: Adding a new dimension
arr_1d_single = np.array([1, 2, 3, 4])
print(f"\nOriginal 1D array: {arr_1d_single} (shape: {arr_1d_single.shape})")

# Convert to a row vector (1 row, N columns)
row_vector = arr_1d_single[np.newaxis, :]
# Equivalent: row_vector = arr_1d_single[None, :]
print(f"As row vector (np.newaxis, :):\n{row_vector} (shape: {row_vector.shape})")
# Output: [[1 2 3 4]]

# Convert to a column vector (N rows, 1 column)
col_vector = arr_1d_single[:, np.newaxis]
# Equivalent: col_vector = arr_1d_single[:, None]
print(f"As column vector (:, np.newaxis):\n{col_vector} (shape: {col_vector.shape})")
# Output:
# [[1]
#  [2]
#  [3]
#  [4]]

# Add a dimension in the middle (e.g., for specific tensor operations)
arr_add_middle_dim = np.arange(6).reshape(2, 3)
print(f"\nOriginal 2D array:\n{arr_add_middle_dim} (shape: {arr_add_middle_dim.shape})")
expanded_arr = arr_add_middle_dim[:, np.newaxis, :] # Add dim between rows and cols
print(f"Expanded array (add dim in middle):\n{expanded_arr} (shape: {expanded_arr.shape})")
# Output:
# [[[0 1 2]]
#
#  [[3 4 5]]] (shape becomes (2, 1, 3))


# 4.2 `squeeze()`: Removing single-dimensional entries
print("\n--- 4.2 `squeeze()`: Removing Single-Dimensional Entries ---")
print("`squeeze()` removes dimensions of size 1 (i.e., where `shape` has a `1`).")
arr_squeezable = np.array([[[1, 2, 3]]]) # Shape (1, 1, 3)
print(f"\nOriginal squeezable array:\n{arr_squeezable} (shape: {arr_squeezable.shape})")

squeezed_arr = arr_squeezable.squeeze()
print(f"Squeezed array: {squeezed_arr} (shape: {squeezed_arr.shape})")
# Output: [1 2 3] (shape becomes (3,))

# Example with a row vector
squeezed_row_vec = row_vector.squeeze()
print(f"Squeezed row vector: {squeezed_row_vec} (shape: {squeezed_row_vec.shape})")
# Output: [1 2 3 4] (shape becomes (4,))


# --- 5. `resize()` (In-place Reshaping) ---
print("\n--- 5. `resize()` (In-place Reshaping) ---")
print("Unlike `reshape()`, `resize()` *modifies the array in-place*.")
print("It can also change the total number of elements, filling new elements with zeros if needed.")
print("Use with caution as it modifies the original array.")

resize_arr = np.array([1, 2, 3, 4])
print(f"\nOriginal array for resize: {resize_arr} (shape: {resize_arr.shape})")

resize_arr.resize(2, 3) # Resize to 2 rows, 3 columns (total 6 elements)
print(f"Array after resize(2,3):\n{resize_arr} (shape: {resize_arr.shape})")
# Output:
# [[1 2 3]
#  [4 0 0]] (New elements are filled with zeros)

# If you make it smaller, elements are truncated
resize_arr.resize(2, 2)
print(f"Array after resize(2,2):\n{resize_arr} (shape: {resize_arr.shape})")
# Output:
# [[1 2]
#  [3 0]] (Elements 0, 0 are truncated)

# Warning: `resize()` is generally not recommended if the array is a view of another array,
# or if it has external references. It might raise an error or lead to unexpected behavior.
# It's safer to use `reshape()` which returns a new array, or `arr = arr.copy().resize()` if you
# need to modify an array in-place that might have external references.


print("\n--- End of NumPy Array Reshaping Practice Code ---")