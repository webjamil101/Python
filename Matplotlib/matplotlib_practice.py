import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print("--- Matplotlib Practice: All About in Code ---")

# --- 1. Basic Plotting (Line Plot) ---
print("\n--- 1. Basic Plotting (Line Plot) ---")
# The simplest way to plot data.
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 1, 5, 3])

plt.figure(figsize=(6, 4)) # Create a new figure with a specific size
plt.plot(x, y) # Plot x vs y
plt.title("Simple Line Plot") # Add a title
plt.xlabel("X-axis Label")    # Add x-axis label
plt.ylabel("Y-axis Label")    # Add y-axis label
plt.grid(True)                # Add a grid
plt.show()                    # Display the plot

# Adding multiple lines to the same plot
x_multi = np.linspace(0, 10, 100) # 100 points between 0 and 10
y_sin = np.sin(x_multi)
y_cos = np.cos(x_multi)

plt.figure(figsize=(8, 5))
plt.plot(x_multi, y_sin, label='Sine Wave', color='blue', linestyle='--') # Custom color and linestyle
plt.plot(x_multi, y_cos, label='Cosine Wave', color='red', marker='.') # Custom color and marker
plt.title("Sine and Cosine Waves")
plt.xlabel("Angle (radians)")
plt.ylabel("Amplitude")
plt.legend() # Show the legend based on 'label' arguments
plt.grid(True)
plt.show()


# --- 2. Scatter Plot ---
print("\n--- 2. Scatter Plot ---")
# Used to show the relationship between two numerical variables.
np.random.seed(42) # for reproducibility
num_points = 50
x_scatter = np.random.rand(num_points) * 10
y_scatter = np.random.rand(num_points) * 10 + x_scatter
colors = np.random.rand(num_points)
sizes = np.random.rand(num_points) * 500 # Marker sizes

plt.figure(figsize=(7, 6))
plt.scatter(x_scatter, y_scatter, c=colors, s=sizes, alpha=0.7, cmap='viridis', edgecolors='black')
plt.colorbar(label='Color intensity') # Add a color bar
plt.title("Scatter Plot with Color and Size Variation")
plt.xlabel("Feature X")
plt.ylabel("Feature Y")
plt.grid(True)
plt.show()


# --- 3. Bar Chart ---
print("\n--- 3. Bar Chart ---")
# Used to display categorical data with rectangular bars.
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 12, 39]

plt.figure(figsize=(7, 5))
plt.bar(categories, values, color=['skyblue', 'lightcoral', 'lightgreen', 'gold', 'plum'])
plt.title("Bar Chart of Categories")
plt.xlabel("Category")
plt.ylabel("Value")
plt.ylim(0, 60) # Set y-axis limits
plt.show()

# Horizontal Bar Chart
plt.figure(figsize=(7, 5))
plt.barh(categories, values, color='salmon')
plt.title("Horizontal Bar Chart")
plt.xlabel("Value")
plt.ylabel("Category")
plt.xlim(0, 60)
plt.show()


# --- 4. Histogram ---
print("\n--- 4. Histogram ---")
# Used to visualize the distribution of a single numerical variable.
data_hist = np.random.randn(1000) # Standard normal distribution
plt.figure(figsize=(8, 5))
plt.hist(data_hist, bins=30, color='lightblue', edgecolor='black', alpha=0.7)
plt.title("Histogram of Random Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(axis='y', alpha=0.75)
plt.show()


# --- 5. Pie Chart ---
print("\n--- 5. Pie Chart ---")
# Used to show proportions of a whole.
labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0) # explode the 2nd slice (Hogs)

plt.figure(figsize=(7, 7))
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, colors=plt.cm.Paired.colors) # Using a colormap
plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Pie Chart of Animal Proportions")
plt.show()


# --- 6. Subplots ---
print("\n--- 6. Subplots ---")
# Arranging multiple plots in a grid.
# `plt.subplot(nrows, ncols, index)` or `plt.subplots(nrows, ncols)`

fig, axes = plt.subplots(2, 2, figsize=(10, 8)) # 2 rows, 2 columns of subplots

# Plot 1: Top-left
axes[0, 0].plot(x, y, 'go-') # 'g' green, 'o' circle marker, '-' solid line
axes[0, 0].set_title("Plot 1: Line")
axes[0, 0].set_xlabel("X")
axes[0, 0].set_ylabel("Y")

# Plot 2: Top-right
axes[0, 1].scatter(x_scatter, y_scatter, color='purple', alpha=0.6)
axes[0, 1].set_title("Plot 2: Scatter")

# Plot 3: Bottom-left
axes[1, 0].bar(categories, values, color='teal')
axes[1, 0].set_title("Plot 3: Bar")

# Plot 4: Bottom-right
axes[1, 1].hist(data_hist, bins=20, color='orange', edgecolor='brown')
axes[1, 1].set_title("Plot 4: Histogram")

plt.tight_layout() # Adjusts subplot params for a tight layout
plt.suptitle("Multiple Subplots Example", y=1.02, fontsize=16) # Super title for the entire figure
plt.show()


# --- 7. Customizing Plots ---
print("\n--- 7. Customizing Plots ---")

# 7.1 Line Styles, Colors, Markers
plt.figure(figsize=(8, 5))
plt.plot(x_multi, np.sin(x_multi), 'r--', label='Red Dashed') # Shorthand 'r--'
plt.plot(x_multi, np.cos(x_multi), 'b:o', label='Blue Dotted with Circles') # Shorthand 'b:o'
plt.plot(x_multi, np.tan(x_multi / 10), color='#8A2BE2', linestyle='-.', marker='x',
         linewidth=2, markersize=5, label='Custom Hex Color')
plt.title("Custom Line Styles, Colors, Markers")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()

# 7.2 Text and Annotations
plt.figure(figsize=(7, 5))
plt.plot(x, y, 'o-')
plt.title("Plot with Annotations")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.annotate('Peak!', xy=(4, 5), xytext=(4.5, 4),
             arrowprops=dict(facecolor='black', shrink=0.05),
             bbox=dict(boxstyle="round,pad=0.3", fc="yellow", ec="red", lw=2, alpha=0.8),
             fontsize=12)
plt.text(1.5, 4.5, "Some Text Here", fontsize=10, color='gray', ha='center')
plt.show()

# 7.3 Axis Limits and Ticks
plt.figure(figsize=(7, 5))
plt.plot(x_multi, y_sin)
plt.title("Custom Axis Limits and Ticks")
plt.xlabel("X")
plt.ylabel("Y")
plt.xlim(0, 5) # Set x-axis limits
plt.ylim(-0.5, 1.0) # Set y-axis limits
plt.xticks(np.arange(0, 5.1, 1)) # Custom x-ticks every 1 unit
plt.yticks([-0.5, 0, 0.5, 1.0]) # Custom y-ticks
plt.show()

# 7.4 Colormaps
print("\n--- 7.4 Colormaps ---")
# Useful for visualizing a third dimension in 2D plots (e.g., scatter, imshow)
gradient_data = np.random.rand(10, 10)
plt.figure(figsize=(7, 6))
plt.imshow(gradient_data, cmap='coolwarm', origin='lower') # origin='lower' puts (0,0) at bottom-left
plt.colorbar(label='Value')
plt.title("Image Plot with Colormap")
plt.show()


# --- 8. 3D Plotting (Basic) ---
print("\n--- 8. 3D Plotting (Basic) ---")
# Requires `mpl_toolkits.mplot3d`
from mpl_toolkits.mplot3d import Axes3D

# 3D Scatter Plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d') # Create a 3D subplot

z_scatter = np.random.rand(num_points) * 10
ax.scatter(x_scatter, y_scatter, z_scatter, c=z_scatter, cmap='plasma')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title("3D Scatter Plot")
plt.show()

# 3D Surface Plot
X_surface = np.arange(-5, 5, 0.25)
Y_surface = np.arange(-5, 5, 0.25)
X_surface, Y_surface = np.meshgrid(X_surface, Y_surface)
R = np.sqrt(X_surface**2 + Y_surface**2)
Z_surface = np.sin(R)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X_surface, Y_surface, Z_surface, cmap='viridis', edgecolor='none')
ax.set_title("3D Surface Plot")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()


# --- 9. Saving Plots ---
print("\n--- 9. Saving Plots ---")
# `plt.savefig()` allows you to save plots to various formats.
# Create a dummy plot to save
plt.figure(figsize=(6, 4))
plt.plot(x, y, 'ro-')
plt.title("Plot to be Saved")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

# 9.1 Saving as PNG (raster image)
plt.savefig("saved_plot.png")
print("Plot saved as 'saved_plot.png'")

# 9.2 Saving as PDF (vector image - good for publications)
plt.savefig("saved_plot.pdf")
print("Plot saved as 'saved_plot.pdf'")

# 9.3 Saving with custom DPI and transparent background
plt.savefig("saved_plot_high_res.png", dpi=300, transparent=True)
print("Plot saved as 'saved_plot_high_res.png' (high res, transparent)")

plt.close() # Close the current figure to free memory

print("\n--- End of Matplotlib Practice Code ---")

# Note: In an interactive environment (like Jupyter Notebook),
# `plt.show()` renders the plot. In a script, it opens a non-blocking window.
# If you run this script, multiple plot windows will appear and close.
# In a Jupyter notebook, the plots will be displayed inline.