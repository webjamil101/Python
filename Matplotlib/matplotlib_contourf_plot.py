import matplotlib.pyplot as plt
import numpy as np

# --- 1. Basic `contourf` plot with simple data ---

# Create a grid of x and y values
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)

# Define a function z = f(x, y) for the contour plot
Z = np.sin(X**2 + Y**2)

# Create a figure and axes for the plot
fig, ax = plt.subplots()

# Use `contourf` to create a filled contour plot
# `levels` can be an integer for number of levels, or an array of specific values.
# `cmap` sets the colormap.
c = ax.contourf(X, Y, Z, levels=20, cmap='viridis')

# Add a color bar to show the mapping of values to colors
fig.colorbar(c, ax=ax, label='Z value')

# Set plot title and labels
ax.set_title('Basic `contourf` Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Display the plot
plt.show()

# --- 2. Customizing `contourf` with specific levels and a different colormap ---

# Create new data
x_custom = np.linspace(-2, 2, 50)
y_custom = np.linspace(-2, 2, 50)
X_custom, Y_custom = np.meshgrid(x_custom, y_custom)
Z_custom = np.exp(-X_custom**2 - Y_custom**2)

# Define custom levels for the contour plot
custom_levels = [0.1, 0.2, 0.4, 0.6, 0.8, 1.0]

fig, ax = plt.subplots()

# `extend` can be 'both', 'min', or 'max' to indicate data outside the range of `levels`.
# `origin` can be 'upper', 'lower', or 'image'.
# `antialiased` can be True or False to smooth the contours.
c = ax.contourf(X_custom, Y_custom, Z_custom, levels=custom_levels, cmap='plasma', extend='both')

fig.colorbar(c, ax=ax, label='Z value')
ax.set_title('Custom `contourf` Plot with Specific Levels')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
plt.show()

# --- 3. Combining `contourf` with `contour` for clearer boundaries ---

# Use the same data as the first example
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X**2 + Y**2)

fig, ax = plt.subplots()

# Plot the filled contours
c_filled = ax.contourf(X, Y, Z, levels=15, cmap='viridis')

# Plot the contour lines on top of the filled contours
# The `colors` argument can be a single color or a list. Here we use black lines.
# `linewidths` controls the thickness of the lines.
c_lines = ax.contour(X, Y, Z, levels=15, colors='black', linewidths=0.5)

# Add a color bar
fig.colorbar(c_filled, ax=ax, label='Z value')

# You can also add labels to the contour lines
ax.clabel(c_lines, inline=True, fontsize=8)

ax.set_title('`contourf` with `contour` for Boundaries')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
plt.show()