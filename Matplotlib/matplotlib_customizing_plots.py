import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import font_manager as fm, rcParams # For font customization

print("--- Matplotlib Customizing Plots: All About in Code ---")

# --- 1. Figure and Axes Level Customization ---
print("\n--- 1. Figure and Axes Level Customization ---")

# 1.1 Figure Size and DPI
print("\n--- 1.1 Figure Size and DPI ---")
# `figsize`: (width, height) in inches.
# `dpi`: dots per inch (resolution of the output).
plt.figure(figsize=(10, 6), dpi=100) # Default is usually (6.4, 4.8)
x = np.linspace(0, 10, 50)
y = np.sin(x)
plt.plot(x, y)
plt.title("Custom Figure Size and DPI")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


# 1.2 Facecolor (Background Color)
print("\n--- 1.2 Facecolor (Background Color) ---")
fig = plt.figure(figsize=(8, 5), facecolor='#F0F0F0') # Light grey background
ax = fig.add_subplot(111) # Get the axes
ax.plot(x, y, color='darkgreen', linestyle='-', linewidth=2)
ax.set_facecolor('#E6EEF4') # Light blue background for the plot area
ax.set_title("Custom Facecolors for Figure and Axes")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
plt.show()


# --- 2. Line Properties ---
print("\n--- 2. Line Properties ---")
x_line = np.linspace(0, 2 * np.pi, 100)
y_line_sin = np.sin(x_line)
y_line_cos = np.cos(x_line)

plt.figure(figsize=(9, 6))
plt.plot(x_line, y_line_sin,
         color='purple',        # Hex color code or name
         linestyle='--',        # '--', ':', '-.', '-'
         linewidth=2.5,         # Thickness of the line
         marker='o',            # Marker style (e.g., 'o', 'x', '^', 's', '*')
         markersize=7,          # Size of the marker
         markeredgecolor='black', # Marker edge color
         markerfacecolor='white', # Marker fill color
         alpha=0.7,             # Transparency
         label='Sine Wave')

plt.plot(x_line, y_line_cos,
         color='darkorange',
         linestyle=':',
         linewidth=1.5,
         marker='D',
         markersize=5,
         markeredgecolor='darkorange',
         markerfacecolor='darkorange',
         alpha=0.6,
         label='Cosine Wave')

plt.title("Line Plot Customization")
plt.xlabel("Angle (radians)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True, linestyle='-', alpha=0.5)
plt.show()


# --- 3. Text Properties (Titles, Labels, Legends) ---
print("\n--- 3. Text Properties (Titles, Labels, Legends) ---")

plt.figure(figsize=(8, 6))
plt.plot(x, y, color='blue')

# 3.1 Titles
plt.title("Plot Title Example",
          fontsize=16,          # Font size
          color='navy',         # Font color
          fontweight='bold',    # 'normal', 'bold', 'light', 'heavy'
          fontfamily='serif',   # 'serif', 'sans-serif', 'monospace', etc.
          loc='center',         # 'left', 'center', 'right'
          pad=15)               # Padding from the top edge

# 3.2 Axis Labels
plt.xlabel("Independent Variable", fontsize=12, color='darkgreen', labelpad=10)
plt.ylabel("Dependent Variable", fontsize=12, color='darkred', labelpad=10)

# 3.3 Legend
# Add a dummy plot for legend to appear
plt.plot([], [], color='blue', label='Data Series 1')
plt.plot([], [], color='red', label='Data Series 2') # Another dummy for demonstration

plt.legend(loc='upper right',      # Location of the legend
           fontsize=10,            # Font size
           facecolor='lightyellow', # Background color of the legend box
           edgecolor='gray',       # Border color
           frameon=True,           # Whether to draw a frame around the legend
           shadow=True,            # Add shadow
           ncols=1,                # Number of columns for legend entries
           title='My Data Legend') # Title for the legend box

plt.show()

# 3.4 Annotations and Text
plt.figure(figsize=(8, 6))
plt.scatter(x_scatter, y_scatter, color='teal', alpha=0.7) # Assume x_scatter, y_scatter from earlier examples

# Add specific text
plt.text(2, 8, "Important Point!",
         fontsize=14, color='red', weight='bold',
         bbox=dict(boxstyle="round,pad=0.5", fc="yellow", ec="red", lw=2, alpha=0.8), # Bounding box
         ha='center', va='center') # Horizontal/Vertical alignment

# Add annotation with arrow
plt.annotate('Outlier!', xy=(9, 25), xytext=(7, 20),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
             fontsize=12, color='darkblue')
plt.title("Annotations and Text on Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()


# --- 4. Axis Ticks and Limits ---
print("\n--- 4. Axis Ticks and Limits ---")

x_ticks = np.linspace(0, 10, 100)
y_ticks = np.sin(x_ticks) * 100 + 500 # Scale y for larger numbers

plt.figure(figsize=(9, 6))
plt.plot(x_ticks, y_ticks, color='darkviolet')

# 4.1 Setting Axis Limits
plt.xlim(-1, 11)   # Set x-axis limits
plt.ylim(300, 700) # Set y-axis limits

# 4.2 Custom Tick Locations and Labels
plt.xticks(np.arange(0, 11, 2),    # Set x-tick locations
           labels=['Start', '2', '4', '6', '8', 'End']) # Custom labels for x-ticks
plt.yticks(np.arange(300, 701, 100)) # Set y-tick locations

# 4.3 Tick Label Properties
ax = plt.gca() # Get current axes
ax.tick_params(axis='x', rotation=45, colors='red', labelsize=10) # Rotate x-tick labels, change color, size
ax.tick_params(axis='y', length=6, width=2, colors='blue', labelsize=10) # Change tick length, width, color

plt.title("Custom Axis Ticks and Limits")
plt.xlabel("Time Period")
plt.ylabel("Value Range")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# 4.4 Logarithmic Scales
print("\n--- 4.4 Logarithmic Scales ---")
x_log = np.logspace(0, 2, 100) # 10^0 to 10^2
y_log = x_log**2

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(x_log, y_log)
plt.xscale('linear')
plt.yscale('linear')
plt.title("Linear Scale")
plt.xlabel("X")
plt.ylabel("Y")

plt.subplot(1, 2, 2)
plt.plot(x_log, y_log)
plt.xscale('log') # Logarithmic x-axis
plt.yscale('log') # Logarithmic y-axis
plt.title("Logarithmic Scale")
plt.xlabel("X (log scale)")
plt.ylabel("Y (log scale)")

plt.tight_layout()
plt.show()


# --- 5. Spines (Borders of the Plot) ---
print("\n--- 5. Spines (Borders of the Plot) ---")
# You can hide or customize the lines forming the plot boundaries.
fig_spines, ax_spines = plt.subplots(figsize=(7, 5))
ax_spines.plot(x, y, color='darkcyan', linewidth=2)

# Hide top and right spines
ax_spines.spines['top'].set_visible(False)
ax_spines.spines['right'].set_visible(False)

# Customize bottom and left spines
ax_spines.spines['bottom'].set_color('blue')
ax_spines.spines['bottom'].set_linewidth(2)
ax_spines.spines['left'].set_color('red')
ax_spines.spines['left'].set_linewidth(2)

# Move spines (e.g., to the origin)
# ax_spines.spines['left'].set_position(('data', 0))
# ax_spines.spines['bottom'].set_position(('data', 0))

ax_spines.set_title("Customized Spines")
ax_spines.set_xlabel("X-axis")
ax_spines.set_ylabel("Y-axis")
plt.show()


# --- 6. Colormaps (for heatmaps, scatter plots with 'c' param) ---
print("\n--- 6. Colormaps ---")
# Colormaps map scalar values to colors.
# https://matplotlib.org/stable/users/explain/colors/colormaps.html

data_2d = np.random.rand(10, 10) # 10x10 array of random values

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(data_2d, cmap='viridis', origin='lower') # 'viridis' is perceptually uniform
plt.colorbar(label='Value')
plt.title("Colormap: Viridis")

plt.subplot(1, 2, 2)
plt.imshow(data_2d, cmap='coolwarm', origin='lower') # 'coolwarm' is diverging
plt.colorbar(label='Value')
plt.title("Colormap: Coolwarm")

plt.tight_layout()
plt.show()


# --- 7. Saving Plots ---
print("\n--- 7. Saving Plots ---")
print("Beyond just displaying, you can save plots in various formats.")
plt.figure(figsize=(8, 5))
plt.plot(x, y, color='magenta')
plt.title("Plot to be Saved")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

# 7.1 Saving as PNG (raster, good for web)
plt.savefig("my_custom_plot.png")
print("Saved: my_custom_plot.png")

# 7.2 Saving as PDF (vector, good for print/publications)
plt.savefig("my_custom_plot.pdf")
print("Saved: my_custom_plot.pdf")

# 7.3 Custom DPI and Transparent Background
plt.savefig("my_custom_plot_high_res.png", dpi=300, transparent=True)
print("Saved: my_custom_plot_high_res.png (300dpi, transparent)")

# Close the plot figure after saving to free memory if not needed further
plt.close()


# --- 8. Using Style Sheets ---
print("\n--- 8. Using Style Sheets ---")
print("Matplotlib comes with several pre-defined style sheets.")
print("You can also create your own. This is a quick way to change aesthetics.")

print(f"Available styles: {plt.style.available}")

# Use a specific style temporarily (within a 'with' block)
with plt.style.context('seaborn-v0_8-darkgrid'):
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label='Sine Wave')
    plt.plot(x, np.cos(x), label='Cosine Wave')
    plt.title("Plot with 'seaborn-v0_8-darkgrid' Style")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

# Set a style globally (affects all plots after this)
# plt.style.use('ggplot')
# print("\nGlobally set 'ggplot' style. All subsequent plots will use it.")
# You would then plot something to see the effect.
# Remember to reset with `plt.style.use('default')` if needed.


print("\n--- End of Matplotlib Customizing Plots Practice Code ---")

# General Tips for Customization:
# - Always prefer using the Axes object methods (e.g., `ax.set_title()`, `ax.set_xlabel()`, `ax.plot()`)
#   when working with `fig, ax = plt.subplots()`, as it gives more precise control over which subplot you're affecting.
# - Experiment with different parameters. The Matplotlib documentation is very extensive.
# - For consistent styling across multiple plots, consider using style sheets or setting global rcParams.