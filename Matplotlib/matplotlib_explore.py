# Matplotlib is a powerful plotting library for Python.
# Its object-oriented structure is built around a few key concepts:
# 1. Figure: The entire window or page that contains everything.
# 2. Axes: The actual plot area where data is drawn. A figure can have multiple axes.
# 3. Artist: Everything you can see on the figure, like lines, titles, and labels.

import matplotlib.pyplot as plt
import numpy as np

# --- 1. The Basic Workflow: Figure and Axes ---

# This is the most common way to start a plot. `plt.subplots()`
# creates a Figure and a single Axes object simultaneously.
# 'fig' is the figure, 'ax' is the axes (the plot itself).
fig, ax = plt.subplots(figsize=(8, 6))

# Generate sample data for plotting.
x = np.linspace(0, 10, 100)
y = np.sin(x)

# --- 2. Plotting Data ---

# `ax.plot()` is a method of the Axes object to plot data.
# You can customize it with various parameters.
ax.plot(x, y, label='sin(x)', color='blue', linestyle='--', linewidth=2, marker='o', markersize=5)

# Matplotlib supports many other plot types:
# `ax.scatter()`: For scatter plots.
# `ax.bar()`: For bar charts.
# `ax.hist()`: For histograms.
# `ax.imshow()`: For displaying 2D data as images.
# `ax.boxplot()`: For box plots.

# --- 3. Customizing the Plot ---

# Titles and Labels
ax.set_title("A Simple Matplotlib Plot", fontsize=16, fontweight='bold')
ax.set_xlabel("X-axis Label", fontsize=12)
ax.set_ylabel("Y-axis Label", fontsize=12)

# Axis Limits
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)

# Legend and Grid
# The `label` from `ax.plot()` is used here.
ax.legend(loc='upper right', frameon=True)
ax.grid(True, linestyle=':', alpha=0.6)

# --- 4. Subplots: Multiple Plots in One Figure ---

# `plt.subplots(nrows, ncols)` is used to create a grid of plots.
# 'axs' is a NumPy array of Axes objects.
fig_multi, axs = plt.subplots(2, 2, figsize=(10, 8))

# Access each subplot using array indexing.
axs[0, 0].plot(x, np.cos(x), color='red')
axs[0, 0].set_title('Top Left: cos(x)')

axs[0, 1].scatter(x, np.exp(y), color='green')
axs[0, 1].set_title('Top Right: Scatter')

axs[1, 0].hist(np.random.randn(100), bins=15)
axs[1, 0].set_title('Bottom Left: Histogram')

axs[1, 1].plot(x, x, color='purple')
axs[1, 1].set_title('Bottom Right: Linear')

# `plt.tight_layout()` adjusts subplot parameters for a clean layout.
plt.tight_layout()
plt.show()

# --- 5. Saving the Plot ---
# You can save a plot to a file instead of displaying it.
# `dpi` sets the resolution.
# fig.savefig('my_plot.png', dpi=300)