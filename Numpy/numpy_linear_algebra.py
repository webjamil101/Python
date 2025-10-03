import numpy as np

print("--- NumPy Linear Algebra: Practice Code ---")

# --- 1. Basic Vector and Matrix Creation ---
print("\n--- 1. Basic Vector and Matrix Creation ---")

# 1.1 Vectors (1D arrays)
vec_a = np.array([1, 2, 3])
vec_b = np.array([4, 5, 6])
print(f"Vector a: {vec_a}")
print(f"Vector b: {vec_b}")

# 1.2 Matrices (2D arrays)
matrix_A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

matrix_B = np.array([
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
])

matrix_C = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]) # Identity matrix

print(f"\nMatrix A:\n{matrix_A}")
print(f"Matrix B:\n{matrix_B}")
print(f"Matrix C (Identity):\n{matrix_C}")

# Special matrices
identity_matrix = np.eye(3) # 3x3 identity matrix
print(f"\nnp.eye(3) (Identity Matrix):\n{identity_matrix}")
zeros_matrix = np.zeros((2, 3)) # 2x3 matrix of zeros
print(f"np.zeros((2,3)):\n{zeros_matrix}")
ones_matrix = np.ones((3, 2)) # 3x2 matrix of ones
print(f"np.ones((3,2)):\n{ones_matrix}")


# --- 2. Vector Operations ---
print("\n--- 2. Vector Operations ---")

# 2.1 Vector Addition and Subtraction (Element-wise)
print(f"\nVector a + Vector b: {vec_a + vec_b}") # [5 7 9]
print(f"Vector a - Vector b: {vec_a - vec_b}") # [-3 -3 -3]

# 2.2 Scalar Multiplication
print(f"Vector a * 3: {vec_a * 3}") # [3 6 9]

# 2.3 Dot Product (Scalar Product)
# `np.dot(vec_a, vec_b)` or `vec_a @ vec_b` for 1D arrays
dot_product = np.dot(vec_a, vec_b)
print(f"Dot product of a and b (np.dot): {dot_product}") # 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32
print(f"Dot product of a and b (@ operator): {vec_a @ vec_b}") # 32

# 2.4 Cross Product (for 3D vectors)
cross_product = np.cross(vec_a, vec_b)
print(f"Cross product of a and b (np.cross): {cross_product}") # [-3  6 -3]

# 2.5 Vector Norm (Magnitude/Length)
# `np.linalg.norm()`
norm_a = np.linalg.norm(vec_a)
print(f"Euclidean norm (L2 norm) of a: {norm_a:.2f}") # sqrt(1^2 + 2^2 + 3^2) = sqrt(1+4+9) = sqrt(14) ~ 3.74

# Other norms (L1 norm, etc.)
l1_norm_a = np.linalg.norm(vec_a, ord=1) # Sum of absolute values
print(f"L1 norm of a: {l1_norm_a}") # 1 + 2 + 3 = 6


# --- 3. Matrix Operations ---
print("\n--- 3. Matrix Operations ---")

# 3.1 Matrix Addition and Subtraction (Element-wise)
print(f"\nMatrix A + Matrix B:\n{matrix_A + matrix_B}")
print(f"Matrix A - Matrix B:\n{matrix_A - matrix_B}")

# 3.2 Scalar-Matrix Multiplication
print(f"Matrix A * 2:\n{matrix_A * 2}")

# 3.3 Element-wise Multiplication (Hadamard Product)
# This is NOT matrix multiplication. Use `*` operator.
print(f"Element-wise multiplication (A * B):\n{matrix_A * matrix_B}")

# 3.4 Matrix Multiplication (Dot Product of Matrices)
# Use `@` operator (preferred in modern NumPy) or `np.dot()`
matrix_product_AB = matrix_A @ matrix_B
print(f"\nMatrix A @ Matrix B (Matrix Multiplication):\n{matrix_product_AB}")
# Result: C_ij = sum_k (A_ik * B_kj)

matrix_product_dot_AB = np.dot(matrix_A, matrix_B)
print(f"np.dot(Matrix A, Matrix B):\n{matrix_product_dot_AB}")

# Matrix-vector multiplication
matrix_vec_product = matrix_A @ vec_a
print(f"Matrix A @ Vector a:\n{matrix_vec_product}") # (3,3) @ (3,) -> (3,)


# 3.5 Transpose
# `matrix.T` or `np.transpose(matrix)`
print(f"\nTranspose of Matrix A (A.T):\n{matrix_A.T}")

# 3.6 Determinant
# `np.linalg.det()`
det_A = np.linalg.det(matrix_A)
print(f"\nDeterminant of Matrix A: {det_A:.2f}") # For matrix_A, determinant is usually 0 due to linear dependence.
# Let's create a non-singular matrix for a better example
non_singular_matrix = np.array([
    [1, 2],
    [3, 4]
])
det_non_singular = np.linalg.det(non_singular_matrix)
print(f"Determinant of non-singular matrix:\n{non_singular_matrix}\nis: {det_non_singular:.2f}") # (1*4 - 2*3) = 4 - 6 = -2


# 3.7 Inverse
# `np.linalg.inv()`
# Only for square, non-singular matrices
try:
    inv_matrix_C = np.linalg.inv(matrix_C) # Inverse of Identity is Identity
    print(f"\nInverse of Identity Matrix C:\n{inv_matrix_C}")

    inv_non_singular = np.linalg.inv(non_singular_matrix)
    print(f"Inverse of non-singular matrix:\n{inv_non_singular}")
    # Verify: matrix @ inverse should be identity
    print(f"Check: non_singular_matrix @ its inverse:\n{np.round(non_singular_matrix @ inv_non_singular)}")

except np.linalg.LinAlgError as e:
    print(f"\nCaught error trying to invert singular matrix: {e}")
    # matrix_A is singular (determinant 0), so it doesn't have an inverse.
    # To demonstrate:
    try:
        np.linalg.inv(matrix_A)
    except np.linalg.LinAlgError as e:
        print(f"Caught expected error when inverting matrix_A: {e}")


# --- 4. Solving Linear Equations ---
print("\n--- 4. Solving Linear Equations ---")
# Solve for x in Ax = b
# A is a matrix, x and b are vectors
# Use `np.linalg.solve(A, b)`

# Example:
# x + 2y = 5
# 3x + 4y = 11

A_solve = np.array([[1, 2], [3, 4]])
b_solve = np.array([5, 11])

print(f"\nSystem to solve: Ax = b")
print(f"A:\n{A_solve}")
print(f"b: {b_solve}")

solution_x = np.linalg.solve(A_solve, b_solve)
print(f"Solution x: {solution_x}") # Expected: [1. 2.] (1 + 2*2 = 5; 3*1 + 4*2 = 11)

# Verify the solution
print(f"Check A @ x: {A_solve @ solution_x}")


# --- 5. Eigenvalues and Eigenvectors ---
print("\n--- 5. Eigenvalues and Eigenvectors ---")
# `np.linalg.eig()` returns eigenvalues and eigenvectors
# `np.linalg.eigh()` is for symmetric/Hermitian matrices (more efficient and stable)

# Example symmetric matrix
sym_matrix = np.array([
    [4, 2],
    [2, 5]
])
print(f"\nSymmetric Matrix:\n{sym_matrix}")

eigenvalues, eigenvectors = np.linalg.eigh(sym_matrix)
print(f"Eigenvalues: {eigenvalues}")
print(f"Eigenvectors:\n{eigenvectors}")
# Each column of eigenvectors corresponds to an eigenvalue
# eigvecs[:, 0] is eigenvector for eigvals[0]

# Verify: Av = lambda*v (Matrix @ Eigenvector = Eigenvalue * Eigenvector)
v1 = eigenvectors[:, 0]
lambda1 = eigenvalues[0]
print(f"\nCheck for first eigenvalue/vector:")
print(f"A @ v1: {sym_matrix @ v1}")
print(f"lambda1 * v1: {lambda1 * v1}")
# The results should be numerically very close


# --- 6. Singular Value Decomposition (SVD) ---
print("\n--- 6. Singular Value Decomposition (SVD) ---")
# `np.linalg.svd()`
# Decomposes a matrix A into U * Sigma * Vh, where:
# U and Vh are unitary matrices, and Sigma is a diagonal matrix of singular values.
# SVD is widely used in dimensionality reduction (PCA), noise reduction, etc.

svd_matrix = np.array([
    [1, 1],
    [2, 2],
    [3, 3]
]) # A rank-1 matrix
print(f"\nMatrix for SVD:\n{svd_matrix}")

U, s, Vh = np.linalg.svd(svd_matrix)
print(f"U (left singular vectors):\n{U}")
print(f"s (singular values, as 1D array): {s}") # Important singular values
print(f"Vh (right singular vectors, transposed):\n{Vh}")

# Reconstruct the original matrix (approximately due to floating point)
Sigma = np.zeros((svd_matrix.shape[0], svd_matrix.shape[1]))
Sigma[:svd_matrix.shape[1], :svd_matrix.shape[1]] = np.diag(s)
reconstructed_matrix = U @ Sigma @ Vh
print(f"Reconstructed matrix (approx):\n{np.round(reconstructed_matrix)}")


print("\n--- End of NumPy Linear Algebra Practice Code ---")