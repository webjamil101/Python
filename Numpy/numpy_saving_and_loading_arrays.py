import numpy as np
import os

print("--- NumPy Saving and Loading Arrays: Practice Code ---")

# Define a directory for temporary files
output_dir = "numpy_save_load_examples"
os.makedirs(output_dir, exist_ok=True)
print(f"Temporary files will be saved in: {output_dir}")


# --- 1. Saving and Loading Single Arrays (`.npy` format) ---
print("\n--- 1. Saving and Loading Single Arrays (`.npy` format) ---")
print("The `.npy` format is the standard binary file format for saving a single NumPy array.")
print("It's highly efficient and preserves array metadata (dtype, shape, etc.).")

# Create a sample array
data_to_save = np.arange(10, 100, 10).reshape(3, 3)
print(f"\nOriginal array to save:\n{data_to_save}")
print(f"Shape: {data_to_save.shape}, Dtype: {data_to_save.dtype}")

# 1.1 Saving with `np.save()`
filename_npy = os.path.join(output_dir, "my_array.npy")
np.save(filename_npy, data_to_save)
print(f"Array saved to: {filename_npy}")

# 1.2 Loading with `np.load()`
loaded_array = np.load(filename_npy)
print(f"Array loaded from {filename_npy}:\n{loaded_array}")
print(f"Shape: {loaded_array.shape}, Dtype: {loaded_array.dtype}")

# Verify if the loaded array is identical
print(f"Are original and loaded arrays equal? {np.array_equal(data_to_save, loaded_array)}")


# --- 2. Saving and Loading Multiple Arrays (`.npz` format) ---
print("\n--- 2. Saving and Loading Multiple Arrays (`.npz` format) ---")
print("The `.npz` format allows you to save multiple NumPy arrays into a single, compressed file.")
print("It's essentially a zipped archive of `.npy` files.")

# Create a few sample arrays
array1 = np.random.rand(2, 2)
array2 = np.array([10, 20, 30])
array_names = ['matrix_rand', 'vector_int'] # Optional: names for the arrays

print(f"\nArray 1 (matrix_rand):\n{array1}")
print(f"Array 2 (vector_int): {array2}")

# 2.1 Saving with `np.savez()` (uncompressed)
filename_npz_uncompressed = os.path.join(output_dir, "multiple_arrays_uncompressed.npz")
np.savez(filename_npz_uncompressed, a=array1, b=array2) # Keys 'a' and 'b' will be used to access
print(f"Multiple arrays saved (uncompressed) to: {filename_npz_uncompressed}")

# 2.2 Saving with `np.savez_compressed()` (compressed - recommended for space)
filename_npz_compressed = os.path.join(output_dir, "multiple_arrays_compressed.npz")
# You can pass keyword arguments, where keywords become the names for the arrays
np.savez_compressed(filename_npz_compressed, matrix_data=array1, vector_data=array2, some_scalar=5.5)
print(f"Multiple arrays saved (compressed) to: {filename_npz_compressed}")


# 2.3 Loading `.npz` files with `np.load()`
print(f"\nLoading from {filename_npz_compressed}:")
loaded_npz = np.load(filename_npz_compressed)
print(f"Loaded object type: {type(loaded_npz)}") # <class 'numpy.lib.npyio.NpzFile'>

# Access arrays using dictionary-like keys
print(f"Keys available in .npz file: {loaded_npz.files}") # Returns a list of keys

loaded_array1_from_npz = loaded_npz['matrix_data']
loaded_array2_from_npz = loaded_npz['vector_data']
loaded_scalar_from_npz = loaded_npz['some_scalar']

print(f"Loaded matrix_data:\n{loaded_array1_from_npz}")
print(f"Loaded vector_data: {loaded_array2_from_npz}")
print(f"Loaded some_scalar: {loaded_scalar_from_npz}")

# Important: Close the loaded NpzFile object when done to release resources
# (especially important if files are large or opened in a loop)
loaded_npz.close()


# --- 3. Saving and Loading with Plain Text Files (`.txt`, `.csv`) ---
print("\n--- 3. Saving and Loading with Plain Text Files (`.txt`, `.csv`) ---")
print("NumPy can read/write simple delimited text files, but it's generally less efficient")
print("and loses metadata (dtype, exact shape) compared to `.npy`/`.npz`.")
print("It's useful for interoperability with other software that expects plain text.")

text_data = np.array([
    [1.1, 2.2, 3.3],
    [4.4, 5.5, 6.6]
])
print(f"\nOriginal text data array:\n{text_data}")

# 3.1 Saving with `np.savetxt()`
filename_txt = os.path.join(output_dir, "my_data.txt")
np.savetxt(filename_txt, text_data, delimiter=',', fmt='%.2f', header='Col1,Col2,Col3', comments='# ')
# `delimiter`: string or character separating columns
# `fmt`: format string for writing numbers (e.g., '%.2f' for 2 decimal places)
# `header`: string to be written at the beginning of the file (prefixed by `comments` string)
# `comments`: string that will be prepended to the header and footer strings
print(f"Array saved to text file: {filename_txt}")
print("File content (check manually or read back):")
with open(filename_txt, 'r') as f:
    print(f.read())

# 3.2 Loading with `np.loadtxt()`
loaded_from_txt = np.loadtxt(filename_txt, delimiter=',')
print(f"Array loaded from text file:\n{loaded_from_txt}")
# Notice: `loadtxt` infers dtype (usually float64) and shape from the data.
print(f"Shape: {loaded_from_txt.shape}, Dtype: {loaded_from_txt.dtype}")

# 3.3 Loading with `np.genfromtxt()` (more robust for missing values, uneven rows, comments)
print("\n--- 3.3 `np.genfromtxt()` (more robust) ---")
# Create a text file with missing values and comments for demonstration
text_data_with_missing = """
# Data with some missing values
1,2,3
4,,6
7,8,
9,10,11 # End of data
"""
filename_missing_txt = os.path.join(output_dir, "data_with_missing.txt")
with open(filename_missing_txt, 'w') as f:
    f.write(text_data_with_missing.strip())
print(f"Created text file with missing data: {filename_missing_txt}")

loaded_genfromtxt = np.genfromtxt(filename_missing_txt, delimiter=',', comments='#', filling_values=0)
# `filling_values`: value to use for missing data
print(f"Array loaded with genfromtxt (filling missing with 0):\n{loaded_genfromtxt}")

loaded_genfromtxt_nan = np.genfromtxt(filename_missing_txt, delimiter=',', comments='#', dtype=float)
# By default, missing values will be converted to NaN if dtype is float
print(f"Array loaded with genfromtxt (missing as NaN):\n{loaded_genfromtxt_nan}")


# --- 4. Memory Mapping for Large Files (`np.memmap`) ---
print("\n--- 4. Memory Mapping for Large Files (`np.memmap`) ---")
print("`np.memmap` allows you to access portions of an array stored in a file on disk as if")
print("it were in memory, without loading the entire file into RAM.")
print("This is useful for very large datasets that don't fit into memory.")

memmap_data = np.arange(100_000, dtype='float32') # Large array
memmap_filename = os.path.join(output_dir, "large_array.dat")
memmap_data.tofile(memmap_filename) # Save array to a raw binary file

print(f"\nCreated a large raw binary file: {memmap_filename}")

# Create a memory map to the file
mmap_array = np.memmap(memmap_filename, dtype='float32', mode='r', shape=(100_000,))
print(f"Memory-mapped array (first 5 elements): {mmap_array[:5]}")
print(f"Memory-mapped array (last 5 elements): {mmap_array[-5:]}")

# You can modify data in 'r+' (read/write) mode
mmap_write_array = np.memmap(memmap_filename, dtype='float32', mode='r+', shape=(100_000,))
mmap_write_array[0] = 999.99
mmap_write_array.flush() # Ensure changes are written to disk
print(f"First element after modification: {mmap_write_array[0]}")

# Re-read to confirm change (if opened in 'r' mode)
mmap_read_confirm = np.memmap(memmap_filename, dtype='float32', mode='r', shape=(100_000,))
print(f"Confirmed first element after flush: {mmap_read_confirm[0]}")
del mmap_write_array # Close the memory map for writing
del mmap_read_confirm # Close the memory map for reading


# --- Cleanup ---
print("\n--- Cleaning up generated files ---")
try:
    for f in os.listdir(output_dir):
        os.remove(os.path.join(output_dir, f))
    os.rmdir(output_dir)
    print(f"Cleaned up {output_dir} directory.")
except OSError as e:
    print(f"Error during cleanup: {e}")

print("\n--- End of NumPy Saving and Loading Arrays Practice Code ---")