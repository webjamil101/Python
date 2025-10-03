import numpy as np
import sys # To demonstrate sys.getsizeof for comparison

print("--- NumPy Array Attributes: Practice Code ---")

# --- 1. Introduction to Array Attributes ---
print("\n--- 1. Introduction to Array Attributes ---")
print("NumPy array attributes are properties of the `ndarray` object that describe its characteristics.")
print("They are accessed directly on the array object (e.g., `my_array.shape`), not as methods.")
print("These attributes are constant for a given array (except when modified in-place by certain operations like `resize`).")


# --- 2. Common and Essential Attributes ---

# Let's create some example arrays to demonstrate attributes
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
array_3d = np.arange(1, 28).reshape(3, 3, 3) # 3x3x3 array

print(f"\n--- Example Arrays ---")
print(f"array_1d:\n{array_1d}")
print(f"array_2d:\n{array_2d}")
print(f"array_3d (first slice):\n{array_3d[0]}")


# 2.1 `ndim`: Number of dimensions (axes)
print("\n--- 2.1 `ndim`: Number of Dimensions ---")
print("`ndim` returns an integer representing the number of array dimensions.")
print(f"array_1d.ndim: {array_1d.ndim}") # Output: 1
print(f"array_2d.ndim: {array_2d.ndim}") # Output: 2
print(f"array_3d.ndim: {array_3d.ndim}") # Output: 3


# 2.2 `shape`: Dimensions of the array
print("\n--- 2.2 `shape`: Dimensions of the Array ---")
print("`shape` returns a tuple of integers indicating the size of the array in each dimension.")
print("It's typically (rows, columns) for 2D arrays, or (depth, rows, columns) for 3D.")
print(f"array_1d.shape: {array_1d.shape}") # Output: (5,)
print(f"array_2d.shape: {array_2d.shape}") # Output: (3, 3)
print(f"array_3d.shape: {array_3d.shape}") # Output: (3, 3, 3)

# Reshaping an array modifies its shape attribute
reshaped_2d = array_1d.reshape(1, 5) # 1 row, 5 columns
print(f"array_1d.reshape(1, 5).shape: {reshaped_2d.shape}") # Output: (1, 5)


# 2.3 `size`: Total number of elements
print("\n--- 2.3 `size`: Total Number of Elements ---")
print("`size` returns the total number of elements in the array.")
print("It's equivalent to the product of the elements in `shape`.")
print(f"array_1d.size: {array_1d.size}") # Output: 5 (1*5)
print(f"array_2d.size: {array_2d.size}") # Output: 9 (3*3)
print(f"array_3d.size: {array_3d.size}") # Output: 27 (3*3*3)


# 2.4 `dtype`: Data type of the elements
print("\n--- 2.4 `dtype`: Data Type of Elements ---")
print("`dtype` returns an object describing the type of the elements in the array.")
print("All elements in a NumPy array must have the same data type.")
print(f"array_1d.dtype: {array_1d.dtype}") # Output: int64 (or int32 on 32-bit systems)
float_array = np.array([1.1, 2.2, 3.3])
print(f"float_array.dtype: {float_array.dtype}") # Output: float64
bool_array = np.array([True, False])
print(f"bool_array.dtype: {bool_array.dtype}") # Output: bool
complex_array = np.array([1+2j, 3+4j])
print(f"complex_array.dtype: {complex_array.dtype}") # Output: complex128

# You can specify dtype upon creation
explicit_dtype_array = np.array([1, 2, 3], dtype=np.float32)
print(f"explicit_dtype_array.dtype: {explicit_dtype_array.dtype}") # Output: float32


# 2.5 `itemsize`: Size of each element in bytes
print("\n--- 2.5 `itemsize`: Size of Each Element in Bytes ---")
print("`itemsize` returns the size in bytes of each element of the array.")
print(f"array_1d.itemsize: {array_1d.itemsize} bytes") # For int64, 8 bytes
print(f"float_array.itemsize: {float_array.itemsize} bytes") # For float64, 8 bytes
print(f"bool_array.itemsize: {bool_array.itemsize} bytes") # For bool, 1 byte
print(f"explicit_dtype_array.itemsize: {explicit_dtype_array.itemsize} bytes") # For float32, 4 bytes


# 2.6 `nbytes`: Total bytes consumed by the array data
print("\n--- 2.6 `nbytes`: Total Bytes Consumed by Array Data ---")
print("`nbytes` returns the total number of bytes consumed by the array data.")
print("It's equivalent to `array.size * array.itemsize`.")
print(f"array_1d.nbytes: {array_1d.nbytes} bytes ({array_1d.size} * {array_1d.itemsize})")
print(f"array_2d.nbytes: {array_2d.nbytes} bytes ({array_2d.size} * {array_2d.itemsize})")
print(f"array_3d.nbytes: {array_3d.nbytes} bytes ({array_3d.size} * {array_3d.itemsize})")

# Compare with Python list (NumPy is much more memory efficient for numerical data)
py_list = list(range(1000))
np_array = np.arange(1000)
print(f"\nMemory comparison (conceptually):")
print(f"Size of Python list (1000 ints): {sys.getsizeof(py_list)} bytes")
print(f"Size of NumPy array (1000 ints): {np_array.nbytes} bytes")
print(f"Note: sys.getsizeof() for lists includes list object overhead, NumPy's nbytes is raw data size.")


# --- 3. Memory Layout and Order Attributes ---
print("\n--- 3. Memory Layout and Order Attributes ---")
print("These attributes describe how the array elements are stored in memory.")

# 3.1 `flags`: Information about memory layout
print("\n--- 3.1 `flags`: Information about Memory Layout ---")
print("`flags` returns a dictionary of flags regarding the memory layout of the array.")
print("Key flags include `C_CONTIGUOUS`, `F_CONTIGUOUS`, `OWNDATA`, `WRITEABLE`.")
print(f"array_2d.flags:\n{array_2d.flags}")

# Create a C-contiguous array (default)
c_array = np.array([[1, 2], [3, 4]], order='C')
print(f"\nC-contiguous array (row-major):\n{c_array.flags['C_CONTIGUOUS']=}\n{c_array.flags['F_CONTIGUOUS']=}")

# Create a Fortran-contiguous array (column-major)
f_array = np.array([[1, 2], [3, 4]], order='F')
print(f"\nF-contiguous array (column-major):\n{f_array.flags['C_CONTIGUOUS']=}\n{f_array.flags['F_CONTIGUOUS']=}")

# A sliced array might not be contiguous
sliced_array = array_2d[:, ::2] # Every other column
print(f"\nSliced array (might not be contiguous):\n{sliced_array.flags['C_CONTIGUOUS']=}")


# 3.2 `strides`: Bytes to step to next element
print("\n--- 3.2 `strides`: Bytes to Step to Next Element ---")
print("`strides` returns a tuple of bytes to step in each dimension when moving to the next element.")
print("`strides[0]` is bytes to go to next row, `strides[1]` is bytes to go to next column.")
print(f"array_2d (shape={array_2d.shape}, itemsize={array_2d.itemsize} bytes):\n{array_2d}")
print(f"array_2d.strides: {array_2d.strides}")
# For int64 (8 bytes), shape (3,3):
# (3 columns * 8 bytes/col, 1 column * 8 bytes/col) = (24, 8)
# To move to next row, jump 24 bytes. To move to next column, jump 8 bytes.

print(f"\nC-contiguous array {c_array.shape}, itemsize {c_array.itemsize}:\n{c_array}")
print(f"c_array.strides: {c_array.strides}") # (2*8, 1*8) = (16, 8)

print(f"\nF-contiguous array {f_array.shape}, itemsize {f_array.itemsize}:\n{f_array}")
print(f"f_array.strides: {f_array.strides}") # (1*8, 2*8) = (8, 16)


# --- 4. Other Useful Attributes ---

# 4.1 `base`: If array is a view of another array
print("\n--- 4.1 `base`: Reference to Base Array ---")
print("`base` refers to the original object that this array is a view of.")
print("If the array owns its own data, `base` is `None`.")
view_array = array_2d[0, :] # Slicing often creates a view
copy_array = array_2d.copy() # .copy() creates a new array with its own data

print(f"array_2d.base is None: {array_2d.base is None}")
print(f"view_array.base is array_2d: {view_array.base is array_2d}")
print(f"copy_array.base is None: {copy_array.base is None}")

# Modifying a view modifies the original array
view_array[0] = 99
print(f"Original array after modifying view:\n{array_2d}")
view_array[0] = 10 # Reset for next example


# 4.2 `T`: Transposed array (view)
print("\n--- 4.2 `T`: Transposed Array ---")
print("`T` returns the transposed view of the array (rows become columns, columns become rows).")
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\nOriginal matrix:\n{matrix}")
print(f"Transposed matrix (matrix.T):\n{matrix.T}")
print(f"Original shape: {matrix.shape}, Transposed shape: {matrix.T.shape}")


# 4.3 `data`: Python buffer object pointing to array's start
print("\n--- 4.3 `data`: Python Buffer Object ---")
print("`data` is the buffer object pointing to the start of the array's data in memory.")
print("It's low-level and generally not used directly in common Python code.")
print(f"array_1d.data: {array_1d.data}")
# type(array_1d.data) -> <class 'memoryview'>


# 4.4 `real` and `imag`: Real and Imaginary parts (for complex numbers)
print("\n--- 4.4 `real` and `imag`: Real/Imaginary Parts ---")
complex_numbers = np.array([1+2j, 3-4j, 5j])
print(f"\nComplex array: {complex_numbers}")
print(f"Real part: {complex_numbers.real}")
print(f"Imaginary part: {complex_numbers.imag}")


# --- 5. When do attributes change? ---
print("\n--- 5. When do attributes change? ---")
print("Most attributes (like `shape`, `ndim`, `dtype`, `size`) are fixed once an array is created,")
print("unless you explicitly call a method that returns a new array with changed attributes (e.g., `reshape()`)")
print("or an in-place modification method (like `resize()` or direct assignment if writeable).")

mod_array = np.zeros((2, 2))
print(f"\nOriginal mod_array shape: {mod_array.shape}")
mod_array.resize((4, 1)) # In-place resize
print(f"mod_array after resize (in-place) shape: {mod_array.shape}")
print(f"mod_array content after resize:\n{mod_array}")


print("\n--- End of NumPy Array Attributes Practice Code ---")