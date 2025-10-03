import numpy as np
import timeit # For benchmarking performance

print("--- NumPy Universal Functions (Ufuncs): Practice Code ---")

# --- 1. What are Universal Functions (Ufuncs)? ---
print("\n--- 1. What are Universal Functions (Ufuncs)? ---")
print("Ufuncs are NumPy functions that perform element-wise operations on `ndarray` objects.")
print("Key characteristics:")
print(" - **Vectorized:** They operate on entire arrays, not element by element in Python loops.")
print(" - **Fast:** Implemented in compiled C code (highly optimized).")
print(" - **Flexible:** Support broadcasting, handling arrays of different but compatible shapes.")
print(" - **Output Array:** Can often specify where the result should be stored (e.g., using `out` argument).")

# Comparison: Ufunc vs. Python loop
size = 1_000_000
arr_ufunc_test = np.random.rand(size)
py_list_test = arr_ufunc_test.tolist()

print(f"\nBenchmarking square root calculation on {size} elements:")

# Using NumPy Ufunc (np.sqrt)
numpy_time = timeit.timeit("np.sqrt(arr_ufunc_test)", globals=globals(), number=10)
print(f"NumPy np.sqrt time: {numpy_time:.6f} seconds")

# Using Python math.sqrt with a list comprehension
python_time = timeit.timeit("[math.sqrt(x) for x in py_list_test]", setup="import math", globals=globals(), number=10)
print(f"Python loop time: {python_time:.6f} seconds")

print(f"NumPy is approximately {python_time / numpy_time:.1f}x faster for this operation.")


# --- 2. Common Mathematical Ufuncs ---
print("\n--- 2. Common Mathematical Ufuncs ---")
arr_math = np.array([-2.5, -1, 0, 0.5, 1, 2.7, 4.0])
print(f"\nArray for Mathematical Ufuncs: {arr_math}")

# 2.1 Absolute Value
print(f"np.abs(): {np.abs(arr_math)}")         # [2.5 1.  0.  0.5 1.  2.7 4. ]

# 2.2 Trigonometric Functions
print(f"np.sin(): {np.sin(arr_math)}")         # Sine of each element
print(f"np.cos(): {np.cos(arr_math)}")         # Cosine of each element
print(f"np.tan(): {np.tan(arr_math)}")         # Tangent of each element

# 2.3 Exponential and Logarithmic Functions
print(f"np.exp(): {np.exp(arr_math)}")         # e^x for each element
print(f"np.log(): {np.log(np.array([1, 2.718, 10]))}") # Natural logarithm (ln)
print(f"np.log10(): {np.log10(np.array([10, 100, 1000]))}") # Base 10 logarithm
print(f"np.log2(): {np.log2(np.array([2, 4, 8]))}")     # Base 2 logarithm

# 2.4 Power and Square Root
print(f"np.sqrt(): {np.sqrt(np.array([4, 9, 16]))}") # Square root
print(f"np.power(arr, exponent): {np.power(arr_math, 2)}") # arr**exponent (e.g., square)
print(f"np.power(base, arr): {np.power(2, arr_math)}") # base**arr (e.g., 2 to the power of each element)

# 2.5 Rounding and Truncation
print(f"np.round(): {np.round(arr_math)}")     # Round to nearest integer (ties to nearest even)
print(f"np.floor(): {np.floor(arr_math)}")     # Round down
print(f"np.ceil(): {np.ceil(arr_math)}")       # Round up
print(f"np.trunc(): {np.trunc(arr_math)}")     # Truncate towards zero (remove decimal part)


# --- 3. Comparison Ufuncs ---
print("\n--- 3. Comparison Ufuncs ---")
arr_comp1 = np.array([1, 5, 2, 8])
arr_comp2 = np.array([4, 2, 8, 3])
print(f"\nArray Comp 1: {arr_comp1}")
print(f"Array Comp 2: {arr_comp2}")

# These also act element-wise and return boolean arrays
print(f"np.equal(): {np.equal(arr_comp1, arr_comp2)}")     # [False False False False]
print(f"np.greater(): {np.greater(arr_comp1, arr_comp2)}")   # [False  True False  True]
print(f"np.less_equal(): {np.less_equal(arr_comp1, arr_comp2)}") # [ True False  True False]

# 3.1 `np.maximum()` and `np.minimum()`
print(f"np.maximum(arr_comp1, arr_comp2): {np.maximum(arr_comp1, arr_comp2)}") # [4 5 8 8] (element-wise max)
print(f"np.minimum(arr_comp1, arr_comp2): {np.minimum(arr_comp1, arr_comp2)}") # [1 2 2 3] (element-wise min)


# --- 4. Bit-wise Ufuncs (for Integer Arrays) ---
print("\n--- 4. Bit-wise Ufuncs ---")
arr_bit1 = np.array([5, 6, 7], dtype=np.uint8)  # 5: 0101, 6: 0110, 7: 0111
arr_bit2 = np.array([3, 4, 1], dtype=np.uint8)  # 3: 0011, 4: 0100, 1: 0001
print(f"\nArray Bit 1: {arr_bit1}")
print(f"Array Bit 2: {arr_bit2}")

print(f"np.bitwise_and(): {np.bitwise_and(arr_bit1, arr_bit2)}") # 5&3=1 (0001), 6&4=4 (0100), 7&1=1 (0001)
print(f"np.bitwise_or(): {np.bitwise_or(arr_bit1, arr_bit2)}")   # 5|3=7 (0111), 6|4=6 (0110), 7|1=7 (0111)
print(f"np.bitwise_xor(): {np.bitwise_xor(arr_bit1, arr_bit2)}") # 5^3=6 (0110), 6^4=2 (0010), 7^1=6 (0110)
print(f"np.invert(): {np.invert(arr_bit1)}") # Inverts bits (e.g., ~5 = -6 for signed, 250 for uint8)


# --- 5. Type Casting and Output Argument (`out`) ---
print("\n--- 5. Type Casting and Output Argument (`out`) ---")

# 5.1 Type Casting
# Ufuncs typically return results in a common type, or the most precise input type.
arr_float = np.array([1.1, 2.7])
arr_int = np.array([1, 2])
print(f"\nfloat array: {arr_float.dtype}, int array: {arr_int.dtype}")
sum_result = np.add(arr_float, arr_int)
print(f"Result of float + int: {sum_result} (dtype: {sum_result.dtype})") # float64 (promotes to higher precision)

# You can specify `dtype` for the output
sum_result_float32 = np.add(arr_float, arr_int, dtype=np.float32)
print(f"Result of float + int (dtype=float32): {sum_result_float32} (dtype: {sum_result_float32.dtype})")


# 5.2 `out` argument
# Instead of creating a new array, you can specify an existing array to store the result.
# This can be useful for memory optimization in long-running computations.
output_array = np.zeros_like(arr_math) # Create an array of zeros with same shape and dtype
print(f"\nInitial output_array: {output_array}")
np.sqrt(np.abs(arr_math), out=output_array) # Calculate sqrt(abs(arr_math)) and store in output_array
print(f"output_array after np.sqrt (using 'out'): {output_array}")


# --- 6. Broadcasting with Ufuncs ---
print("\n--- 6. Broadcasting with Ufuncs ---")
print("Ufuncs automatically apply broadcasting rules when operating on arrays of different shapes.")

mat_A = np.array([[1, 2, 3], [4, 5, 6]]) # Shape (2, 3)
vec_B = np.array([10, 20, 30])           # Shape (3,)
scalar_C = 5                             # Shape ()

print(f"\nMatrix A:\n{mat_A} (shape: {mat_A.shape})")
print(f"Vector B: {vec_B} (shape: {vec_B.shape})")
print(f"Scalar C: {scalar_C} (shape: {scalar_C.shape})")

print(f"\nnp.add(mat_A, scalar_C):\n{np.add(mat_A, scalar_C)}") # Scalar broadcasting
print(f"np.multiply(mat_A, vec_B):\n{np.multiply(mat_A, vec_B)}") # Row broadcasting

# An example where broadcasting would fail
try:
    vec_D = np.array([100, 200]) # Shape (2,)
    print(f"\nAttempting np.add(mat_A, vec_D) (expect error):")
    np.add(mat_A, vec_D)
except ValueError as e:
    print(f"Caught expected error: {e}") # Shapes (2,3) and (2,) are not broadcast compatible


# --- 7. Aggregation Methods of Ufuncs (`reduce`, `accumulate`, `outer`) ---
print("\n--- 7. Aggregation Methods of Ufuncs ---")
print("Ufuncs also have methods for performing reductions and other operations.")

reduce_arr = np.array([1, 2, 3, 4, 5])

# 7.1 `reduce()`: Applies the ufunc repeatedly along an axis, reducing the array to a single value.
print(f"\nReduce array: {reduce_arr}")
sum_reduced = np.add.reduce(reduce_arr) # Equivalent to np.sum(reduce_arr)
print(f"np.add.reduce(reduce_arr): {sum_reduced}") # 1+2+3+4+5 = 15

product_reduced = np.multiply.reduce(reduce_arr) # Equivalent to np.prod(reduce_arr)
print(f"np.multiply.reduce(reduce_arr): {product_reduced}") # 1*2*3*4*5 = 120

# 7.2 `accumulate()`: Applies the ufunc repeatedly, returning intermediate results.
accumulate_result = np.add.accumulate(reduce_arr) # Equivalent to np.cumsum(reduce_arr)
print(f"np.add.accumulate(reduce_arr): {accumulate_result}") # [ 1  3  6 10 15]

accumulate_prod_result = np.multiply.accumulate(reduce_arr) # Equivalent to np.cumprod(reduce_arr)
print(f"np.multiply.accumulate(reduce_arr): {accumulate_prod_result}") # [  1   2   6  24 120]

# 7.3 `outer()`: Computes the outer product of two arrays using the ufunc.
# For `np.add.outer(a,b)`, result[i,j] = a[i] + b[j]
arr_outer1 = np.array([1, 2])
arr_outer2 = np.array([10, 20, 30])
print(f"\nOuter product arrays: {arr_outer1}, {arr_outer2}")
outer_add = np.add.outer(arr_outer1, arr_outer2)
print(f"np.add.outer(arr_outer1, arr_outer2):\n{outer_add}")
# Output:
# [[11 21 31]  (1+10, 1+20, 1+30)
#  [12 22 32]]  (2+10, 2+20, 2+30)

outer_multiply = np.multiply.outer(arr_outer1, arr_outer2)
print(f"np.multiply.outer(arr_outer1, arr_outer2):\n{outer_multiply}")
# Output:
# [[10 20 30]
#  [20 40 60]]


print("\n--- End of NumPy Universal Functions (Ufuncs) Practice Code ---")