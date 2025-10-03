# ====================================================================
# NumPy Saving and Loading with Text Files
# ====================================================================

import numpy as np
import os

# Create a sample 2D array to demonstrate saving and loading
data_to_save = np.array([[1.123, 2.345, 3.567],
                         [4.789, 5.901, 6.012],
                         [7.234, 8.456, 9.678]])
print("Original Array to be Saved:")
print(data_to_save)
print("-" * 30)

# --------------------------------------------------------------------
# 1. Saving an Array to a Text File with np.savetxt()
# --------------------------------------------------------------------

# np.savetxt() saves an array to a text file.
# Key parameters:
# - fname: The file path.
# - X: The array to be saved.
# - delimiter: The string used to separate values. Common choices are ',', ' ', '\t'.
# - fmt: The format string for writing the values (e.g., '%.3f' for 3 decimal places).
file_path_txt = 'my_numpy_data.txt'
np.savetxt(file_path_txt, data_to_save, delimiter=',', fmt='%.3f')
print(f"Array successfully saved to '{file_path_txt}' as a CSV file.")
print("-" * 30)

# --------------------------------------------------------------------
# 2. Loading an Array from a Text File with np.loadtxt()
# --------------------------------------------------------------------

# np.loadtxt() loads data from a text file into a NumPy array.
# Key parameters:
# - fname: The file path.
# - delimiter: The string that separates the values in the file. It must match
#              the delimiter used in np.savetxt().
loaded_data = np.loadtxt(file_path_txt, delimiter=',')
print("Loaded Array from the text file:")
print(loaded_data)
print("-" * 30)

# --------------------------------------------------------------------
# 3. Verification and Cleanup
# --------------------------------------------------------------------

# We can verify that the loaded data is the same as the original data.
# Note that floating point precision might be a factor, but for this
# example, it should be fine.
print(f"Original and loaded arrays are equal: {np.allclose(data_to_save, loaded_data)}")

# Clean up the file created for this example
os.remove(file_path_txt)
print(f"Cleaned up the file '{file_path_txt}'.")
