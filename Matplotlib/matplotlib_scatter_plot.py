import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print("--- Matplotlib Scatter Plot: All About in Code ---")

# --- 1. Basic Scatter Plot ---
print("\n--- 1. Basic Scatter Plot ---")
print("The simplest scatter plot shows the relationship between two variables (X and Y).")

np.random.seed(42) # for reproducibility
num_points = 50

# Generate some correlated data with noise
x_basic = 10 * np.random.rand(num_points)
y_basic = 2 * x_basic + np.random.randn(num_points) * 3 # y is roughly 2x + noise

plt.figure(figsize=(7, 5))
plt.scatter(x_basic, y_basic)
plt.title("Basic Scatter Plot")
plt.xlabel("X-axis (Independent Variable)")
plt.ylabel("Y-axis (Dependent Variable)")
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()


# --- 2. Customizing Markers ---
print("\n--- 2. Customizing Markers ---")
print("You can change the shape, size, color, and transparency of individual markers.")

# 2.1 Changing Marker Style and Color
plt.figure(figsize=(7, 5))
plt.scatter(x_basic, y_basic,
            marker='o',       # Circle marker (default)
            color='blue',     # Color of markers
            s=50,             # Size of markers
            alpha=0.8,        # Transparency (alpha)
            edgecolors='black', # Color of the marker edge
            linewidths=0.7)    # Width of the marker edge
plt.title("Scatter Plot with Custom Marker Style")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()

# Other common markers: 'o' (circle), 's' (square), '^' (triangle up), 'v' (triangle down),
# 'x' (x marker), '+' (plus marker), '*' (star), 'D' (diamond), '.' (point)

# 2.2 Varying Marker Size and Color based on a Third Variable
print("\n--- 2.2 Varying Marker Size and Color ---")
# Let's create data where size and color depend on other features.
np.random.seed(0)
num_samples = 100
data_x = np.random.randn(num_samples) * 10
data_y = np.random.randn(num_samples) * 5 + 20
data_z_size = np.abs(np.random.randn(num_samples) * 200 + 50) # Size of markers
data_z_color = np.random.rand(num_samples) # Value for color mapping

plt.figure(figsize=(8, 7))
plt.scatter(data_x, data_y,
            s=data_z_size,     # Marker size determined by `data_z_size`
            c=data_z_color,    # Marker color determined by `data_z_color`
            cmap='viridis',    # Colormap to use (e.g., 'viridis', 'plasma', 'coolwarm', 'RdBu')
            alpha=0.7,
            edgecolors='gray',
            linewidths=0.5)
plt.colorbar(label='Z-Axis (Color Intensity)') # Add a color bar to explain the `c` mapping
plt.title("Scatter Plot with Varying Size and Color")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid(True, alpha=0.6)
plt.show()


# --- 3. Scatter Plot with Categories / Different Groups ---
print("\n--- 3. Scatter Plot with Categories / Different Groups ---")
print("You can plot different groups of data on the same scatter plot with distinct markers or colors.")

# Create categorical data
category_data = np.random.randint(0, 3, num_samples) # 3 categories (0, 1, 2)
colors = ['red', 'green', 'blue']
labels = ['Group A', 'Group B', 'Group C']
markers = ['o', 's', '^']

plt.figure(figsize=(8, 6))
for i in range(3):
    mask = (category_data == i)
    plt.scatter(data_x[mask], data_y[mask],
                color=colors[i],
                marker=markers[i],
                s=80,
                alpha=0.7,
                label=labels[i],
                edgecolors='black')
plt.title("Scatter Plot by Category")
plt.xlabel("X Value")
plt.ylabel("Y Value")
plt.legend(title="Categories") # Show legend for groups
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()


# --- 4. Scatter Plot for Time Series (e.g., Daily Readings) ---
print("\n--- 4. Scatter Plot for Time Series ---")
print("While line plots are common for time series, scatter plots can highlight individual events or readings.")

# Generate some time series data
dates = pd.to_datetime(pd.date_range(start='2024-01-01', periods=50, freq='D'))
temperature = 15 + 5 * np.sin(np.linspace(0, 4 * np.pi, 50)) + np.random.randn(50) * 1.5

plt.figure(figsize=(10, 6))
plt.scatter(dates, temperature,
            color='orange',
            s=70,
            alpha=0.7,
            edgecolors='darkorange',
            label='Daily Temperature')
plt.title("Daily Temperature Readings (Scatter)")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45) # Rotate x-axis labels for better readability
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout() # Adjust layout to prevent labels from overlapping
plt.show()


# --- 5. Combining Scatter Plots with Other Plot Types (e.g., Line) ---
print("\n--- 5. Combining Scatter Plots with Other Plot Types ---")
print("You can overlay a scatter plot on top of a line plot, for instance, to show raw data points and a trend line.")

x_trend = np.linspace(0, 10, 100)
y_trend = 2 * x_trend + 5 # A clear linear trend

plt.figure(figsize=(8, 6))
plt.plot(x_trend, y_trend, color='red', linestyle='-', linewidth=2, label='Trend Line') # Line plot for trend
plt.scatter(x_basic, y_basic, color='blue', alpha=0.6, label='Raw Data Points') # Scatter plot for raw data
plt.title("Scatter Plot with a Trend Line")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True, alpha=0.7)
plt.show()


# --- 6. Annotations on Scatter Plots ---
print("\n--- 6. Annotations on Scatter Plots ---")
print("Add text labels or arrows to highlight specific data points.")

# Find a point to annotate (e.g., the point with max Y value)
max_y_index = np.argmax(y_basic)
annot_x = x_basic[max_y_index]
annot_y = y_basic[max_y_index]

plt.figure(figsize=(7, 5))
plt.scatter(x_basic, y_basic, color='green', alpha=0.7)
plt.scatter(annot_x, annot_y, color='red', s=100, marker='*', label='Max Y Point', zorder=5) # Highlight it

plt.annotate('Highest Value', xy=(annot_x, annot_y), xytext=(annot_x + 1.5, annot_y - 3),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8),
             bbox=dict(boxstyle="round,pad=0.5", fc="yellow", ec="darkred", lw=1, alpha=0.8),
             fontsize=10,
             color='darkred')
plt.title("Scatter Plot with Annotation")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()


print("\n--- End of Matplotlib Scatter Plot Practice Code ---")

# Remember: `plt.show()` is crucial to display your plots.
# In a script, it opens a window. In a Jupyter Notebook, it renders inline.