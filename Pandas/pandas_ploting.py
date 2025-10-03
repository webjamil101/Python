import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # Often imported for additional customization

print("--- Pandas Plotting Code ---")

# --- 1. Setup: Create Sample DataFrames ---
print("\n--- 1. Sample Data Setup ---")

# Time Series Data for Line Plot
dates = pd.date_range(start='2023-01-01', periods=100, freq='D')
ts_data = {
    'Value1': np.random.randn(100).cumsum() + 50,
    'Value2': np.random.randn(100).cumsum() + 30
}
df_ts = pd.DataFrame(ts_data, index=dates)
print("Time Series DataFrame (df_ts):\n", df_ts.head())

# Categorical and Numerical Data for Bar, Box, Histograms
np.random.seed(42) # for reproducibility
categorical_data = {
    'Category': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'D'] * 10,
    'Score': np.random.randint(50, 100, 100),
    'Age': np.random.randint(20, 40, 100),
    'Gender': np.random.choice(['Male', 'Female'], 100)
}
df_categorical = pd.DataFrame(categorical_data)
print("\nCategorical DataFrame (df_categorical):\n", df_categorical.head())

# Data for Scatter Plot
scatter_data = {
    'X_Axis': np.random.rand(50) * 100,
    'Y_Axis': np.random.rand(50) * 100 + np.random.rand(50) * 20, # some correlation
    'Size': np.random.rand(50) * 500 + 100, # for size of points
    'Color_Group': np.random.choice(['Group1', 'Group2', 'Group3'], 50)
}
df_scatter = pd.DataFrame(scatter_data)
print("\nScatter DataFrame (df_scatter):\n", df_scatter.head())


# --- 2. Basic Plots ---
print("\n--- 2. Basic Plots ---")

# 2.1 Line Plot (default for Series/DataFrame with datetime index)
print("\n--- Line Plot ---")
df_ts['Value1'].plot(title='Value1 Over Time')
plt.ylabel('Value')
plt.grid(True)
plt.show()

# Plot multiple columns on the same line plot
df_ts.plot(figsize=(10, 6), title='Values Over Time')
plt.ylabel('Values')
plt.grid(True)
plt.show()

# 2.2 Bar Plot
print("\n--- Bar Plot ---")
# Value counts of a categorical column
df_categorical['Category'].value_counts().plot(kind='bar', title='Count by Category')
plt.xlabel('Category')
plt.ylabel('Count')
plt.xticks(rotation=0) # Keep x-axis labels horizontal
plt.show()

# Bar plot of mean score by category
mean_score_by_category = df_categorical.groupby('Category')['Score'].mean()
mean_score_by_category.plot(kind='barh', title='Mean Score by Category', color='skyblue') # Horizontal bar plot
plt.xlabel('Mean Score')
plt.ylabel('Category')
plt.show()

# 2.3 Histogram
print("\n--- Histogram ---")
df_categorical['Score'].plot(kind='hist', bins=10, title='Distribution of Scores')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.show()

# Histogram for multiple columns
df_categorical[['Score', 'Age']].plot(kind='hist', bins=15, alpha=0.7, title='Score and Age Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# 2.4 Box Plot
print("\n--- Box Plot ---")
df_categorical['Score'].plot(kind='box', title='Box Plot of Scores')
plt.ylabel('Score')
plt.show()

# Box plots by group
df_categorical.boxplot(column='Score', by='Category', figsize=(8, 6))
plt.title('Score Distribution by Category')
plt.suptitle('') # Suppress the default matplotlib title
plt.xlabel('Category')
plt.ylabel('Score')
plt.show()

# 2.5 Scatter Plot
print("\n--- Scatter Plot ---")
df_scatter.plot(kind='scatter', x='X_Axis', y='Y_Axis', title='Scatter Plot of X vs Y')
plt.xlabel('X Value')
plt.ylabel('Y Value')
plt.show()

# Scatter plot with size and color differentiation
# 's' for size, 'c' for color, 'cmap' for color map, 'alpha' for transparency
df_scatter.plot(
    kind='scatter',
    x='X_Axis',
    y='Y_Axis',
    s=df_scatter['Size'] / 10, # Scale size for better visualization
    c=df_scatter['Y_Axis'],   # Color based on Y_Axis value
    cmap='viridis',           # Colormap
    alpha=0.6,
    title='Scatter Plot (Size and Color by Y-Axis)'
)
plt.xlabel('X Value')
plt.ylabel('Y Value')
plt.colorbar(label='Y_Axis Value') # Add a color bar
plt.show()


# --- 3. Other Plot Types ---
print("\n--- 3. Other Plot Types ---")

# 3.1 Area Plot
print("\n--- Area Plot ---")
df_ts.plot(kind='area', stacked=True, alpha=0.5, figsize=(10, 6), title='Stacked Area Plot of Values')
plt.ylabel('Cumulative Value')
plt.show()

# 3.2 Pie Chart
print("\n--- Pie Chart ---")
df_categorical['Gender'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%', # show percentages
    startangle=90,
    explode=(0.1, 0),  # explode the first slice (Male)
    title='Gender Distribution'
)
plt.ylabel('') # Hide the y-axis label
plt.show()

# 3.3 Kernel Density Estimate (KDE) Plot
print("\n--- KDE Plot ---")
df_categorical['Age'].plot(kind='kde', title='KDE of Age Distribution')
plt.xlabel('Age')
plt.ylabel('Density')
plt.grid(True)
plt.show()


# --- 4. Customization and Subplots ---
print("\n--- 4. Customization and Subplots ---")

# 4.1 Customizing plot elements
df_ts['Value1'].plot(
    figsize=(8, 4),
    color='red',
    linestyle='--',
    marker='o',
    markersize=5,
    title='Customized Line Plot of Value1',
    xlabel='Date',
    ylabel='Value',
    grid=True,
    legend=True
)
plt.axhline(df_ts['Value1'].mean(), color='gray', linestyle=':', label='Mean') # Add a horizontal line
plt.legend()
plt.show()

# 4.2 Creating subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

# Plot on the first subplot
df_categorical['Score'].plot(kind='hist', ax=axes[0], bins=15, title='Score Histogram')
axes[0].set_xlabel('Score')
axes[0].set_ylabel('Frequency')

# Plot on the second subplot
df_categorical['Age'].plot(kind='kde', ax=axes[1], title='Age KDE')
axes[1].set_xlabel('Age')
axes[1].set_ylabel('Density')

plt.tight_layout() # Adjust layout to prevent overlapping
plt.show()

# More complex subplot grid
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))

df_ts['Value1'].plot(ax=axes[0, 0], title='Value1 Time Series')
df_ts['Value2'].plot(ax=axes[0, 1], title='Value2 Time Series', color='orange')
df_categorical['Score'].plot(kind='hist', ax=axes[1, 0], bins=10, title='Score Histogram')
df_categorical['Category'].value_counts().plot(kind='bar', ax=axes[1, 1], title='Category Counts')

plt.tight_layout()
plt.show()


# --- 5. Plotting with Specific Columns ---
print("\n--- 5. Plotting Specific Columns ---")

# Plotting specific columns from a DataFrame directly
df_students_grades = pd.DataFrame({
    'Student': ['S1', 'S2', 'S3', 'S4'],
    'Math': [85, 90, 78, 92],
    'Physics': [70, 85, 90, 75],
    'Chemistry': [65, 80, 88, 70]
})
print("\nStudent Grades DataFrame:\n", df_students_grades)

df_students_grades.set_index('Student').plot(kind='bar', figsize=(8, 5), title='Student Scores by Subject')
plt.ylabel('Score')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


print("\n--- End of Pandas Plotting Code ---")