import numpy as np

print("--- NumPy Basic Operations: Practice Code ---")

# --- 1. Element-wise Arithmetic Operations ---
print("\n--- 1. Element-wise Arithmetic Operations ---")
print("NumPy operations between arrays (or between an array and a scalar) are performed element by element.")
print("This is called 'vectorization' and is significantly faster than explicit Python loops for large arrays.")

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])
scalar = 2

print(f"\nArray 1: {arr1}")
print(f"Array 2: {arr2}")
print(f"Scalar: {scalar}")

# 1.1 Addition
print(f"\nArray 1 + Array 2: {arr1 + arr2}")      # [11 22 33 44 55]
print(f"Array 1 + Scalar: {arr1 + scalar}")      # [ 3  4  5  6  7]

# 1.2 Subtraction
print(f"Array 2 - Array 1: {arr2 - arr1}")      # [ 9 18 27 36 45]
print(f"Array 1 - Scalar: {arr1 - scalar}")      # [-1  0  1  2  3]

# 1.3 Multiplication (Element-wise, not matrix multiplication)
print(f"Array 1 * Array 2: {arr1 * arr2}")      # [ 10  40  90 160 250]
print(f"Array 1 * Scalar: {arr1 * scalar}")      # [ 2  4  6  8 10]

# 1.4 Division
print(f"Array 2 / Array 1: {arr2 / arr1}")      # [10.  10.  10.  10.  10.]
print(f"Array 1 / Scalar: {arr1 / scalar}")      # [0.5 1.  1.5 2.  2.5]
print(f"Integer Division (floor division): {arr1 // scalar}") # [0 1 1 2 2]

# 1.5 Exponentiation
print(f"Array 1 ** 2: {arr1 ** 2}")          # [ 1  4  9 16 25]
print(f"Array 2 ** 0.5 (sqrt): {arr2 ** 0.5}") # [3.16 4.47 5.47 6.32 7.07]

# 1.6 Modulus (Remainder)
print(f"Array 2 % Array 1: {arr2 % arr1}")      # [0 0 0 0 0] (since all are multiples)
print(f"Array 1 % 2: {arr1 % 2}")          # [1 0 1 0 1]


# --- 2. Comparison Operations ---
print("\n--- 2. Comparison Operations ---")
print("Comparisons between arrays (or array and scalar) also happen element-wise and result in a boolean array.")

arr_comp1 = np.array([10, 20, 30, 40, 50])
arr_comp2 = np.array([10, 25, 20, 40, 55])

print(f"\nArray Comp 1: {arr_comp1}")
print(f"Array Comp 2: {arr_comp2}")

print(f"Arr1 == Arr2: {arr_comp1 == arr_comp2}") # [ True False False  True False]
print(f"Arr1 != Arr2: {arr_comp1 != arr_comp2}") # [False  True  True False  True]
print(f"Arr1 < Arr2: {arr_comp1 < arr_comp2}")  # [False  True False False  True]
print(f"Arr1 <= Arr2: {arr_comp1 <= arr_comp2}") # [ True  True False  True  True]
print(f"Arr1 > Arr2: {arr_comp1 > arr_comp2}")  # [False False  True False False]
print(f"Arr1 >= Arr2: {arr_comp1 >= arr_comp2}") # [ True False  True  True False]

# Comparison with a scalar
print(f"Arr1 > 30: {arr_comp1 > 30}")      # [False False False  True  True]


# --- 3. Logical Operations (for Boolean Arrays) ---
print("\n--- 3. Logical Operations (for Boolean Arrays) ---")
print("These are typically used on boolean arrays, often results of comparison operations.")
print("Use `&` for element-wise AND, `|` for element-wise OR, `~` for element-wise NOT.")

bool_arr1 = np.array([True, False, True, False])
bool_arr2 = np.array([True, True, False, False])

print(f"\nBoolean Array 1: {bool_arr1}")
print(f"Boolean Array 2: {bool_arr2}")

print(f"Bool1 & Bool2 (AND): {bool_arr1 & bool_arr2}") # [ True False False False]
print(f"Bool1 | Bool2 (OR): {bool_arr1 | bool_arr2}") # [ True  True  True False]
print(f"~Bool1 (NOT): {~bool_arr1}")              # [False  True False  True]

# Combining comparisons and logical operations
data = np.array([1, 8, 3, 10, 5, 12])
print(f"\nData for combined logic: {data}")
condition1 = data > 3   # [False  True False  True  True  True]
condition2 = data < 10  # [ True  True  True False  True False]

combined_cond = (data > 3) & (data < 10)
print(f"(data > 3) & (data < 10): {combined_cond}") # [False  True False False  True False]
print(f"Elements satisfying condition: {data[combined_cond]}") # [8 5]


# --- 4. Universal Functions (Ufuncs) ---
print("\n--- 4. Universal Functions (Ufuncs) ---")
print("Ufuncs are NumPy functions that operate element-wise on `ndarray`s.")
print("They are implemented in C and optimized for speed.")

ufunc_arr = np.array([-1.5, 0, 0.5, 2.7, 4.0])
print(f"\nArray for Ufuncs: {ufunc_arr}")

# 4.1 Mathematical Ufuncs
print(f"Absolute values (np.abs): {np.abs(ufunc_arr)}")       # [1.5 0.  0.5 2.7 4. ]
print(f"Square root (np.sqrt): {np.sqrt(np.array([4, 9, 16]))}") # [2. 3. 4.]
print(f"Exponential (np.exp): {np.exp(ufunc_arr)}")          # [0.22 1.   1.65 14.88 54.6 ]
print(f"Logarithm (np.log): {np.log(np.array([1, np.e, 10]))}") # [0. 1. 2.3] (e is math.e)
print(f"Sine (np.sin): {np.sin(ufunc_arr)}")              # [-0.99  0.    0.48  0.42  0.76]
print(f"Ceiling (np.ceil): {np.ceil(ufunc_arr)}")          # [-1.  0.  1.  3.  4.]
print(f"Floor (np.floor): {np.floor(ufunc_arr)}")          # [-2.  0.  0.  2.  4.]
print(f"Round (np.round): {np.round(ufunc_arr)}")          # [-2.  0.  1.  3.  4.] (rounds to nearest even for .5)
print(f"Is Finite (np.isfinite): {np.isfinite(ufunc_arr)}")  # [ True  True  True  True  True] (checks for inf, nan)

# 4.2 Ufuncs with multiple arguments (e.g., `add`, `maximum`)
arr_ufunc1 = np.array([1, 5, 2])
arr_ufunc2 = np.array([4, 2, 8])
print(f"\nUfunc Array 1: {arr_ufunc1}")
print(f"Ufunc Array 2: {arr_ufunc2}")
print(f"np.add(arr1, arr2): {np.add(arr_ufunc1, arr_ufunc2)}") # [ 5  7 10]
print(f"np.maximum(arr1, arr2): {np.maximum(arr_ufunc1, arr_ufunc2)}") # [4 5 8] (element-wise max)


# --- 5. Matrix Multiplication (Beyond Basic Element-wise) ---
print("\n--- 5. Matrix Multiplication ---")
print("While `*` performs element-wise multiplication, for proper matrix multiplication, use `@` operator or `np.dot()`.")

matrix_A = np.array([[1, 2], [3, 4]])
matrix_B = np.array([[5, 6], [7, 8]])
print(f"\nMatrix A:\n{matrix_A}")
print(f"Matrix B:\n{matrix_B}")

# Matrix multiplication using the @ operator (preferred for readability)
matrix_product_at = matrix_A @ matrix_B
print(f"Matrix A @ Matrix B:\n{matrix_product_at}")
# Output:
# [[1*5 + 2*7, 1*6 + 2*8],
#  [3*5 + 4*7, 3*6 + 4*8]]
# [[19 22]
#  [43 50]]

# Matrix multiplication using np.dot()
matrix_product_dot = np.dot(matrix_A, matrix_B)
print(f"np.dot(Matrix A, Matrix B):\n{matrix_product_dot}")

# Dot product of 1D arrays (scalar result)
vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])
dot_product_1d = np.dot(vec1, vec2)
print(f"Dot product of 1D arrays ({vec1} . {vec2}): {dot_product_1d}") # 1*4 + 2*5 + 3*6 = 4+10+18 = 32


print("\n--- End of NumPy Basic Operations Practice Code ---")