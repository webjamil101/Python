import matplotlib.pyplot as plt
import numpy as np

print("--- Matplotlib Basic Plotting: Practice Code ---")

# --- 1. The Simplest Plot: Line Plot ---
print("\n--- 1. The Simplest Plot: Line Plot ---")
print("A line plot connects data points with lines, typically used to show trends over time or ordered data.")

# Create some basic data
x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([2, 4, 1, 5, 3])

# 1.1 Basic `plt.plot()`
plt.figure(figsize=(7, 5)) # Create a new figure (the canvas for your plot)
plt.plot(x_data, y_data)   # Plot x_data on the x-axis, y_data on the y-axis
plt.title("My First Line Plot") # Add a title to the plot
plt.xlabel("X-axis Values")    # Add a label for the x-axis
plt.ylabel("Y-axis Values")    # Add a label for the y-axis
plt.grid(True)                 # Add a grid for better readability
plt.show()                     # Display the plot


# 1.2 Adding Customizations (Color, Line Style, Marker)
print("\n--- 1.2 Customizing Line Plots ---")
x_sine = np.linspace(0, 2 * np.pi, 100) # 100 points from 0 to 2*pi
y_sine = np.sin(x_sine)
y_cosine = np.cos(x_sine)

plt.figure(figsize=(8, 6))

# Plotting the sine wave with specific color, line style, and label
plt.plot(x_sine, y_sine,
         color='blue',       # Line color
         linestyle='--',     # Dashed line style
         marker='o',         # Circle markers at each data point
         markersize=5,       # Size of the markers
         label='Sine Wave')  # Label for the legend

# Plotting the cosine wave with a different style
plt.plot(x_sine, y_cosine,
         color='red',
         linestyle=':',      # Dotted line style
         marker='x',         # 'x' markers
         alpha=0.7,          # Transparency (0.0 to 1.0)
         linewidth=2,        # Thickness of the line
         label='Cosine Wave')

plt.title("Sine and Cosine Waves with Custom Styles")
plt.xlabel("Angle (radians)")
plt.ylabel("Amplitude")
plt.legend()                 # Display the legend (uses the 'label' arguments)
plt.grid(True, linestyle=':', alpha=0.6) # Customize grid line style and transparency
plt.show()

# Shorthand for styling: 'color_marker_linestyle'
# e.g., 'ro-' means red line, circle markers, solid line
plt.figure(figsize=(6, 4))
plt.plot(x_data, y_data, 'g^:') # Green, triangle_up markers, dotted line
plt.title("Shorthand Styling Example")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# --- 2. Scatter Plot ---
print("\n--- 2. Scatter Plot ---")
print("A scatter plot displays individual data points as markers, useful for showing correlation or distribution.")

np.random.seed(42) # for reproducibility
num_samples = 100
x_scatter = np.random.rand(num_samples) * 10
y_scatter = 2 * x_scatter + np.random.randn(num_samples) * 2 # y roughly proportional to x with some noise

plt.figure(figsize=(7, 6))
plt.scatter(x_scatter, y_scatter,
            color='purple',    # Color of the markers
            s=50,              # Size of the markers
            alpha=0.6,         # Transparency
            edgecolors='black', # Color of the marker edges
            label='Data Points')
plt.title("Simple Scatter Plot")
plt.xlabel("Independent Variable")
plt.ylabel("Dependent Variable")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Scatter plot with color mapping (using a third variable)
colors_scatter = np.random.rand(num_samples) # Random values for color mapping
plt.figure(figsize=(8, 7))
plt.scatter(x_scatter, y_scatter,
            c=colors_scatter,  # Map color based on this array
            cmap='viridis',    # Colormap to use (e.g., 'viridis', 'plasma', 'coolwarm')
            s=100,             # Marker size
            alpha=0.8,
            edgecolors='white',
            linewidths=0.5)
plt.colorbar(label='Feature Z Value') # Add a color bar to explain the colors
plt.title("Scatter Plot with Color Mapping")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# --- 3. Bar Chart ---
print("\n--- 3. Bar Chart ---")
print("Bar charts are used to compare categorical data, showing quantities for different categories.")

categories = ['Apples', 'Bananas', 'Oranges', 'Grapes']
sales = [150, 220, 180, 90]

plt.figure(figsize=(8, 6))
plt.bar(categories, sales,
        color=['skyblue', 'lightcoral', 'lightgreen', 'gold'], # Different colors for each bar
        edgecolor='black',
        width=0.7) # Width of the bars (0 to 1, default 0.8)
plt.title("Monthly Sales by Fruit")
plt.xlabel("Fruit Type")
plt.ylabel("Sales Units")
plt.ylim(0, 250) # Set y-axis limits to provide consistent scaling
plt.grid(axis='y', linestyle='--', alpha=0.7) # Grid lines only on y-axis
plt.show()

# Horizontal Bar Chart
plt.figure(figsize=(8, 6))
plt.barh(categories, sales, color='teal', edgecolor='black')
plt.title("Monthly Sales by Fruit (Horizontal)")
plt.xlabel("Sales Units")
plt.ylabel("Fruit Type")
plt.xlim(0, 250)
plt.show()


# --- 4. Histogram ---
print("\n--- 4. Histogram ---")
print("Histograms display the distribution of a single numerical variable by dividing data into bins.")

data_distribution = np.random.normal(loc=0, scale=1, size=1000) # 1000 data points from a normal distribution

plt.figure(figsize=(8, 6))
plt.hist(data_distribution,
         bins=30,           # Number of bins (intervals)
         color='lightblue',
         edgecolor='darkblue', # Edges of the bars
         alpha=0.7,          # Transparency
         density=False)      # If True, plots probability density; if False (default), plots counts
plt.title("Distribution of Data (Histogram)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(axis='y', alpha=0.7)
plt.show()

# Histogram with density (area sums to 1)
plt.figure(figsize=(8, 6))
plt.hist(data_distribution, bins=30, density=True, color='lightgreen', edgecolor='green', alpha=0.7)
plt.title("Probability Density Histogram")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()


# --- 5. Pie Chart ---
print("\n--- 5. Pie Chart ---")
print("Pie charts show proportions of a whole, dividing a circle into slices.")

# Data for pie chart
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [30, 25, 20, 25] # Proportions, sums to 100
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0, 0.1, 0, 0) # 'explode' the 2nd slice (Category B) slightly

plt.figure(figsize=(8, 8)) # Make the figure square for a perfect circle
plt.pie(sizes,
        explode=explode,     # How much to "explode" slices
        labels=labels,       # Labels for each slice
        colors=colors,       # Colors for each slice
        autopct='%1.1f%%',   # Format percentage on slices (e.g., 25.0%)
        shadow=True,         # Add a shadow effect
        startangle=90)       # Start the first slice at 90 degrees (top)
plt.axis('equal')            # Ensures the pie chart is drawn as a circle.
plt.title("Distribution of Categories")
plt.show()


print("\n--- End of Matplotlib Basic Plotting Practice Code ---")

# Important notes for running in different environments:
# - If running in a script, `plt.show()` opens a new window for each plot.
# - If running in a Jupyter Notebook or IPython, plots are displayed inline.
# - Use `plt.close()` or `plt.clf()` to close the current figure or clear it if you're
#   generating many plots in a loop and want to manage memory.