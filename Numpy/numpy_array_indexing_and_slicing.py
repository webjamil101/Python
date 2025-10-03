import numpy as np

print("--- NumPy Array Indexing and Slicing: Practice Code ---")

# --- 1. Introduction to Indexing and Slicing ---
print("\n--- 1. Introduction to Indexing and Slicing ---")
print("NumPy arrays support powerful and flexible ways to access subsets of data.")
print(" - **Indexing:** Accessing individual elements or specific elements using their positions.")
print(" - **Slicing:** Accessing contiguous blocks of elements using start:stop:step notation.")
print(" - **Fancy Indexing:** Accessing non-contiguous elements using an array of indices.")
print(" - **Boolean Indexing:** Accessing elements based on a boolean condition.")


# --- 2. 1D Array Indexing and Slicing ---
print("\n--- 2. 1D Array Indexing and Slicing ---")
arr_1d = np.arange(10, 101, 10) # Creates [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(f"Original 1D array: {arr_1d}")

# 2.1 Basic Indexing (Accessing single elements)
print(f"Element at index 0: {arr_1d[0]}")      # 10
print(f"Element at index 5: {arr_1d[5]}")      # 60
print(f"Element at last index (negative): {arr_1d[-1]}") # 100
print(f"Element at second to last index: {arr_1d[-2]}") # 90

# 2.2 Slicing (Accessing ranges of elements)
# Syntax: `[start:stop:step]`
# - `start`: inclusive index (default 0)
# - `stop`: exclusive index (default end of array)
# - `step`: increment (default 1)

print(f"Elements from index 2 up to (but not including) 7: {arr_1d[2:7]}") # [30 40 50 60 70]
print(f"Elements from index 5 to end: {arr_1d[5:]}")     # [60 70 80 90 100]
print(f"Elements from beginning to index 4 (exclusive): {arr_1d[:4]}")   # [10 20 30 40]
print(f"All elements (full slice): {arr_1d[:]}")      # [10 20 30 40 50 60 70 80 90 100]
print(f"Every 2nd element: {arr_1d[::2]}")     # [10 30 50 70 90]
print(f"Elements from index 1, every 3rd element: {arr_1d[1::3]}") # [20 50 80]
print(f"Reverse the array: {arr_1d[::-1]}")    # [100 90 80 70 60 50 40 30 20 10]


# --- 3. 2D Array Indexing and Slicing ---
print("\n--- 3. 2D Array Indexing and Slicing ---")
arr_2d = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
print(f"Original 2D array:\n{arr_2d}")

# 3.1 Basic Indexing (Accessing single elements)
# Syntax: `[row_index, col_index]`
print(f"Element at row 0, column 0: {arr_2d[0, 0]}") # 1
print(f"Element at row 2, column 3: {arr_2d[2, 3]}") # 12
print(f"Element at last row, last column: {arr_2d[-1, -1]}") # 16

# 3.2 Slicing Rows and Columns
# Syntax: `[row_slice, col_slice]`
print(f"First row: {arr_2d[0, :]}")          # [1 2 3 4]
print(f"Last column: {arr_2d[:, -1]}")       # [4 8 12 16] (as 1D array)
print(f"Rows 1 and 2 (indices 1, 2): {arr_2d[1:3, :]}") # Rows 1 and 2, all columns
# Output:
# [[ 5  6  7  8]
#  [ 9 10 11 12]]

print(f"Columns 1 and 2 (indices 1, 2):\n{arr_2d[:, 1:3]}") # All rows, columns 1 and 2
# Output:
# [[ 2  3]
#  [ 6  7]
#  [10 11]
#  [14 15]]

# 3.3 Combined Slicing (Sub-arrays)
print(f"Sub-array from rows 0-1, columns 2-3:\n{arr_2d[0:2, 2:4]}")
# Output:
# [[ 3  4]
#  [ 7  8]]

print(f"Every other row, every other column:\n{arr_2d[::2, ::2]}")
# Output:
# [[ 1  3]
#  [ 9 11]]


# --- 4. 3D Array Indexing and Slicing ---
print("\n--- 4. 3D Array Indexing and Slicing ---")
arr_3d = np.arange(1, 28).reshape(3, 3, 3) # 3 "pages", 3 rows, 3 columns
print(f"Original 3D array (first 'page'):\n{arr_3d[0]}")

# Syntax: `[page_index, row_index, col_index]`
print(f"Element at page 0, row 1, col 2: {arr_3d[0, 1, 2]}") # 6
print(f"Second 'page' (index 1):\n{arr_3d[1, :, :]}") # All rows/cols of page 1
# Output:
# [[10 11 12]
#  [13 14 15]
#  [16 17 18]]

print(f"All 'pages', row 0, all columns:\n{arr_3d[:, 0, :]}") # All pages, first row, all cols
# Output:
# [[ 1  2  3]
#  [10 11 12]
#  [19 20 21]]

print(f"Slice from pages 0-1, rows 1-2, columns 0-1:\n{arr_3d[0:2, 1:3, 0:2]}")
# Output (a 2x2x2 array):
# [[[ 4  5]
#   [ 7  8]]
#
#  [[13 14]
#   [16 17]]]


# --- 5. Fancy Indexing ---
print("\n--- 5. Fancy Indexing ---")
print("Fancy indexing allows you to pass an array (or list) of indices to select non-contiguous elements.")

# 5.1 1D Fancy Indexing
arr_fancy_1d = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
print(f"\nOriginal 1D array for fancy indexing: {arr_fancy_1d}")
indices_to_select = [0, 3, 5]
print(f"Elements at indices {indices_to_select}: {arr_fancy_1d[indices_to_select]}") # ['A' 'D' 'F']

# Can specify order and repetition
reordered_indices = [4, 1, 4, 0]
print(f"Elements with reordered/repeated indices {reordered_indices}: {arr_fancy_1d[reordered_indices]}") # ['E' 'B' 'E' 'A']

# 5.2 2D Fancy Indexing (Row selection)
arr_fancy_2d_rows = np.arange(1, 17).reshape(4, 4)
print(f"\nOriginal 2D array for fancy row indexing:\n{arr_fancy_2d_rows}")
rows_to_select = [0, 3, 1]
print(f"Selected rows {rows_to_select}:\n{arr_fancy_2d_rows[rows_to_select]}")
# Output:
# [[ 1  2  3  4]
#  [13 14 15 16]
#  [ 5  6  7  8]]

# 5.3 2D Fancy Indexing (Specific element selection)
# When you provide arrays for both row and column indices,
# they are paired element-wise: (row[0], col[0]), (row[1], col[1]), etc.
rows = np.array([0, 1, 2])
cols = np.array([0, 2, 1])
print(f"Elements at (0,0), (1,2), (2,1): {arr_fancy_2d_rows[rows, cols]}") # [1 7 10]


# --- 6. Boolean Indexing ---
print("\n--- 6. Boolean Indexing ---")
print("Boolean indexing allows you to select elements based on a condition.")
print("You provide a boolean array of the same shape, where True selects the corresponding element.")

arr_bool = np.array([10, 5, 20, 15, 25, 8, 30])
print(f"\nOriginal array for boolean indexing: {arr_bool}")

# 6.1 Selecting elements based on a condition
condition = arr_bool > 15
print(f"Boolean mask (arr_bool > 15): {condition}") # [False False  True  False  True False  True]
print(f"Elements greater than 15: {arr_bool[condition]}") # [20 25 30]

# Combine conditions
combined_condition = (arr_bool > 10) & (arr_bool < 30) # Use & for AND, | for OR
print(f"Elements > 10 AND < 30: {arr_bool[combined_condition]}") # [20 15 25]

# 6.2 Boolean Indexing in 2D
arr_bool_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(f"\nOriginal 2D array for boolean indexing:\n{arr_bool_2d}")
condition_2d = arr_bool_2d % 2 == 0 # Select even numbers
print(f"Boolean mask (even numbers):\n{condition_2d}")
print(f"Even numbers in the array: {arr_bool_2d[condition_2d]}") # Returns a 1D array of selected elements


# 6.3 Modifying elements using Boolean Indexing
arr_modify = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"\nArray before modification: {arr_modify}")
arr_modify[arr_modify % 2 == 0] = -1 # Set all even numbers to -1
print(f"Array after setting even numbers to -1: {arr_modify}") # [ 1 -1  3 -1  5 -1  7 -1  9 -1]


# --- 7. Views vs. Copies ---
print("\n--- 7. Views vs. Copies ---")
print("Important: Basic slicing often creates a 'view' into the original array's data, not a new copy.")
print("Changes to the view *will* affect the original array.")
print("Fancy indexing and boolean indexing always create *copies*.")

original_arr = np.array([10, 20, 30, 40, 50])
print(f"\nOriginal array: {original_arr}")

# 7.1 Slicing (View)
sliced_view = original_arr[1:4] # Elements [20 30 40]
print(f"Sliced view: {sliced_view}")
sliced_view[0] = 99 # Modify an element in the view
print(f"Sliced view after modification: {sliced_view}") # [99 30 40]
print(f"Original array after view modification: {original_arr}") # [10 99 30 40 50] (Original was modified!)

# 7.2 Fancy Indexing (Copy)
original_arr = np.array([10, 20, 30, 40, 50]) # Reset original array
fancy_copy = original_arr[[0, 2, 4]] # Elements [10 30 50]
print(f"\nOriginal array (reset): {original_arr}")
print(f"Fancy indexed copy: {fancy_copy}")
fancy_copy[0] = 99 # Modify an element in the copy
print(f"Fancy indexed copy after modification: {fancy_copy}") # [99 30 50]
print(f"Original array after fancy copy modification: {original_arr}") # [10 20 30 40 50] (Original NOT modified!)

# 7.3 To explicitly create a copy from a slice (if needed)
explicit_copy = original_arr[1:4].copy()
print(f"\nExplicit copy from slice: {explicit_copy}")
explicit_copy[0] = 88
print(f"Explicit copy after modification: {explicit_copy}")
print(f"Original array after explicit copy modification: {original_arr}") # Original NOT modified!


print("\n--- End of NumPy Array Indexing and Slicing Practice Code ---")