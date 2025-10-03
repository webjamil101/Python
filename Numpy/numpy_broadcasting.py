import numpy as np

print("--- NumPy Broadcasting: Practice Code ---")

# --- 1. What is Broadcasting? ---
print("\n--- 1. What is Broadcasting? ---")
print("Broadcasting is a set of rules NumPy applies to enable operations between arrays of different shapes.")
print("It allows us to perform arithmetic operations, comparisons, and other ufunc (universal function) operations.")
print("Without broadcasting, arrays would need to have exactly the same shape for element-wise operations.")
print("The primary goal is to perform operations without explicitly copying data to match shapes, saving memory and time.")


# --- 2. Broadcasting Rules ---
print("\n--- 2. Broadcasting Rules Explained ---")
print("Broadcasting occurs when iterating over operand arrays in reverse order of their dimensions, starting with the trailing dimensions.")
print("Two dimensions are compatible when:")
print(" 1. They are equal, OR")
print(" 2. One of them is 1 (in which case the dimension with size 1 is stretched or 'broadcast' to match the other).")
print("If these conditions are not met, a `ValueError` is raised.")

# --- 3. Broadcasting Examples ---

# 3.1 Scalar Broadcasting
print("\n--- 3.1 Scalar Broadcasting ---")
print("A scalar can be broadcast to any array, effectively performing the operation with the scalar value on every element.")
arr_scalar = np.array([1, 2, 3])
scalar_val = 5
print(f"Array: {arr_scalar}")
print(f"Scalar: {scalar_val}")

print(f"Array + Scalar: {arr_scalar + scalar_val}")   # [ 6  7  8]
print(f"Array * Scalar: {arr_scalar * scalar_val}")   # [ 5 10 15]
print(f"Array > Scalar: {arr_scalar > 2}")        # [False True True]


# 3.2 1D Array + 2D Array (Row Broadcasting)
print("\n--- 3.2 1D Array + 2D Array (Row Broadcasting) ---")
# Rule: If dimensions do not match, pad the smaller shape with ones on its left side.
# Then, apply the two rules.
mat_2d = np.array([[10, 20, 30],
                   [40, 50, 60]]) # Shape (2, 3)
vec_1d = np.array([1, 2, 3])     # Shape (3,)

# How broadcasting sees it:
# mat_2d: (2, 3)
# vec_1d: (1, 3)  (NumPy automatically adds a leading dimension of 1)
# Result: (2, 3)

print(f"2D Matrix:\n{mat_2d} (shape: {mat_2d.shape})")
print(f"1D Vector: {vec_1d} (shape: {vec_1d.shape})")

result_row_broadcast = mat_2d + vec_1d
print(f"Matrix + Vector (row broadcast):\n{result_row_broadcast}")
# Output:
# [[11 22 33]  (10+1, 20+2, 30+3)
#  [41 52 63]]  (40+1, 50+2, 60+3)


# 3.3 2D Array + Column Vector (Column Broadcasting)
print("\n--- 3.3 2D Array + Column Vector (Column Broadcasting) ---")
col_vec = np.array([[100],
                    [200]]) # Shape (2, 1)

# How broadcasting sees it:
# mat_2d:  (2, 3)
# col_vec: (2, 1)
# Result:  (2, 3)

print(f"2D Matrix:\n{mat_2d} (shape: {mat_2d.shape})")
print(f"Column Vector:\n{col_vec} (shape: {col_vec.shape})")

result_col_broadcast = mat_2d + col_vec
print(f"Matrix + Column Vector (column broadcast):\n{result_col_broadcast}")
# Output:
# [[110 120 130]  (10+100, 20+100, 30+100)
#  [240 250 260]]  (40+200, 50+200, 60+200)


# 3.4 Both Arrays Broadcastable (e.g., Column Vector + Row Vector)
print("\n--- 3.4 Both Arrays Broadcastable (Column Vector + Row Vector) ---")
row_vec_single = np.array([1, 2, 3])     # Shape (3,) -> (1, 3) for broadcasting
col_vec_single = np.array([[10], [20]])  # Shape (2, 1)

# How broadcasting sees it:
# col_vec_single: (2, 1)
# row_vec_single: (1, 3)
# Result:         (2, 3)

print(f"Row Vector: {row_vec_single} (shape: {row_vec_single.shape})")
print(f"Column Vector:\n{col_vec_single} (shape: {col_vec_single.shape})")

result_both_broadcast = row_vec_single + col_vec_single
print(f"Row Vector + Column Vector:\n{result_both_broadcast}")
# Output:
# [[11 12 13]  (10+1, 10+2, 10+3)
#  [21 22 23]]  (20+1, 20+2, 20+3)


# 3.5 More Complex Broadcasting Example
print("\n--- 3.5 More Complex Broadcasting Example ---")
arr_A = np.arange(1, 13).reshape(2, 2, 3) # Shape (2, 2, 3)
# [[[ 1  2  3]
#   [ 4  5  6]]
#
#  [[ 7  8  9]
#   [10 11 12]]]

arr_B = np.arange(10, 13) # Shape (3,) -> (1, 1, 3) for broadcasting
# [10 11 12]

# How broadcasting sees it:
# arr_A: (2, 2, 3)
# arr_B: (1, 1, 3)
# Result: (2, 2, 3)

print(f"Array A (3D):\n{arr_A} (shape: {arr_A.shape})")
print(f"Array B (1D): {arr_B} (shape: {arr_B.shape})")

result_3d = arr_A * arr_B
print(f"Result of A * B:\n{result_3d}")
# Each element of arr_A is multiplied by the corresponding element from arr_B,
# which is effectively stretched across the first two dimensions.
# e.g., arr_A[0,0,0]*arr_B[0], arr_A[0,0,1]*arr_B[1], arr_A[0,0,2]*arr_B[2]
#       1*10, 2*11, 3*12
# Output:
# [[[ 10  22  36]
#   [ 40  55  72]]
#
#  [[ 70  88 108]
#   [100 121 144]]]


# --- 4. When Broadcasting Fails ---
print("\n--- 4. When Broadcasting Fails ---")
print("Broadcasting fails when dimensions are incompatible according to the rules.")

# Example 1: Trailing dimensions don't match and neither is 1
try:
    arr_fail1 = np.array([[1, 2, 3], [4, 5, 6]]) # Shape (2, 3)
    arr_fail2 = np.array([1, 2])                 # Shape (2,) -> (1, 2)
    print(f"\nAttempting to add shapes (2,3) and (2,) (expect error):")
    # (2, 3)
    # (1, 2) <- trailing dimensions (3 vs 2) are not equal and neither is 1
    arr_fail1 + arr_fail2
except ValueError as e:
    print(f"Caught expected error: {e}") # `operands could not be broadcast together with shapes (2,3) (2,)`

# Example 2: More complex mismatch
try:
    arr_fail3 = np.zeros((3, 4, 5)) # Shape (3, 4, 5)
    arr_fail4 = np.zeros((4, 1))    # Shape (4, 1) -> (1, 4, 1) for broadcasting
    print(f"\nAttempting to add shapes (3,4,5) and (4,1) (expect error):")
    # arr_fail3: (3, 4, 5)
    # arr_fail4: (1, 4, 1)
    # Match: (5 vs 1 -> OK), (4 vs 4 -> OK), (3 vs 1 -> OK)
    # Wait, this example actually *works*! Let's find one that truly fails.
    # What if the middle dimension was mismatched?

    arr_fail5 = np.zeros((3, 4, 5)) # Shape (3, 4, 5)
    arr_fail6 = np.zeros((2, 5))    # Shape (2, 5) -> (1, 2, 5) for broadcasting
    print(f"\nAttempting to add shapes (3,4,5) and (2,5) (expect error):")
    # arr_fail5: (3, 4, 5)
    # arr_fail6: (1, 2, 5)
    # Match: (5 vs 5 -> OK), (4 vs 2 -> NOT OK!)
    arr_fail5 + arr_fail6
except ValueError as e:
    print(f"Caught expected error: {e}") # `operands could not be broadcast together with shapes (3,4,5) (2,5)`


# --- 5. Making Arrays Broadcastable (Adding Dimensions) ---
print("\n--- 5. Making Arrays Broadcastable (Adding Dimensions) ---")
print("You can explicitly add new dimensions of size 1 using `np.newaxis` (or `None`).")

original_1d = np.array([1, 2, 3]) # Shape (3,)
mat_to_add = np.array([[10, 20, 30],
                       [40, 50, 60]]) # Shape (2, 3)

# If we want to add `original_1d` as a column to `mat_to_add`, direct addition fails.
try:
    print(f"\nAttempting to add (2,3) and (3,) as column (expect error):")
    mat_to_add + original_1d[:, np.newaxis] # This attempts (2,3) + (3,1) -> Fails
except ValueError as e:
    print(f"Caught expected error: {e}") # `operands could not be broadcast together with shapes (2,3) (3,1)`

# Correct way to add a column vector:
col_vector_from_1d = original_1d[:, np.newaxis] # Shape (3, 1)
print(f"1D array as column vector: {col_vector_from_1d} (shape: {col_vector_from_1d.shape})")

# Now, if we try to add a 2D array and a properly shaped column vector:
mat_example = np.array([[10, 20],
                        [30, 40],
                        [50, 60]]) # Shape (3, 2)
col_vec_example = np.array([[1], [2], [3]]) # Shape (3, 1)
print(f"\nMatrix example:\n{mat_example} (shape: {mat_example.shape})")
print(f"Column vector example:\n{col_vec_example} (shape: {col_vec_example.shape})")

# Broadcasting: (3, 2) + (3, 1) -> (3, 2) (compatible!)
result_explicit_broadcast = mat_example + col_vec_example
print(f"Matrix + Column Vector (explicitly shaped):\n{result_explicit_broadcast}")
# Output:
# [[11 21]
#  [32 42]
#  [53 63]]


print("\n--- End of NumPy Broadcasting Practice Code ---")