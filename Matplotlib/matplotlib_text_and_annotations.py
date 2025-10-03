import matplotlib.pyplot as plt
import numpy as np

print("--- Matplotlib Text and Annotations: All About in Code ---")

# --- 1. Basic Text (`plt.text()` or `ax.text()`) ---
print("\n--- 1. Basic Text ---")
print("`plt.text(x, y, s, **kwargs)` adds text at an arbitrary location on the axes.")
print("`s` is the string, `x`, `y` are data coordinates.")

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, color='blue', label='Sine Wave')

# Add text at a specific data coordinate
plt.text(2, 0.8, "Peak Amplitude",
         fontsize=14,        # Font size
         color='red',        # Text color
         fontweight='bold',  # Font weight (e.g., 'normal', 'bold', 'light')
         ha='center',        # Horizontal alignment: 'left', 'right', 'center'
         va='bottom',        # Vertical alignment: 'top', 'bottom', 'center', 'baseline'
         bbox=dict(boxstyle="round,pad=0.3", fc="yellow", ec="darkorange", lw=2, alpha=0.7)) # Bounding box
plt.title("Plot with Basic Text")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()

# Text on axes (using `ax.text` with `plt.subplots`)
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y, color='green')
ax.set_title("Axes Text Example")
ax.set_xlabel("X-values")
ax.set_ylabel("Y-values")

# Add text in axes coordinates (0,0 is bottom-left, 1,1 is top-right of axes)
ax.text(0.05, 0.95, "Top-Left Corner",
        transform=ax.transAxes, # Important: specify `transform=ax.transAxes` for axes coordinates
        fontsize=12, color='navy',
        ha='left', va='top')

ax.text(0.95, 0.05, "Bottom-Right Corner",
        transform=ax.transAxes,
        fontsize=12, color='darkred',
        ha='right', va='bottom')

plt.show()


# --- 2. Titles and Labels (Advanced Customization) ---
print("\n--- 2. Titles and Labels (Advanced Customization) ---")
print("While not strictly 'annotations', titles and labels are key text elements.")

plt.figure(figsize=(9, 6))
plt.plot(x, y, color='darkcyan')

# Main Title Customization
plt.title("Comprehensive Plot Title Customization",
          fontsize=18,
          color='#333333', # Dark gray
          fontfamily='serif',
          fontweight='heavy',
          loc='center', # 'left', 'center', 'right'
          pad=20) # Distance from the top of the axes to the title

# X-axis Label Customization
plt.xlabel("Independent Variable (Units)",
           fontsize=14,
           color='darkgreen',
           fontstyle='italic', # 'normal', 'italic', 'oblique'
           labelpad=15) # Distance from the axis to the label

# Y-axis Label Customization
plt.ylabel("Dependent Variable (Magnitude)",
           fontsize=14,
           color='darkblue',
           rotation=90, # Rotate label (default)
           ha='right', # Horizontal alignment of the label itself
           labelpad=15)

plt.grid(True, linestyle=':', alpha=0.7)
plt.show()


# --- 3. Annotations (`plt.annotate()` or `ax.annotate()`) ---
print("\n--- 3. Annotations (`plt.annotate()` / `ax.annotate()`) ---")
print("`annotate()` creates text with an optional arrow, connecting a text label to a specific data point.")
print("`xy`: (x, y) coordinates of the point to annotate.")
print("`xytext`: (x, y) coordinates of the text label.")
print("`arrowprops`: Dictionary of arrow properties.")

# Find a specific point to highlight (e.g., maximum value)
max_y_index = np.argmax(y)
point_x = x[max_y_index]
point_y = y[max_y_index]

plt.figure(figsize=(9, 7))
plt.plot(x, y, 'o-', markersize=4, color='orange', label='Data Series')
plt.scatter(point_x, point_y, color='red', s=100, zorder=5) # Highlight the point

# Basic Annotation
plt.annotate('Local Maximum',          # The text string
             xy=(point_x, point_y),    # The point to annotate (data coordinates)
             xytext=(point_x + 1.5, point_y + 0.3), # Where the text should be (data coordinates)
             arrowprops=dict(facecolor='black', shrink=0.05), # Arrow properties
             fontsize=12,
             color='black')

# Another annotation with a specific arrow style and textbox
plt.annotate('Start Point',
             xy=(x[0], y[0]),
             xytext=(x[0] + 2, y[0] - 0.5),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2", color='darkgreen', linewidth=1.5),
             bbox=dict(boxstyle="square,pad=0.5", fc="lightgreen", ec="green", lw=1),
             fontsize=10,
             color='darkgreen')

plt.title("Plot with Annotations")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()


# --- 4. Customizing Arrow Properties (`arrowprops`) ---
print("\n--- 4. Customizing Arrow Properties ---")
print("`arrowprops` is a dictionary that takes various parameters to control the arrow's appearance.")

plt.figure(figsize=(10, 8))
plt.plot(x, y, color='gray', linestyle=':', label='Background Trend')

# Example 1: Simple arrow
plt.annotate('Arrow Style 1', xy=(2.5, np.sin(2.5)), xytext=(0.5, 0.5),
             arrowprops=dict(facecolor='red', shrink=0.05),
             fontsize=10, color='red')

# Example 2: Double-sided arrow, blue, thicker
plt.annotate('Arrow Style 2', xy=(5, np.sin(5)), xytext=(7, 0.8),
             arrowprops=dict(arrowstyle='<->', color='blue', linewidth=2),
             fontsize=10, color='blue')

# Example 3: Curved arrow with specific head
plt.annotate('Arrow Style 3', xy=(8, np.sin(8)), xytext=(6, -0.8),
             arrowprops=dict(arrowstyle='-[, widthA=2.0, lengthA=1.0', lw=1.5, color='green', connectionstyle="arc3,rad=-0.3"),
             fontsize=10, color='green')

# Example 4: Fancy arrow with different head/tail
plt.annotate('Fancy Arrow', xy=(7, np.sin(7)), xytext=(9, -0.5),
             arrowprops=dict(arrowstyle="fancy", fc="purple", ec="purple", connectionstyle="arc3,rad=.5", patchB=plt.Circle((0, 0), 0.2, fc="yellow")),
             fontsize=10, color='purple')

plt.title("Annotation Arrow Style Gallery")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# Common `arrowstyle` values: '-', '->', '-[', '|-|', 'fancy', 'simple', 'wedge'
# Common `connectionstyle` values: 'arc3', 'angle', 'angle3', 'arc', 'bar'


# --- 5. Math Text (`$formula$`) ---
print("\n--- 5. Math Text (`$formula$`) ---")
print("Matplotlib supports LaTeX-like math text using dollar signs ($...$).")

plt.figure(figsize=(8, 6))
plt.plot(x, np.sin(x), 'b-', label=r'$y = \sin(x)$') # Use 'r' for raw string to avoid backslash issues

plt.title(r'Visualization of $y = \sin(x)$ with $\int_a^b f(x) dx$', fontsize=16) # Title with math
plt.xlabel(r'Angle $\theta$ (radians)', fontsize=14)
plt.ylabel(r'Amplitude $A$', fontsize=14)

plt.text(6, 0.5, r'$\frac{d}{dx}(\sin(x)) = \cos(x)$',
         fontsize=16, color='darkgreen',
         bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="green", lw=1))

plt.annotate(r'Maximum at $\frac{\pi}{2}$',
             xy=(np.pi/2, 1), xytext=(np.pi/2 + 1.5, 0.7),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12)

plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


# --- 6. Figure Text (`fig.text()`) ---
print("\n--- 6. Figure Text (`fig.text()`) ---")
print("Text added using `fig.text()` is relative to the figure, not to a specific axes.")
print("Useful for adding general notes or copyrights to the entire figure.")

fig_text = plt.figure(figsize=(9, 7))
ax_f = fig_text.add_subplot(111)
ax_f.plot(x, y**2, color='brown')
ax_f.set_title("Plot in a Figure")
ax_f.set_xlabel("X")
ax_f.set_ylabel("Y")
ax_f.grid(True)

# Add text to the figure itself (0,0 is bottom-left of figure, 1,1 is top-right)
fig_text.text(0.5, 0.02, "Data Source: Simulated Data | Plot by Matplotlib",
              fontsize=10, color='gray', ha='center', va='bottom')

fig_text.text(0.01, 0.98, "Version 1.0",
              fontsize=8, color='darkgray', ha='left', va='top')

plt.tight_layout(rect=[0.0, 0.05, 1, 1.0]) # Adjust layout to make space for figure text
plt.show()


print("\n--- End of Matplotlib Text and Annotations Practice Code ---")

# Key takeaways:
# - `plt.text()` / `ax.text()` for arbitrary text at data coordinates (or axes coordinates with `transform`).
# - `plt.title()`, `plt.xlabel()`, `plt.ylabel()` for plot labels.
# - `plt.annotate()` / `ax.annotate()` for text connected to a point with an arrow.
# - `arrowprops` dictionary for extensive arrow customization.
# - Use `r'$...$'` for LaTeX-like mathematical expressions.
# - `fig.text()` for text relative to the entire figure.