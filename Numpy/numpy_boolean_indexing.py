import numpy as np

print("--- NumPy Boolean Indexing: Practice Code ---")

# --- 1. What is Boolean Indexing? ---
print("\n--- 1. What is Boolean Indexing? ---")
print("Boolean indexing involves using a boolean array (an array of True/False values) to select elements from another array.")
print("The boolean array must have the same shape or be broadcastable to the array being indexed.")
print("Wherever the boolean array has `True`, the corresponding element from the original array is selected.")
print("The result of boolean indexing is always a *copy* of the selected elements, returned as a 1D array.")


# --- 2. Basic Boolean Indexing (1D Array) ---
print("\n--- 2. Basic Boolean Indexing (1D Array) ---")
data_1d = np.array([10, 5, 20, 15, 25, 8, 30, 12, 18])
print(f"Original 1D array: {data_1d}")

# 2.1 Creating a Boolean Mask (Condition)
# This creates a boolean array of the same shape as `data_1d`
mask_greater_than_15 = data_1d > 15
print(f"Boolean mask (elements > 15): {mask_greater_than_15}")
# Output: [False False  True False  True False  True False  True]

# 2.2 Applying the Boolean Mask
selected_elements = data_1d[mask_greater_than_15]
print(f"Elements greater than 15: {selected_elements}")
# Output: [20 25 30 18] (This is a 1D array of the selected elements)

# Direct application of condition (no need for a separate mask variable)
selected_less_than_10 = data_1d[data_1d < 10]
print(f"Elements less than 10: {selected_less_than_10}")
# Output: [5 8]

selected_equal_20 = data_1d[data_1d == 20]
print(f"Elements equal to 20: {selected_equal_20}")
# Output: [20]


# --- 3. Boolean Indexing with Multiple Conditions ---
print("\n--- 3. Boolean Indexing with Multiple Conditions ---")
print("When combining conditions, use logical operators `&` (AND), `|` (OR), `~` (NOT).")
print("Remember to use parentheses around each condition because of operator precedence.")

# Condition 1: greater than 10
cond1 = data_1d > 10
# Condition 2: less than 25
cond2 = data_1d < 25

# 3.1 AND (`&`) operation
combined_and = data_1d[(data_1d > 10) & (data_1d < 25)]
print(f"Elements > 10 AND < 25: {combined_and}")
# Output: [20 15 18 12]

# 3.2 OR (`|`) operation
combined_or = data_1d[(data_1d < 10) | (data_1d > 20)]
print(f"Elements < 10 OR > 20: {combined_or}")
# Output: [ 5 25  8 30]

# 3.3 NOT (`~`) operation
not_between_10_and_20 = data_1d[~((data_1d >= 10) & (data_1d <= 20))]
print(f"Elements NOT between 10 and 20 (inclusive): {not_between_10_and_20}")
# Output: [ 5 25  8 30]


# --- 4. Boolean Indexing in Higher Dimensions (2D, 3D Arrays) ---
print("\n--- 4. Boolean Indexing in Higher Dimensions ---")
data_2d = np.array([
    [10, 20, 30],
    [40, 5, 60],
    [70, 15, 90]
])
print(f"Original 2D array:\n{data_2d}")

# 4.1 Applying a simple condition to a 2D array
mask_2d_greater_than_35 = data_2d > 35
print(f"Boolean mask (elements > 35):\n{mask_2d_greater_than_35}")
# Output:
# [[False False False]
#  [ True False  True]
#  [ True False  True]]

selected_elements_2d = data_2d[mask_2d_greater_than_35]
print(f"Elements > 35 (returned as 1D array): {selected_elements_2d}")
# Output: [40 60 70 90]

# 4.2 Using conditions to select rows or columns (sometimes a simpler slice is better)
# To select rows where any element meets a condition:
rows_with_large_value = data_2d[np.any(data_2d > 60, axis=1)]
print(f"Rows with at least one element > 60:\n{rows_with_large_value}")
# Output:
# [[70 15 90]]

# To select columns where all elements meet a condition:
cols_all_above_0 = data_2d[:, np.all(data_2d > 0, axis=0)]
print(f"Columns where all elements > 0 (example):\n{cols_all_above_0}")


# --- 5. Modifying Elements Using Boolean Indexing ---
print("\n--- 5. Modifying Elements Using Boolean Indexing ---")
mod_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"Array before modification: {mod_array}")

# Set all even numbers to 0
mod_array[mod_array % 2 == 0] = 0
print(f"Array after setting even numbers to 0: {mod_array}")
# Output: [1 0 3 0 5 0 7 0 9 0]

# Set elements greater than 5 to their negative value
mod_array[mod_array > 5] = -mod_array[mod_array > 5]
print(f"Array after setting elements > 5 to their negative: {mod_array}")
# Output: [ 1  0  3  0  5  0 -7  0 -9  0]


# --- 6. `isin()` and `in1d()` for Membership Testing ---
print("\n--- 6. `isin()` for Membership Testing ---")
print("`np.isin(element, test_elements)` checks if each element in `element` is present in `test_elements`.")

main_array = np.array([10, 20, 30, 40, 50, 10, 60, 20])
values_to_check = [10, 40, 70]
print(f"Main array: {main_array}")
print(f"Values to check for: {values_to_check}")

mask_isin = np.isin(main_array, values_to_check)
print(f"Boolean mask (isin {values_to_check}): {mask_isin}")
# Output: [ True False False  True False  True False False]

selected_isin = main_array[mask_isin]
print(f"Elements present in {values_to_check}: {selected_isin}")
# Output: [10 40 10]

# Note: `np.in1d()` is an older, 1D-specific version of `np.isin()`. `np.isin()` is generally preferred.


# --- 7. Boolean Indexing with `where()` (Conditional Element Selection/Replacement) ---
print("\n--- 7. `np.where()` for Conditional Selection/Replacement ---")
print("`np.where(condition, x, y)` returns elements chosen from `x` or `y` depending on `condition`.")
print("If `condition` is True, it takes from `x`; if False, it takes from `y`.")

scores = np.array([85, 92, 78, 65, 95, 50, 88])
print(f"Scores: {scores}")

# If score > 80, assign 'Pass', else 'Fail'
results = np.where(scores > 80, 'Pass', 'Fail')
print(f"Pass/Fail results: {results}")
# Output: ['Pass' 'Pass' 'Fail' 'Fail' 'Pass' 'Fail' 'Pass']

# Replace values based on condition (similar to direct boolean assignment but returns new array)
modified_scores = np.where(scores < 70, 0, scores)
print(f"Scores where < 70 replaced with 0: {modified_scores}")
# Output: [85 92 78  0 95  0 88]


print("\n--- End of NumPy Boolean Indexing Practice Code ---")