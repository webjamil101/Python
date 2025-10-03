import matplotlib.pyplot as plt
import numpy as np

# A single Matplotlib `Figure` can contain one or more `Axes` objects,
# which are the individual plots. Plotting on the "same figure"
# typically means using a single `Axes` object to plot multiple data series,
# or using multiple `Axes` objects within a single `Figure` (sub-plots).

# --- 1. Plotting multiple lines on a single Axes object ---

# Create sample data for two different lines.
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure and a single axes object.
fig, ax = plt.subplots(figsize=(8, 5))

# Plot both datasets on the same axes.
# Each call to `ax.plot()` adds a new line to the same plot area.
ax.plot(x, y1, label='sin(x)', color='blue')
ax.plot(x, y2, label='cos(x)', color='red', linestyle='--')

# Add a legend to differentiate the lines.
ax.legend()
ax.set_title('Multiple Lines on a Single Axes')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.grid(True)
plt.show()


# --- 2. Plotting multiple subplots on the same Figure ---

# Create sample data for two separate plots.
x_data = np.arange(10)
y_scatter = x_data**2
y_bar = x_data * 3

# `plt.subplots()` can create a grid of axes objects.
# Here, we create a 1x2 grid of plots (1 row, 2 columns).
# `axs` will be an array-like object containing the two axes.
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

# Plot on the first axes (left subplot).
axs[0].plot(x_data, y_scatter, marker='o', linestyle='-')
axs[0].set_title('Subplot 1: Line Plot')
axs[0].set_xlabel('X-values')
axs[0].set_ylabel('Y-values')

# Plot on the second axes (right subplot).
axs[1].bar(x_data, y_bar, color='green')
axs[1].set_title('Subplot 2: Bar Plot')
axs[1].set_xlabel('X-values')
axs[1].set_ylabel('Y-values')

# `plt.tight_layout()` adjusts subplot params to give a tight layout.
fig.suptitle('Multiple Subplots on a Single Figure')
plt.tight_layout()
plt.show()


# --- 3. Mixing plot types on a single Axes ---

# It's also possible to plot different types of charts on the same axes.
fig, ax = plt.subplots(figsize=(8, 5))

# Plot a line
ax.plot(x, y1, label='sin(x)', color='blue')

# Plot a scatter plot on top of the line plot.
ax.scatter(x[::10], y1[::10], color='red', s=50, label='Sample points')

ax.legend()
ax.set_title('Mixed Plot Types on a Single Axes')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# --- 1. Create a simple 2x2 grid of subplots ---

# `plt.subplots(nrows, ncols, ...)` creates a figure and a grid of axes.
# `fig` is the figure object.
# `axs` is a NumPy array of axes objects, shaped as (nrows, ncols).
# Here, we get a 2x2 array of axes.
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# `axs` is a 2D array, so we can access each subplot using standard NumPy indexing.
# For example, `axs[0, 0]` is the top-left subplot.
axs[0, 0].plot(np.random.rand(10))
axs[0, 0].set_title('Top Left')

axs[0, 1].scatter(np.random.rand(10), np.random.rand(10))
axs[0, 1].set_title('Top Right')

axs[1, 0].hist(np.random.randn(100), bins=15)
axs[1, 0].set_title('Bottom Left')

axs[1, 1].boxplot(np.random.rand(10, 5))
axs[1, 1].set_title('Bottom Right')

# `fig.suptitle()` adds a title to the entire figure.
fig.suptitle('Figure with 2x2 Subplots')

# `plt.tight_layout()` automatically adjusts subplot parameters
# to give a tight layout, preventing titles and labels from overlapping.
plt.tight_layout()
plt.show()

# --- 2. Create a single row or column of subplots ---

# A 1x3 grid (1 row, 3 columns).
# `axs` will be a 1D array of 3 axes.
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

x = np.linspace(0, 2 * np.pi, 100)

# Access the subplots using a single index.
axs[0].plot(x, np.sin(x))
axs[0].set_title('sin(x)')

axs[1].plot(x, np.cos(x))
axs[1].set_title('cos(x)')

axs[2].plot(x, np.tan(x))
axs[2].set_title('tan(x)')

fig.suptitle('1x3 Subplots')
plt.tight_layout()
plt.show()

# --- 3. Sharing axes between subplots ---

# Use `sharex=True` or `sharey=True` to share the x or y-axis limits.
# This is useful for comparing plots with the same scale.
x_data = np.arange(10)
y_data1 = x_data
y_data2 = x_data**2

fig, axs = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

axs[0].plot(x_data, y_data1)
axs[0].set_title('Linear')

axs[1].plot(x_data, y_data2, color='red')
axs[1].set_title('Quadratic')

# The x-axis is only labeled on the bottom subplot to avoid redundancy.
axs[1].set_xlabel('Common X-axis')

fig.suptitle('Subplots Sharing the X-axis')
plt.tight_layout()
plt.show()

# --- 4. Using `plt.subplot()` for more complex layouts ---

# `plt.subplot(nrows, ncols, index)` is an older method but can be
# useful for non-grid layouts or when adding plots one by one.
fig = plt.figure(figsize=(10, 6))

# The arguments are `nrows`, `ncols`, and `index`.
# The index starts from 1 and goes row-by-row.
ax1 = fig.add_subplot(2, 2, 1) # Top-left
ax1.plot([1, 2, 3])

ax2 = fig.add_subplot(2, 2, 2) # Top-right
ax2.scatter([1, 2, 3], [3, 2, 1])

ax3 = fig.add_subplot(2, 1, 2)  # Occupies the entire bottom row (2 rows, 1 col, index 2)
ax3.hist(np.random.randn(100))

plt.tight_layout()
plt.show()