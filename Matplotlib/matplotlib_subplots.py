import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print("--- Matplotlib Subplots: All About in Code ---")

# --- 1. Basic Subplots using `plt.subplot()` ---
print("\n--- 1. Basic Subplots using `plt.subplot()` ---")
print("`plt.subplot(nrows, ncols, index)` is a quick way to create a grid of plots.")
print("`index` starts from 1 and goes row by row.")

# Generate some data for different plots
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = x**2
y4 = np.exp(-x)

plt.figure(figsize=(10, 8)) # Create a figure to hold the subplots

# Subplot 1 (2 rows, 2 columns, 1st plot)
plt.subplot(2, 2, 1)
plt.plot(x, y1, color='blue')
plt.title("Sine Wave")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

# Subplot 2 (2 rows, 2 columns, 2nd plot)
plt.subplot(2, 2, 2)
plt.plot(x, y2, color='green')
plt.title("Cosine Wave")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

# Subplot 3 (2 rows, 2 columns, 3rd plot)
plt.subplot(2, 2, 3)
plt.plot(x, y3, color='red')
plt.title("X Squared")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

# Subplot 4 (2 rows, 2 columns, 4th plot)
plt.subplot(2, 2, 4)
plt.plot(x, y4, color='purple')
plt.title("Exponential Decay")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

plt.suptitle("Multiple Subplots using plt.subplot()", fontsize=16, y=1.02) # A title for the entire figure
plt.tight_layout(rect=[0, 0.03, 1, 0.98]) # Adjust layout to prevent overlap, leaving space for suptitle
plt.show()


# --- 2. Recommended Way: `plt.subplots()` ---
print("\n--- 2. Recommended Way: `plt.subplots()` ---")
print("`plt.subplots(nrows, ncols)` returns a `figure` object and an `axes` object (or an array of axes objects).")
print("This is generally preferred as it provides more control over individual subplots.")

# Create a 1x2 grid of subplots (1 row, 2 columns)
fig, axes = plt.subplots(1, 2, figsize=(12, 5)) # `axes` will be a 1D NumPy array of Axes objects

# Plot on the first axes (left)
axes[0].scatter(np.random.rand(50), np.random.rand(50) * 10, color='orange', alpha=0.7)
axes[0].set_title("Random Scatter Plot")
axes[0].set_xlabel("X-axis")
axes[0].set_ylabel("Y-axis")
axes[0].grid(True)

# Plot on the second axes (right)
categories = ['P', 'Q', 'R', 'S']
values = [10, 25, 15, 30]
axes[1].bar(categories, values, color='teal')
axes[1].set_title("Categorical Bar Chart")
axes[1].set_xlabel("Category")
axes[1].set_ylabel("Value")
axes[1].grid(axis='y')

fig.suptitle("Subplots using plt.subplots()", fontsize=16, y=1.02)
plt.tight_layout(rect=[0, 0.03, 1, 0.98])
plt.show()

# Example with a 2x3 grid
fig2, axes2 = plt.subplots(2, 3, figsize=(15, 8)) # `axes2` will be a 2D NumPy array of Axes objects

# Flatten the axes array to easily iterate if needed (optional but often convenient)
axes2_flat = axes2.flatten()

# Example: Plotting histograms for different random distributions
distributions = {
    'Normal': np.random.randn(500),
    'Uniform': np.random.rand(500) * 10,
    'Exponential': np.random.exponential(1, 500),
    'Poisson (lambda=3)': np.random.poisson(3, 500),
    'Binomial (n=10, p=0.5)': np.random.binomial(10, 0.5, 500),
    'Beta (a=0.5, b=0.5)': np.random.beta(0.5, 0.5, 500)
}

for i, (dist_name, data) in enumerate(distributions.items()):
    ax = axes2_flat[i] # Get the current axes object from the flattened array
    ax.hist(data, bins=30, color=plt.cm.viridis(i/len(distributions)), edgecolor='black', alpha=0.7)
    ax.set_title(dist_name, fontsize=10)
    ax.tick_params(axis='x', labelsize=8)
    ax.tick_params(axis='y', labelsize=8)
    ax.grid(axis='y', linestyle=':', alpha=0.6)

fig2.suptitle("Various Data Distributions", fontsize=18)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()


# --- 3. Adjusting Subplot Layout (`tight_layout`, `subplots_adjust`) ---
print("\n--- 3. Adjusting Subplot Layout ---")
print("`plt.tight_layout()` automatically adjusts subplot parameters for a tight layout.")
print("`fig.subplots_adjust()` gives manual control over spacing.")

fig_adj, axes_adj = plt.subplots(2, 2, figsize=(10, 8))

# Simulate a plot with long labels to show default overlap
axes_adj[0, 0].plot(x, y1)
axes_adj[0, 0].set_title("Plot with Long Title and Labels")
axes_adj[0, 0].set_xlabel("Very Long X-axis Label to Demonstrate Overlap")
axes_adj[0, 0].set_ylabel("Another Very Long Y-axis Label")

axes_adj[0, 1].plot(x, y2)
axes_adj[1, 0].plot(x, y3)
axes_adj[1, 1].plot(x, y4)

fig_adj.suptitle("Subplots Before and After Tight Layout", fontsize=16)
# If you comment out tight_layout(), you'll see labels might overlap
# plt.tight_layout() # Uncomment this to see the effect
plt.show()

# Manual adjustment (usually after `tight_layout` if fine-tuning is needed)
fig_manual, axes_manual = plt.subplots(2, 2, figsize=(10, 8))
axes_manual[0, 0].plot(x, y1)
axes_manual[0, 1].plot(x, y2)
axes_manual[1, 0].plot(x, y3)
axes_manual[1, 1].plot(x, y4)

# Manual adjustments:
# `left`, `right`, `top`, `bottom`: positions of the edges of the subplots as fractions of figure width/height
# `wspace`: width reserved for blank space between subplots (fraction of total width)
# `hspace`: height reserved for blank space between subplots (fraction of total height)
fig_manual.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0.3, hspace=0.4)
fig_manual.suptitle("Subplots with Manual Adjustment", fontsize=16)
plt.show()


# --- 4. Sharing Axes (`sharex`, `sharey`) ---
print("\n--- 4. Sharing Axes (`sharex`, `sharey`) ---")
print("This is useful when plots share the same x-axis or y-axis scale, reducing redundancy.")

fig_shared, axes_shared = plt.subplots(2, 1, figsize=(9, 7), sharex=True) # Share the x-axis

# Plot 1
axes_shared[0].plot(x, y_sine, color='blue', label='Sine')
axes_shared[0].set_title("Shared X-axis Example: Sine Wave")
axes_shared[0].set_ylabel("Amplitude")
axes_shared[0].legend()
axes_shared[0].grid(True, linestyle=':', alpha=0.7)

# Plot 2
axes_shared[1].plot(x, y_cosine, color='red', label='Cosine')
axes_shared[1].set_title("Shared X-axis Example: Cosine Wave") # Title optional for lower plot
axes_shared[1].set_xlabel("Angle (radians)") # Only the bottom plot needs x-label
axes_shared[1].set_ylabel("Amplitude")
axes_shared[1].legend()
axes_shared[1].grid(True, linestyle=':', alpha=0.7)

plt.tight_layout()
plt.show()

# Example with shared Y-axis
fig_shared_y, axes_shared_y = plt.subplots(1, 2, figsize=(12, 5), sharey=True) # Share the y-axis

# Create some random data for shared Y
data_A = np.random.normal(loc=5, scale=1, size=100)
data_B = np.random.normal(loc=5.5, scale=0.8, size=100)

axes_shared_y[0].hist(data_A, bins=15, color='orange', edgecolor='black', alpha=0.7)
axes_shared_y[0].set_title("Distribution A")
axes_shared_y[0].set_xlabel("Value")
axes_shared_y[0].set_ylabel("Frequency") # Only the left plot needs y-label

axes_shared_y[1].hist(data_B, bins=15, color='darkgreen', edgecolor='black', alpha=0.7)
axes_shared_y[1].set_title("Distribution B")
axes_shared_y[1].set_xlabel("Value")
# No ylabel needed for right plot due to sharey=True

plt.tight_layout()
plt.show()


# --- 5. `add_subplot()` for More Complex Grids / Manual Placement ---
print("\n--- 5. `add_subplot()` for More Complex Grids / Manual Placement ---")
print("For non-uniform grids or mixing `subplot` and `subplots` paradigms.")
print("`fig.add_subplot(nrows, ncols, index)` is an alternative to `plt.subplot()` but called on a figure.")

fig_add = plt.figure(figsize=(10, 8))

ax1 = fig_add.add_subplot(2, 2, 1) # Top-left
ax1.plot(x, y1)
ax1.set_title('Plot 1')

ax2 = fig_add.add_subplot(2, 2, 2) # Top-right
ax2.scatter(np.random.rand(20), np.random.rand(20))
ax2.set_title('Plot 2')

ax3 = fig_add.add_subplot(2, 1, 2) # Bottom row (takes up both columns)
ax3.plot(x, y1 + y2, color='magenta')
ax3.set_title('Plot 3 (Spanning Columns)')

fig_add.suptitle("Complex Subplot Layout with add_subplot", fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()


# --- 6. `GridSpec` for Advanced Layouts ---
print("\n--- 6. `GridSpec` for Advanced Layouts ---")
print("For highly customized subplot layouts, `GridSpec` gives precise control over grid structure.")

from matplotlib.gridspec import GridSpec

fig_gs = plt.figure(figsize=(12, 9))
gs = GridSpec(3, 3) # 3 rows, 3 columns grid

# A main plot spanning across the top row
ax_main = fig_gs.add_subplot(gs[0, :]) # First row, all columns
ax_main.plot(x, np.sin(x) * np.exp(-x/5), color='darkblue')
ax_main.set_title("Main Time Series Plot")
ax_main.set_xlabel("Time")
ax_main.set_ylabel("Value")
ax_main.grid(True)

# A smaller plot in the middle-left
ax_hist1 = fig_gs.add_subplot(gs[1, 0]) # Second row, first column
ax_hist1.hist(np.random.normal(0, 1, 500), bins=20, color='lightgreen', edgecolor='black')
ax_hist1.set_title('Distribution 1', fontsize=10)

# Another smaller plot in the middle-middle
ax_hist2 = fig_gs.add_subplot(gs[1, 1]) # Second row, second column
ax_hist2.hist(np.random.normal(2, 0.5, 500), bins=20, color='skyblue', edgecolor='black')
ax_hist2.set_title('Distribution 2', fontsize=10)

# A scatter plot spanning bottom-right
ax_scatter = fig_gs.add_subplot(gs[1:, 2]) # Second row onwards, last column
ax_scatter.scatter(np.random.rand(50), np.random.rand(50))
ax_scatter.set_title('Scatter Plot', fontsize=10)

# A heatmap/imshow in the bottom-left
ax_heatmap = fig_gs.add_subplot(gs[2, 0]) # Third row, first column
data_heatmap = np.random.rand(10, 10)
im = ax_heatmap.imshow(data_heatmap, cmap='hot', origin='lower')
ax_heatmap.set_title('Heatmap', fontsize=10)
fig_gs.colorbar(im, ax=ax_heatmap, fraction=0.046, pad=0.04) # Add colorbar to specific axes

# A box plot in the bottom-middle
ax_boxplot = fig_gs.add_subplot(gs[2, 1]) # Third row, second column
data_boxplot = [np.random.normal(0, 1, 100), np.random.normal(1, 0.5, 100)]
ax_boxplot.boxplot(data_boxplot, labels=['Group 1', 'Group 2'])
ax_boxplot.set_title('Box Plot', fontsize=10)


fig_gs.suptitle("Advanced Layout with GridSpec", fontsize=18)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()


print("\n--- End of Matplotlib Subplots Practice Code ---")

# Key takeaways:
# - `plt.subplot()` is quick for simple, uniform grids.
# - `plt.subplots()` is recommended: returns `fig` and `axes` objects for better control.
# - `axes` object methods (e.g., `ax.set_title()`, `ax.plot()`) are used instead of `plt` functions.
# - `plt.tight_layout()` helps prevent overlap.
# - `sharex`/`sharey` are useful for aligning axes.
# - `GridSpec` for highly customized, non-uniform layouts.

# --- 1. Creating a Figure and a single Subplot ---

# `plt.subplots()` is the most common way to create a figure and axes.
# It returns a tuple: `fig` (the container) and `ax` (the subplot).
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot([1, 2, 3], [1, 4, 9])
ax.set_title("Single Subplot")
plt.show()

# --- 2. Creating a Grid of Subplots ---

# `plt.subplots(nrows, ncols)` creates a grid.
# `axs` is a 2D NumPy array of axes objects.
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle("Grid of 2x2 Subplots")

# Access subplots using row and column indexing.
axs[0, 0].plot(np.random.rand(10), color='red')
axs[0, 0].set_title("Top Left")

axs[0, 1].scatter(np.random.rand(10), np.random.rand(10), color='green')
axs[0, 1].set_title("Top Right")

axs[1, 0].hist(np.random.randn(100), bins=15, color='blue')
axs[1, 0].set_title("Bottom Left")

axs[1, 1].boxplot(np.random.rand(10, 5))
axs[1, 1].set_title("Bottom Right")

# `plt.tight_layout()` adjusts spacing to prevent labels from overlapping.
plt.tight_layout()
plt.show()

# --- 3. Creating Subplots in a Single Row or Column ---

# A 1x3 grid returns a 1D array of axes objects.
fig, axs = plt.subplots(1, 3, figsize=(15, 4))
fig.suptitle("Three Subplots in a Row")

x = np.linspace(0, 10, 100)
axs[0].plot(x, np.sin(x), color='red')
axs[0].set_title("sin(x)")

axs[1].plot(x, np.cos(x), color='green')
axs[1].set_title("cos(x)")

axs[2].plot(x, np.tan(x), color='blue')
axs[2].set_title("tan(x)")

plt.tight_layout()
plt.show()

# --- 4. Sharing Axes ---

# `sharex=True` or `sharey=True` ensures subplots share the same axis limits.
fig, axs = plt.subplots(2, 1, sharex=True, figsize=(6, 8))
fig.suptitle("Subplots Sharing X-axis")

axs[0].plot(x, y=np.sin(x))
axs[0].set_title("Plot 1")
axs[0].set_ylabel("Amplitude")

axs[1].plot(x, y=np.cos(x))
axs[1].set_title("Plot 2")
axs[1].set_xlabel("Time")
axs[1].set_ylabel("Amplitude")

plt.tight_layout()
plt.show()

# --- 5. Older Method: `plt.subplot()` ---

# `plt.subplot(nrows, ncols, index)` adds a single subplot to the current figure.
# Index starts from 1.
fig = plt.figure(figsize=(10, 6))
ax1 = plt.subplot(2, 2, 1) # Top-left
ax1.plot([1, 2], [1, 2])

ax2 = plt.subplot(2, 2, 2) # Top-right
ax2.scatter([1, 2], [2, 1])

ax3 = plt.subplot(2, 1, 2)  # Bottom, spans two columns
ax3.bar(['A', 'B'], [10, 20])

plt.tight_layout()
plt.show()