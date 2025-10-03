import matplotlib.pyplot as plt
import numpy as np

print("--- Matplotlib Pie Chart: All About in Code ---")

# --- 1. Basic Pie Chart ---
print("\n--- 1. Basic Pie Chart ---")
print("A pie chart divides a circle into sectors, each representing a proportional part of the whole.")

# Data: Proportions of different categories
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [30, 25, 20, 25] # These values will be converted to percentages automatically

plt.figure(figsize=(7, 7)) # Make the figure square for a perfect circle
plt.pie(sizes, labels=labels) # Create the pie chart
plt.title("Basic Pie Chart")
plt.axis('equal') # Ensures that pie is drawn as a circle.
plt.show()


# --- 2. Customizing Pie Charts ---
print("\n--- 2. Customizing Pie Charts ---")

# 2.1 Adding Percentages (`autopct`)
print("\n--- 2.1 Adding Percentages (`autopct`) ---")
# `autopct` allows you to display the percentage value on each slice.
# The format string uses standard string formatting.
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%') # Format: 1 decimal place, followed by '%'
plt.title("Pie Chart with Percentages")
plt.axis('equal')
plt.show()

# More complex autopct formatting (e.g., value and percentage)
total = sum(sizes)
def func(pct, allvals):
    absolute = int(pct/100.*total)
    return f"{pct:.1f}%\n({absolute:d})"

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct=lambda pct: func(pct, sizes),
        pctdistance=0.8) # Distance of percentage labels from center
plt.title("Pie Chart with Value and Percentage Labels")
plt.axis('equal')
plt.show()


# 2.2 Colors and `explode` Effect
print("\n--- 2.2 Colors and `explode` ---")
# `colors`: list of colors for each slice.
# `explode`: a tuple or array indicating how much each slice should be 'exploded' (pulled out).

# Define custom colors
custom_colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99'] # Hex codes for pastel colors
explode_effect = (0, 0.1, 0, 0.05) # Explode 'Category B' and 'Category D'

plt.figure(figsize=(8, 8))
plt.pie(sizes,
        explode=explode_effect, # Apply explode effect
        labels=labels,
        colors=custom_colors,   # Apply custom colors
        autopct='%1.1f%%',
        shadow=True,            # Add a shadow effect
        startangle=90)          # Start the first slice at 90 degrees (top)
plt.title("Customized Pie Chart with Explode and Shadow")
plt.axis('equal')
plt.show()

# 2.3 Customizing Text Properties (Labels, Percentages)
print("\n--- 2.3 Customizing Text Properties ---")

plt.figure(figsize=(9, 9))
wedges, texts, autotexts = plt.pie(sizes,
                                   explode=explode_effect,
                                   labels=labels,
                                   colors=custom_colors,
                                   autopct='%1.1f%%',
                                   shadow=True,
                                   startangle=90,
                                   textprops={'fontsize': 12, 'color': 'darkblue'}) # Properties for labels
# Customize autotexts (percentages)
for autotext in autotexts:
    autotext.set_color('white') # Set color of percentage text
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

plt.title("Pie Chart with Customized Text")
plt.axis('equal')
plt.show()


# --- 3. Donut Chart (Pie Chart with a Hole) ---
print("\n--- 3. Donut Chart ---")
print("A donut chart is a pie chart with a blank center, often used to display data in the center.")

# Draw a circle in the middle
my_circle = plt.Circle((0, 0), 0.7, color='white') # (center_x, center_y), radius, color

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=custom_colors, autopct='%1.1f%%',
        pctdistance=0.85, # Keep percentages closer to the center
        wedgeprops={'edgecolor': 'black', 'linewidth': 1.5, 'antialiased': True}) # Properties for the wedges
plt.title("Donut Chart")
p = plt.gcf() # Get the current figure
p.gca().add_artist(my_circle) # Add the circle to the current axes
plt.axis('equal')
plt.show()


# --- 4. Nested Pie Chart (or Sunburst Chart concept) ---
print("\n--- 4. Nested Pie Chart (conceptual) ---")
print("Representing hierarchical data. This is more advanced and often done with `sunburst` plots in libraries like Plotly or Seaborn, but can be simulated in Matplotlib.")

# Outer ring data
group_names = ['Group A', 'Group B', 'Group C']
group_sizes = [40, 30, 30] # Total for each group

# Inner ring data (breakdown of each group)
subgroup_names = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
subgroup_sizes = [25, 15, 10, 20, 15, 15] # Must sum up to group_sizes (25+15=40, 10+20=30, 15+15=30)
subgroup_colors = ['#FFB3BA', '#FFDFBA', '#FFFFBA', '#BAFFC9', '#BAE1FF', '#D8BFD8'] # More granular colors

# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 10))

# Outer ring (groups)
ax.pie(group_sizes,
       radius=1, # Outer radius
       labels=group_names,
       colors=['lightgray'] * len(group_names), # Use a neutral color for outer ring
       wedgeprops=dict(width=0.3, edgecolor='w')) # Make it a ring

# Inner ring (subgroups)
ax.pie(subgroup_sizes,
       radius=0.7, # Inner radius
       labels=subgroup_names,
       labeldistance=0.8, # Move inner labels closer
       colors=subgroup_colors,
       autopct='%1.1f%%', # Percentages for inner ring
       pctdistance=0.6,
       wedgeprops=dict(width=0.3, edgecolor='w'))

ax.set_title("Nested Pie Chart Example")
ax.axis('equal')
plt.show()


# --- 5. When to Use/Avoid Pie Charts ---
print("\n--- 5. When to Use/Avoid Pie Charts ---")
print("Use when:")
print(" - Showing proportions of a whole (must sum to 100% or equivalent).")
print(" - You have a small number of categories (ideally 2-5).")
print(" - The differences in proportions are significant.")
print("\nAvoid when:")
print(" - Comparing many categories (becomes cluttered and hard to read).")
print(" - Exact values or small differences are important (bar charts are better).")
print(" - Categories don't sum to a meaningful whole.")


print("\n--- End of Matplotlib Pie Chart Practice Code ---")

# Reminder:
# - `plt.figure()` for new plots.
# - `plt.show()` to display plots.
# - `plt.axis('equal')` is vital for a circular pie chart.
# - `autopct` for percentages.
# - `explode` to highlight slices.