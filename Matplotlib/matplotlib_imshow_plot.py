# The `imshow()` function in Matplotlib is used to display data as an image.
# It's particularly useful for visualizing 2D arrays, such as heatmaps or images.

import matplotlib.pyplot as plt
import numpy as np

# --- 1. Basic Usage: Plotting a 2D array ---

# Create a sample 2D array (e.g., a simple gradient)
data = np.random.rand(10, 10)

# `imshow()` takes a 2D array and displays it.
# The `cmap` argument specifies the colormap (e.g., 'viridis', 'hot', 'gray').
# The default origin is 'upper' (row 0 is at the top).
plt.imshow(data, cmap='viridis')

# Add a colorbar to interpret the values.
plt.colorbar(label='Data Value')

# Add a title and labels for clarity.
plt.title("Basic imshow Plot of a 2D Array")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Display the plot.
plt.show()


# --- 2. Customizing the Plot ---

# Create another 2D array for a more complex example.
data_complex = np.zeros((10, 10))
data_complex[2:8, 2:8] = 1 # Create a square in the middle
data_complex[4:6, 4:6] = 2 # Create a smaller square in the center

# `interpolation` controls how the pixels are rendered.
# 'nearest' (default) shows distinct pixels.
# 'bilinear' or 'bicubic' can smooth the image.
# `vmin` and `vmax` set the color limits for the data.
plt.imshow(data_complex, cmap='plasma', interpolation='nearest', vmin=0, vmax=2)
plt.colorbar(label='Value')
plt.title("imshow with Interpolation and Value Limits")
plt.show()


# --- 3. Plotting with Specific Coordinates ---

# `imshow()` can take `extent` to define the coordinates of the image.
# This maps the array to a specific rectangular region in data coordinates.
# The format is [left, right, bottom, top].
x_min, x_max = -5, 5
y_min, y_max = -3, 3

# Create a 2D array for this example.
x = np.linspace(x_min, x_max, 100)
y = np.linspace(y_min, y_max, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

plt.imshow(Z, extent=[x_min, x_max, y_min, y_max], origin='lower', cmap='seismic')

# `origin='lower'` places row 0 at the bottom, which is standard for most plots.
# The default is 'upper' which places row 0 at the top.
plt.colorbar(label='sin(r)')
plt.title("imshow with Custom Extent and Origin")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# --- 4. Displaying a True-Color Image ---

# `imshow()` can also display 3D arrays representing images (e.g., RGB or RGBA).
# The shape should be (M, N, 3) for RGB or (M, N, 4) for RGBA.
# Create a sample RGB image (a 100x100 pixel image with random colors).
# Each pixel has three values for Red, Green, and Blue.
image_data = np.random.rand(100, 100, 3)

plt.imshow(image_data)
plt.title("imshow Plot of an RGB Image")
plt.show()