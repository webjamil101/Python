import numpy as np

print("--- NumPy Array Concatenation and Splitting: Practice Code ---")

# --- 1. Concatenation (Joining Arrays) ---
print("\n--- 1. Concatenation (Joining Arrays) ---")
print("Concatenation joins two or more arrays along an existing axis.")
print("The arrays must have the same shape along all axes *except* the axis along which they are being joined.")

# 1.1 `np.concatenate()`: The General Purpose Concatenation Function
print("\n--- 1.1 `np.concatenate()`: General Purpose Concatenation ---")
# This is the most versatile function for joining arrays.
# It takes a tuple of arrays to concatenate and an `axis` argument.

# Example 1: Concatenating 1D arrays
arr1_1d = np.array([1, 2, 3])
arr2_1d = np.array([4, 5, 6])
print(f"1D array 1: {arr1_1d}")
print(f"1D array 2: {arr2_1d}")

# Concatenate 1D arrays (default axis is 0, which is the only axis for 1D)
concat_1d = np.concatenate((arr1_1d, arr2_1d))
print(f"Concatenated 1D arrays: {concat_1d}") # Output: [1 2 3 4 5 6]

# Example 2: Concatenating 2D arrays along `axis=0` (row-wise)
arr1_2d = np.array([[1, 2], [3, 4]])
arr2_2d = np.array([[5, 6], [7, 8]])
print(f"\n2D array 1:\n{arr1_2d}")
print(f"2D array 2:\n{arr2_2d}")

concat_rows = np.concatenate((arr1_2d, arr2_2d), axis=0)
print(f"Concatenated along axis=0 (row-wise):\n{concat_rows}")
# Output:
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# Example 3: Concatenating 2D arrays along `axis=1` (column-wise)
concat_cols = np.concatenate((arr1_2d, arr2_2d), axis=1)
print(f"Concatenated along axis=1 (column-wise):\n{concat_cols}")
# Output:
# [[1 2 5 6]
#  [3 4 7 8]]

# Example 4: Concatenating arrays of different compatible shapes
arr_a = np.array([[10, 20]]) # Shape (1, 2)
arr_b = np.array([[30, 40], [50, 60]]) # Shape (2, 2)
print(f"\nArray A:\n{arr_a}")
print(f"Array B:\n{arr_b}")

# Can concatenate along axis=0 if columns match
concat_diff_rows = np.concatenate((arr_a, arr_b), axis=0)
print(f"Concatenating (1,2) and (2,2) along axis=0:\n{concat_diff_rows}")
# Output:
# [[10 20]
#  [30 40]
#  [50 60]]

# Error: Incompatible shapes for concatenation along axis=1
try:
    arr_c = np.array([[1], [2]]) # Shape (2, 1)
    print(f"\nArray A (1,2):\n{arr_a}")
    print(f"Array C (2,1):\n{arr_c}")
    print(f"Attempting to concatenate (1,2) and (2,1) along axis=1 (expect error):")
    np.concatenate((arr_a, arr_c), axis=1)
except ValueError as e:
    print(f"Caught expected error: {e}") # All input array dimensions for the concatenation axis must match exactly, or one of them has to be 1.


# 1.2 `np.vstack()`: Vertical Stacking (Row-wise)
print("\n--- 1.2 `np.vstack()`: Vertical Stacking ---")
print("`vstack()` stacks arrays in sequence vertically (row-wise). It's equivalent to `np.concatenate(..., axis=0)` for 2D arrays.")
print("It handles 1D inputs by converting them to row vectors first.")

arr_v1 = np.array([1, 2, 3]) # 1D
arr_v2 = np.array([4, 5, 6]) # 1D
vstack_1d = np.vstack((arr_v1, arr_v2))
print(f"vstack 1D arrays:\n{vstack_1d} (shape: {vstack_1d.shape})")
# Output:
# [[1 2 3]
#  [4 5 6]]

arr_v3 = np.array([[10, 20]]) # 2D (1,2)
arr_v4 = np.array([[30, 40], [50, 60]]) # 2D (2,2)
vstack_2d = np.vstack((arr_v3, arr_v4))
print(f"vstack 2D arrays:\n{vstack_2d}")
# Output:
# [[10 20]
#  [30 40]
#  [50 60]]


# 1.3 `np.hstack()`: Horizontal Stacking (Column-wise)
print("\n--- 1.3 `np.hstack()`: Horizontal Stacking ---")
print("`hstack()` stacks arrays in sequence horizontally (column-wise). It's equivalent to `np.concatenate(..., axis=1)` for 2D arrays.")
print("It handles 1D inputs by keeping them as 1D (unlike vstack).")

arr_h1 = np.array([1, 2, 3]) # 1D
arr_h2 = np.array([4, 5, 6]) # 1D
hstack_1d = np.hstack((arr_h1, arr_h2))
print(f"hstack 1D arrays: {hstack_1d} (shape: {hstack_1d.shape})")
# Output: [1 2 3 4 5 6]

arr_h3 = np.array([[10], [20]]) # 2D (2,1)
arr_h4 = np.array([[30, 40], [50, 60]]) # 2D (2,2)
hstack_2d = np.hstack((arr_h3, arr_h4))
print(f"hstack 2D arrays:\n{hstack_2d}")
# Output:
# [[10 30 40]
#  [20 50 60]]


# 1.4 `np.dstack()`: Stacking along a Third Axis (Depth-wise)
print("\n--- 1.4 `np.dstack()`: Depth Stacking ---")
print("`dstack()` stacks arrays along the third axis (depth-wise).")
print("This is useful for creating 3D arrays from 2D arrays, or increasing dimensions.")

arr_d1 = np.array([[1, 2], [3, 4]]) # (2,2)
arr_d2 = np.array([[5, 6], [7, 8]]) # (2,2)
print(f"Array D1:\n{arr_d1}")
print(f"Array D2:\n{arr_d2}")
dstack_arr = np.dstack((arr_d1, arr_d2))
print(f"dstack arrays:\n{dstack_arr} (shape: {dstack_arr.shape})")
# Output:
# [[[1 5] [2 6]]
#  [[3 7] [4 8]]] (shape becomes (2, 2, 2))
# For each element [r,c] in input arrays, the new array will have [r,c,0]=arr_d1[r,c] and [r,c,1]=arr_d2[r,c]


# --- 2. Splitting Arrays ---
print("\n--- 2. Splitting Arrays ---")
print("Splitting divides an array into multiple sub-arrays along a specified axis.")

# 2.1 `np.split()`: The General Purpose Splitting Function
print("\n--- 2.1 `np.split()`: General Purpose Splitting ---")
# `np.split(array, indices_or_sections, axis=0)`
# - `array`: The array to be split.
# - `indices_or_sections`:
#   - An integer: Specifies the number of equally sized sub-arrays. (Must divide evenly)
#   - A 1D array of sorted integers: Specifies the indices *before* which to split.

# Example 1: Splitting 1D array into equal sections
arr_split_1d = np.arange(10) # [0 1 2 3 4 5 6 7 8 9]
print(f"\nOriginal 1D array: {arr_split_1d}")
split_equal_sections = np.split(arr_split_1d, 2) # Split into 2 equal parts
print(f"Split into 2 equal sections: {split_equal_sections}")
# Output: [array([0, 1, 2, 3, 4]), array([5, 6, 7, 8, 9])]

# Example 2: Splitting 1D array at specific indices
split_at_indices = np.split(arr_split_1d, [2, 5, 8]) # Split before index 2, 5, and 8
print(f"Split at indices [2, 5, 8]: {split_at_indices}")
# Output: [array([0, 1]), array([2, 3, 4]), array([5, 6, 7]), array([8, 9])]

# Example 3: Splitting 2D array along `axis=0` (row-wise)
arr_split_2d = np.arange(16).reshape(4, 4)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]
print(f"\nOriginal 2D array:\n{arr_split_2d}")

split_rows = np.split(arr_split_2d, 2, axis=0) # Split into 2 equal parts vertically
print(f"Split into 2 equal row sections:\n{split_rows[0]}\n---\n{split_rows[1]}")
# Output:
# [[0 1 2 3]
#  [4 5 6 7]]
# ---
# [[ 8  9 10 11]
#  [12 13 14 15]]

# Example 4: Splitting 2D array along `axis=1` (column-wise)
split_cols = np.split(arr_split_2d, [1, 3], axis=1) # Split before col 1, and before col 3
print(f"Split into column sections at indices [1, 3]:")
for i, part in enumerate(split_cols):
    print(f"Part {i}:\n{part}")
# Output:
# Part 0:
# [[ 0]
#  [ 4]
#  [ 8]
#  [12]]
# Part 1:
# [[ 1  2]
#  [ 5  6]
#  [ 9 10]
#  [13 14]]
# Part 2:
# [[ 3]
#  [ 7]
#  [11]
#  [15]]

# Error: Uneven division for integer sections
try:
    np.split(arr_split_1d, 3) # 10 elements cannot be split into 3 equal sections
except ValueError as e:
    print(f"\nCaught expected error for uneven split: {e}")


# 2.2 `np.hsplit()`: Horizontal Split (Column-wise)
print("\n--- 2.2 `np.hsplit()`: Horizontal Split (Column-wise) ---")
print("`hsplit()` splits an array into multiple sub-arrays horizontally (column-wise).")
print("It's equivalent to `np.split(..., axis=1)`.")

hsplit_arr = np.arange(20).reshape(4, 5)
print(f"\nOriginal array for hsplit:\n{hsplit_arr}")
hsplit_result = np.hsplit(hsplit_arr, [1, 3]) # Split before col 1, and before col 3
print(f"hsplit into sections [1, 3]:")
for i, part in enumerate(hsplit_result):
    print(f"Part {i}:\n{part}")


# 2.3 `np.vsplit()`: Vertical Split (Row-wise)
print("\n--- 2.3 `np.vsplit()`: Vertical Split (Row-wise) ---")
print("`vsplit()` splits an array into multiple sub-arrays vertically (row-wise).")
print("It's equivalent to `np.split(..., axis=0)`.")

vsplit_arr = np.arange(16).reshape(4, 4)
print(f"\nOriginal array for vsplit:\n{vsplit_arr}")
vsplit_result = np.vsplit(vsplit_arr, 2) # Split into 2 equal sections
print(f"vsplit into 2 sections:\n{vsplit_result[0]}\n---\n{vsplit_result[1]}")


# 2.4 `np.dsplit()`: Depth Split (Depth-wise)
print("\n--- 2.4 `np.dsplit()`: Depth Split (Depth-wise) ---")
print("`dsplit()` splits an array into multiple sub-arrays along the third axis (depth-wise).")
print("It's equivalent to `np.split(..., axis=2)`.")

dsplit_arr = np.arange(2 * 3 * 4).reshape(2, 3, 4) # A 2x3x4 3D array
print(f"\nOriginal 3D array for dsplit (first page):\n{dsplit_arr[0]}")
dsplit_result = np.dsplit(dsplit_arr, 2) # Split into 2 equal sections along depth axis
print(f"dsplit into 2 sections (shape of first section: {dsplit_result[0].shape}):")
print(f"First section (first page):\n{dsplit_result[0][0]}\n---")
print(f"Second section (first page):\n{dsplit_result[1][0]}")
# Notice the last dimension of the split parts is now 2 (original 4 divided by 2)


print("\n--- End of NumPy Array Concatenation and Splitting Practice Code ---")