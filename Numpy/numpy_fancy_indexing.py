import numpy as np

print("--- NumPy Fancy Indexing: Practice Code ---")

# --- 1. What is Fancy Indexing? ---
print("\n--- 1. What is Fancy Indexing? ---")
print("Fancy indexing allows you to select elements from an array using another array (or list) of integer indices.")
print("Unlike slicing, fancy indexing allows you to select non-contiguous elements and even repeat elements.")
print("The result of fancy indexing is always a *copy* of the selected elements, not a view.")


# --- 2. 1D Array Fancy Indexing ---
print("\n--- 2. 1D Array Fancy Indexing ---")
arr_1d = np.array(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape'])
print(f"Original 1D array: {arr_1d}")

# 2.1 Selecting specific elements by position
indices_to_select = [0, 2, 5]
print(f"Elements at indices {indices_to_select}: {arr_1d[indices_to_select]}")
# Output: ['apple' 'cherry' 'fig']

# 2.2 Reordering elements
reorder_indices = [4, 1, 0, 3]
print(f"Elements reordered by indices {reorder_indices}: {arr_1d[reorder_indices]}")
# Output: ['elderberry' 'banana' 'apple' 'date']

# 2.3 Repeating elements
repeat_indices = [2, 2, 0, 5, 0]
print(f"Elements repeated by indices {repeat_indices}: {arr_1d[repeat_indices]}")
# Output: ['cherry' 'cherry' 'apple' 'fig' 'apple']

# 2.4 Using a NumPy array of indices
np_indices = np.array([6, 1])
print(f"Elements using NumPy array of indices {np_indices}: {arr_1d[np_indices]}")
# Output: ['grape' 'banana']


# --- 3. 2D Array Fancy Indexing ---
print("\n--- 3. 2D Array Fancy Indexing ---")
arr_2d = np.arange(10, 50, 5).reshape(4, 2) # Create a 4x2 array
# [[10 15]
#  [20 25]
#  [30 35]
#  [40 45]]
print(f"Original 2D array:\n{arr_2d}")

# 3.1 Selecting specific rows
row_indices = [0, 3, 1]
print(f"Selected rows {row_indices}:\n{arr_2d[row_indices]}")
# Output:
# [[10 15]
#  [40 45]
#  [20 25]]

# 3.2 Selecting specific columns (using a simple slice for rows)
col_indices = [1, 0]
print(f"Selected columns {col_indices}:\n{arr_2d[:, col_indices]}")
# Output:
# [[15 10]
#  [25 20]
#  [35 30]
#  [45 40]]

# 3.3 Selecting specific elements using paired (row, column) indices
# This is where it gets 'fancy' for 2D. You provide two 1D arrays of indices.
# The elements at (row_indices[i], col_indices[i]) are selected.
print("\n--- Paired (Row, Column) Indexing ---")
rows = np.array([0, 1, 3])
cols = np.array([0, 1, 0]) # Selects (0,0), (1,1), (3,0)
print(f"Selecting elements at (row_indices, col_indices):")
print(f"  Rows: {rows}")
print(f"  Cols: {cols}")
print(f"Result: {arr_2d[rows, cols]}")
# Output: [10 25 40]

# Example with repeated indices
rows_repeated = np.array([1, 1, 3])
cols_repeated = np.array([0, 0, 1])
print(f"Selecting elements with repeated (row, col) pairs:")
print(f"  Rows: {rows_repeated}")
print(f"  Cols: {cols_repeated}")
print(f"Result: {arr_2d[rows_repeated, cols_repeated]}")
# Output: [20 20 45]


# --- 4. Combining Fancy Indexing with Slicing ---
print("\n--- 4. Combining Fancy Indexing with Slicing ---")
arr_combined = np.arange(100, 116).reshape(4, 4)
# [[100 101 102 103]
#  [104 105 106 107]
#  [108 109 110 111]
#  [112 113 114 115]]
print(f"Original array:\n{arr_combined}")

# Select specific rows, but only a slice of their columns
selected_rows = [0, 2] # Select rows 0 and 2
sliced_cols = slice(1, 3) # Select columns 1 and 2 (inclusive of 1, exclusive of 3)
print(f"Rows {selected_rows}, columns {sliced_cols}:\n{arr_combined[selected_rows, sliced_cols]}")
# Output:
# [[101 102]
#  [109 110]]

# Select all rows, but specific columns using fancy indexing
all_rows = slice(None) # Equivalent to :
specific_cols = [0, 3] # Select column 0 and column 3
print(f"All rows, columns {specific_cols}:\n{arr_combined[all_rows, specific_cols]}")
# Output:
# [[100 103]
#  [104 107]
#  [108 111]
#  [112 115]]

# This can also be written as:
print(f"All rows, columns {specific_cols} (shorthand):\n{arr_combined[:, specific_cols]}")


# --- 5. Modifying Elements Using Fancy Indexing ---
print("\n--- 5. Modifying Elements Using Fancy Indexing ---")
mod_arr = np.array([10, 20, 30, 40, 50])
print(f"Array before modification: {mod_arr}")

indices_to_modify = [0, 2, 4]
mod_arr[indices_to_modify] = 99
print(f"Array after setting elements at {indices_to_modify} to 99: {mod_arr}")
# Output: [99 20 99 40 99]

# Note: If duplicate indices are present on the left-hand side, the assignment is performed multiple times,
# but the final value will be the last assignment in the index list.
mod_arr = np.array([10, 20, 30])
print(f"\nArray before modification: {mod_arr}")
indices_with_duplicates = [0, 0, 1]
values_to_assign = [100, 200, 300]
mod_arr[indices_with_duplicates] = values_to_assign
print(f"Array after duplicate assignment: {mod_arr}")
# Output: [200 300  30] (Index 0 got 100 then 200, so 200 is final)


# --- 6. Boolean vs. Fancy Indexing ---
print("\n--- 6. Boolean vs. Fancy Indexing ---")
print("While they both select subsets, their mechanisms and use cases differ:")
print(" - **Boolean Indexing:** Selects elements based on a *True/False* condition across the array.")
print("   `arr[arr > 5]` (selects all elements where condition is true)")
print(" - **Fancy Indexing:** Selects elements based on explicit *integer positions* you provide.")
print("   `arr[[0, 3, 5]]` (selects elements at positions 0, 3, and 5)")

data_comparison = np.array([1, 8, 3, 10, 5, 12, 7])
print(f"\nData for comparison: {data_comparison}")

# Boolean Indexing example
boolean_result = data_comparison[data_comparison > 7]
print(f"Boolean Indexing (elements > 7): {boolean_result}") # [ 8 10 12]

# Fancy Indexing example (to get similar values if possible)
# Note: You'd need to know the indices first to use fancy indexing for this.
indices_of_large_values = np.where(data_comparison > 7)[0]
fancy_result = data_comparison[indices_of_large_values]
print(f"Fancy Indexing (elements at indices {indices_of_large_values}): {fancy_result}") # [ 8 10 12]


print("\n--- End of NumPy Fancy Indexing Practice Code ---")