import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print("--- Matplotlib Bar Chart: All About in Code ---")

# --- 1. Basic Vertical Bar Chart ---
print("\n--- 1. Basic Vertical Bar Chart ---")
print("A bar chart typically displays categories on one axis and values on the other.")

# Data
categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
values = [25, 40, 30, 55, 20]

plt.figure(figsize=(8, 6)) # Create a new figure
plt.bar(categories, values) # Create the bar chart
plt.title("Basic Vertical Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.grid(axis='y', linestyle='--', alpha=0.7) # Add horizontal grid lines
plt.show()


# --- 2. Customizing Bar Charts ---
print("\n--- 2. Customizing Bar Charts ---")

# 2.1 Colors, Edges, Width, and Transparency
plt.figure(figsize=(9, 6))
plt.bar(categories, values,
        color=['skyblue', 'lightcoral', 'lightgreen', 'gold', 'plum'], # List of colors for each bar
        edgecolor='black', # Color of the bar borders
        linewidth=1,       # Width of the bar borders
        width=0.7,         # Width of the bars (0 to 1, default is 0.8)
        alpha=0.8)         # Transparency of the bars
plt.title("Customized Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.ylim(0, 60) # Set y-axis limits for consistent scaling
plt.grid(axis='y', linestyle=':', alpha=0.6)
plt.show()

# 2.2 Adding Text Labels on Bars
plt.figure(figsize=(9, 6))
bars = plt.bar(categories, values, color='teal', alpha=0.8)
plt.title("Bar Chart with Value Labels")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.ylim(0, 65) # Adjust y-limit to make space for labels

# Add value labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, round(yval, 1), ha='center', va='bottom', fontsize=10)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# --- 3. Horizontal Bar Chart (`barh`) ---
print("\n--- 3. Horizontal Bar Chart ---")
print("Use `plt.barh()` for horizontal bars, often better for many categories with long names.")

plt.figure(figsize=(9, 6))
plt.barh(categories, values, color='salmon', edgecolor='black')
plt.title("Horizontal Bar Chart")
plt.xlabel("Values")
plt.ylabel("Categories")
plt.xlim(0, 60) # Set x-axis limits
plt.grid(axis='x', linestyle='--', alpha=0.7) # Horizontal grid lines
plt.show()

# Adding labels to horizontal bars
plt.figure(figsize=(9, 6))
bars_h = plt.barh(categories, values, color='cornflowerblue', alpha=0.8)
plt.title("Horizontal Bar Chart with Value Labels")
plt.xlabel("Values")
plt.ylabel("Categories")
plt.xlim(0, 65) # Adjust x-limit

for bar in bars_h:
    xval = bar.get_width()
    plt.text(xval + 1, bar.get_y() + bar.get_height()/2, round(xval, 1), va='center', ha='left', fontsize=10)

plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()


# --- 4. Grouped Bar Charts ---
print("\n--- 4. Grouped Bar Charts ---")
print("Compare multiple sets of values across categories.")

labels = ['Group 1', 'Group 2', 'Group 3', 'Group 4']
data_set1 = [10, 20, 15, 25]
data_set2 = [12, 18, 20, 22]
data_set3 = [8, 25, 10, 30]

x_indices = np.arange(len(labels)) # The label locations
width = 0.2 # Width of each bar

plt.figure(figsize=(10, 7))
# Plotting three sets of bars
plt.bar(x_indices - width, data_set1, width, label='Dataset 1', color='skyblue', edgecolor='black')
plt.bar(x_indices, data_set2, width, label='Dataset 2', color='lightcoral', edgecolor='black')
plt.bar(x_indices + width, data_set3, width, label='Dataset 3', color='lightgreen', edgecolor='black')

plt.title("Grouped Bar Chart")
plt.xlabel("Groups")
plt.ylabel("Scores")
plt.xticks(x_indices, labels) # Set tick locations and labels
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# --- 5. Stacked Bar Charts ---
print("\n--- 5. Stacked Bar Charts ---")
print("Show the composition of categories, where segments of each bar represent different components.")

labels_stacked = ['Q1', 'Q2', 'Q3', 'Q4']
component1 = np.array([5, 10, 7, 12])
component2 = np.array([8, 6, 10, 5])
component3 = np.array([3, 4, 5, 8])

plt.figure(figsize=(8, 6))
# Plot the first component
plt.bar(labels_stacked, component1, label='Component A', color='mediumaquamarine', edgecolor='black')
# Plot the second component on top of the first
plt.bar(labels_stacked, component2, bottom=component1, label='Component B', color='sandybrown', edgecolor='black')
# Plot the third component on top of the sum of first two
plt.bar(labels_stacked, component3, bottom=component1 + component2, label='Component C', color='cornflowerblue', edgecolor='black')

plt.title("Stacked Bar Chart (Quarterly Breakdown)")
plt.xlabel("Quarter")
plt.ylabel("Total Value")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# --- 6. Bar Charts with Error Bars ---
print("\n--- 6. Bar Charts with Error Bars ---")
print("Visualize the variability or uncertainty in your data.")

data_mean = [30, 45, 20, 50]
data_std = [3, 5, 2, 4] # Standard deviation or error

plt.figure(figsize=(8, 6))
plt.bar(categories[:4], data_mean, yerr=data_std, capsize=5, color='lightgray', edgecolor='black')
# `yerr`: size of error bar
# `capsize`: width of the caps on the error bars
plt.title("Bar Chart with Error Bars")
plt.xlabel("Experiment Conditions")
plt.ylabel("Mean Result")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# --- 7. Bar Charts from Pandas DataFrame ---
print("\n--- 7. Bar Charts from Pandas DataFrame ---")
print("Pandas has built-in plotting functions that use Matplotlib as backend, making it convenient.")

df_data = pd.DataFrame({
    'City': ['Dhaka', 'Chittagong', 'Khulna', 'Sylhet'],
    'Population (Millions)': [21.0, 5.2, 2.9, 1.0],
    'Area (km^2)': [306, 168, 45, 26]
})
print(f"\nDataFrame:\n{df_data}")

plt.figure(figsize=(8, 6))
df_data.plot(x='City', y='Population (Millions)', kind='bar',
             color='darkcyan', edgecolor='black', legend=False, ax=plt.gca()) # ax=plt.gca() uses current axes
plt.title("Population by City (from Pandas)")
plt.xlabel("City")
plt.ylabel("Population (Millions)")
plt.xticks(rotation=45, ha='right') # Rotate labels for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout() # Adjust layout to prevent labels from overlapping
plt.show()


print("\n--- End of Matplotlib Bar Chart Practice Code ---")

# Remember:
# - `plt.figure()` creates a new plot window/canvas.
# - `plt.show()` displays all open figures.
# - In interactive environments (like Jupyter), plots appear inline.
# - `plt.tight_layout()` helps prevent labels from overlapping.