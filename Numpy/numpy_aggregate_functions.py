import numpy as np

print("--- NumPy Aggregate Functions: Practice Code ---")

# --- 1. What are Aggregate Functions? ---
print("\n--- 1. What are Aggregate Functions? ---")
print("Aggregate functions (or reduction operations) compute a single value from an array (or along a specific axis).")
print("They are essential for summarizing data.")
print("Examples: sum, mean, median, min, max, standard deviation, variance.")

# Let's create an example array
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"\nOriginal 1D data: {data}")

# --- 2. Common Aggregation Functions (1D Array) ---

# 2.1 `np.sum()`: Sum of all elements
print(f"\n--- 2.1 `np.sum()`: Sum ---")
print(f"Sum of all elements: {np.sum(data)}") # Output: 55

# 2.2 `np.min()` and `np.max()`: Minimum and Maximum
print(f"\n--- 2.2 `np.min()` and `np.max()`: Min & Max ---")
print(f"Minimum element: {np.min(data)}") # Output: 1
print(f"Maximum element: {np.max(data)}") # Output: 10

# Corresponding methods on the array object itself
print(f"data.min(): {data.min()}")
print(f"data.max(): {data.max()}")


# 2.3 `np.mean()`: Arithmetic Mean (Average)
print(f"\n--- 2.3 `np.mean()`: Mean (Average) ---")
print(f"Mean of elements: {np.mean(data)}") # Output: 5.5 (55 / 10)

# 2.4 `np.std()`: Standard Deviation
print(f"\n--- 2.4 `np.std()`: Standard Deviation ---")
print(f"Standard deviation of elements: {np.std(data):.2f}") # Output: 2.87

# 2.5 `np.var()`: Variance
print(f"\n--- 2.5 `np.var()`: Variance ---")
print(f"Variance of elements: {np.var(data):.2f}") # Output: 8.25

# 2.6 `np.prod()`: Product of all elements
print(f"\n--- 2.6 `np.prod()`: Product ---")
print(f"Product of all elements: {np.prod(data)}") # Output: 3628800 (10!)

# 2.7 `np.median()`: Median
print(f"\n--- 2.7 `np.median()`: Median ---")
print(f"Median of elements: {np.median(data)}") # Output: 5.5

# 2.8 `np.percentile()`: Percentile
print(f"\n--- 2.8 `np.percentile()`: Percentile ---")
print(f"25th percentile: {np.percentile(data, 25)}") # Output: 3.25
print(f"75th percentile: {np.percentile(data, 75)}") # Output: 7.75


# --- 3. Aggregations with `axis` (Multi-dimensional Arrays) ---
print("\n--- 3. Aggregations with `axis` (Multi-dimensional Arrays) ---")
print("The `axis` argument is crucial for performing aggregations along specific dimensions.")
print(" - `axis=0`: Operate column-wise (aggregate rows), resulting in values for each column.")
print(" - `axis=1`: Operate row-wise (aggregate columns), resulting in values for each row.")
print(" - `axis=None` (default): Aggregate over all elements, returning a single scalar.")

# Create a 2D array
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(f"\nOriginal 2D matrix:\n{matrix}")

# 3.1 `np.sum()` with `axis`
print(f"\n--- `np.sum()` with `axis` ---")
print(f"Sum of all elements (axis=None): {np.sum(matrix)}") # Output: 45

print(f"Sum along axis=0 (column sums):\n{np.sum(matrix, axis=0)}") # Output: [12 15 18] (1+4+7, 2+5+8, 3+6+9)
print(f"Sum along axis=1 (row sums):\n{np.sum(matrix, axis=1)}") # Output: [ 6 15 24] (1+2+3, 4+5+6, 7+8+9)

# 3.2 `np.mean()` with `axis`
print(f"\n--- `np.mean()` with `axis` ---")
print(f"Mean along axis=0 (column means):\n{np.mean(matrix, axis=0)}") # Output: [4. 5. 6.]
print(f"Mean along axis=1 (row means):\n{np.mean(matrix, axis=1)}") # Output: [2. 5. 8.]

# 3.3 `np.min()`/`np.max()` with `axis`
print(f"\n--- `np.min()`/`np.max()` with `axis` ---")
print(f"Min along axis=0 (column mins): {np.min(matrix, axis=0)}") # [1 2 3]
print(f"Max along axis=1 (row maxs): {np.max(matrix, axis=1)}") # [3 6 9]

# 3.4 Higher dimensional arrays
arr_3d = np.arange(1, 28).reshape(3, 3, 3) # 3 "pages", 3 rows, 3 columns
print(f"\nOriginal 3D array (first page):\n{arr_3d[0]}")
print(f"Sum along axis=0 (summing across pages for each [row,col]):\n{np.sum(arr_3d, axis=0)}")
# The result will be a 3x3 array where each element is the sum of elements at that [row,col] across all 3 pages.
# e.g., result[0,0] = arr_3d[0,0,0] + arr_3d[1,0,0] + arr_3d[2,0,0] = 1 + 10 + 19 = 30

print(f"Mean along axis=2 (mean of elements in each column across pages):\n{np.mean(arr_3d, axis=2)}")
# Result will be a 3x3 array, each element is the mean of 3 elements from the 3rd dimension


# --- 4. Cumulative Aggregations (`cumsum`, `cumprod`) ---
print("\n--- 4. Cumulative Aggregations (`cumsum`, `cumprod`) ---")
print("These functions return an array of the same shape, where each element is the accumulated result up to that point.")

arr_cumulative = np.array([1, 2, 3, 4, 5])
print(f"\nOriginal array for cumulative operations: {arr_cumulative}")

# 4.1 `np.cumsum()`: Cumulative sum
print(f"Cumulative sum: {np.cumsum(arr_cumulative)}") # [ 1  3  6 10 15]

# 4.2 `np.cumprod()`: Cumulative product
print(f"Cumulative product: {np.cumprod(arr_cumulative)}") # [  1   2   6  24 120]

# Cumulative operations on 2D arrays with `axis`
matrix_cum = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\nOriginal 2D matrix for cumulative ops:\n{matrix_cum}")

print(f"Cumulative sum along axis=0 (column-wise):\n{np.cumsum(matrix_cum, axis=0)}")
# Output:
# [[1 2 3]
#  [5 7 9]] (1+4, 2+5, 3+6)

print(f"Cumulative sum along axis=1 (row-wise):\n{np.cumsum(matrix_cum, axis=1)}")
# Output:
# [[ 1  3  6] (1, 1+2, 1+2+3)
#  [ 4  9 15]] (4, 4+5, 4+5+6)


# --- 5. Handling Missing Values (`NaN`) in Aggregations ---
print("\n--- 5. Handling Missing Values (`NaN`) in Aggregations ---")
print("NumPy has special versions of aggregate functions that ignore `NaN` (Not a Number) values.")
data_with_nan = np.array([1, 2, np.nan, 4, 5])
print(f"\nData with NaN: {data_with_nan}")

print(f"np.sum(data_with_nan): {np.sum(data_with_nan)}") # Output: nan (default behavior is to propagate NaN)
print(f"np.nansum(data_with_nan): {np.nansum(data_with_nan)}") # Output: 12.0 (ignores NaN)

print(f"np.mean(data_with_nan): {np.mean(data_with_nan)}") # Output: nan
print(f"np.nanmean(data_with_nan): {np.nanmean(data_with_nan):.2f}") # Output: 3.00 (12 / 4)

print(f"np.min(data_with_nan): {np.min(data_with_nan)}") # Output: nan
print(f"np.nanmin(data_with_nan): {np.nanmin(data_with_nan)}") # Output: 1.0


# --- 6. `keepdims` Argument ---
print("\n--- 6. `keepdims` Argument ---")
print("`keepdims=True` prevents the aggregation from reducing the number of dimensions.")
print("The aggregated axis will remain as a dimension of size 1.")

arr_keepdims = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\nOriginal array: {arr_keepdims} (shape: {arr_keepdims.shape})")

sum_axis0 = np.sum(arr_keepdims, axis=0)
print(f"Sum along axis=0 (default): {sum_axis0} (shape: {sum_axis0.shape})") # [5 7 9] (shape: (3,))

sum_axis0_keepdims = np.sum(arr_keepdims, axis=0, keepdims=True)
print(f"Sum along axis=0 (keepdims=True): {sum_axis0_keepdims} (shape: {sum_axis0_keepdims.shape})") # [[5 7 9]] (shape: (1, 3))

sum_axis1_keepdims = np.sum(arr_keepdims, axis=1, keepdims=True)
print(f"Sum along axis=1 (keepdims=True):\n{sum_axis1_keepdims} (shape: {sum_axis1_keepdims.shape})")
# Output:
# [[ 6]
#  [15]] (shape: (2, 1))

# This is useful for maintaining compatibility for broadcasting in further operations.


print("\n--- End of NumPy Aggregate Functions Practice Code ---")