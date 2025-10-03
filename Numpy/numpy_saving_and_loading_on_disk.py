# ====================================================================
# NumPy Saving and Loading
# ====================================================================

import numpy as np

# Create a sample array to save
arr_to_save = np.arange(10).reshape(2, 5)
print("Original Array to be Saved:")
print(arr_to_save)
print("-" * 30)

# --------------------------------------------------------------------
# 1. Saving a Single Array to a Binary .npy File
# --------------------------------------------------------------------

# np.save() saves a NumPy array to a binary file with a .npy extension.
# This is the standard format for saving a single NumPy array on disk.
file_path_npy = 'my_array.npy'
np.save(file_path_npy, arr_to_save)
print(f"Array saved to '{file_path_npy}'")

# np.load() is used to load data from a .npy file.
loaded_arr_npy = np.load(file_path_npy)
print("Loaded Array from .npy file:")
print(loaded_arr_npy)
print(f"Arrays are equal: {np.array_equal(arr_to_save, loaded_arr_npy)}")
print("-" * 30)

# --------------------------------------------------------------------
# 2. Saving Multiple Arrays to a Zipped .npz File
# --------------------------------------------------------------------

# np.savez() saves multiple arrays into a single, uncompressed .npz file.
# The arrays are saved as keyword arguments.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
file_path_npz = 'multiple_arrays.npz'
np.savez(file_path_npz, arr1=arr1, arr2=arr2)
print(f"Multiple arrays saved to '{file_path_npz}'")

# np.load() on an .npz file returns a dictionary-like object.
loaded_npz = np.load(file_path_npz)
print("Keys in the loaded .npz file:", list(loaded_npz.keys()))

# Access the individual arrays using their keyword names
loaded_arr1 = loaded_npz['arr1']
loaded_arr2 = loaded_npz['arr2']
print("Loaded arr1:")
print(loaded_arr1)
print("Loaded arr2:")
print(loaded_arr2)
print("-" * 30)

# --------------------------------------------------------------------
# 3. Saving Multiple Arrays to a Compressed Zipped .npz File
# --------------------------------------------------------------------

# np.savez_compressed() is similar to np.savez() but compresses the file.
file_path_npz_compressed = 'compressed_arrays.npz'
np.savez_compressed(file_path_npz_compressed, arr1=arr1, arr2=arr2)
print(f"Multiple arrays saved to '{file_path_npz_compressed}' (compressed)")

# Loading a compressed .npz file is the same as a regular .npz file
loaded_npz_compressed = np.load(file_path_npz_compressed)
print("Loaded arr1 from compressed file:")
print(loaded_npz_compressed['arr1'])
print("-" * 30)

# --------------------------------------------------------------------
# 4. Saving/Loading to a Text File
# --------------------------------------------------------------------

# np.savetxt() saves an array to a plain text file.
# This is useful for sharing data with non-NumPy applications.
file_path_txt = 'my_array.txt'
np.savetxt(file_path_txt, arr_to_save, delimiter=',', fmt='%.2f')
print(f"Array saved to '{file_path_txt}' as text.")

# np.loadtxt() is used to load data from a text file.
loaded_arr_txt = np.loadtxt(file_path_txt, delimiter=',')
print("Loaded Array from .txt file:")
print(loaded_arr_txt)
print("-" * 30)

# --------------------------------------------------------------------
# 5. Summary and Best Practices
# --------------------------------------------------------------------

# - For saving a single array: Use np.save() for speed and fidelity.
# - For saving multiple arrays: Use np.savez() or np.savez_compressed()
#   to keep related data together in one file.
# - For interoperability: Use np.savetxt() for simple, human-readable text
#   files that can be opened in other software (e.g., spreadsheets).
#
# Remember to clean up the created files after your work is done!
# You can use the 'os' module to do this.
import os
os.remove(file_path_npy)
os.remove(file_path_npz)
os.remove(file_path_npz_compressed)
os.remove(file_path_txt)
print("Cleaned up created files.")
