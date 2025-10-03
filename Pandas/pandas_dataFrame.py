import pandas as pd
import numpy as np

print("--- Pandas DataFrame Practice Code ---")

# --- 1. DataFrame Creation from various sources ---
print("\n--- 1. DataFrame Creation ---")

# 1.1 From a dictionary of lists (most common)
data1 = {
    'StudentID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Major': ['CS', 'Math', 'Physics', 'CS', 'Chemistry'],
    'GPA': [3.8, 3.5, 3.9, 3.2, 3.7]
}
df_students = pd.DataFrame(data1)
print("\nDataFrame from dict of lists (df_students):\n", df_students)

# 1.2 From a list of dictionaries
data2 = [
    {'City': 'New York', 'Population': 8.4, 'Country': 'USA'},
    {'City': 'London', 'Population': 8.9, 'Country': 'UK'},
    {'City': 'Paris', 'Population': 2.1, 'Country': 'France'},
    {'City': 'Tokyo', 'Population': 13.9, 'Country': 'Japan'}
]
df_cities = pd.DataFrame(data2)
print("\nDataFrame from list of dicts (df_cities):\n", df_cities)

# 1.3 From a NumPy array (specify columns/index if needed)
np_data = np.random.rand(4, 3) * 100 # 4 rows, 3 columns of random numbers
df_random = pd.DataFrame(np_data, columns=['ColA', 'ColB', 'ColC'], index=['r1', 'r2', 'r3', 'r4'])
print("\nDataFrame from NumPy array (df_random):\n", df_random)

# 1.4 Creating a DataFrame with a MultiIndex (Hierarchical Index)
arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
          ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
multi_index = pd.MultiIndex.from_arrays(arrays, names=['first', 'second'])
s = pd.Series(np.random.randn(8), index=multi_index)
df_multi_index = pd.DataFrame(s, columns=['Value'])
print("\nDataFrame with MultiIndex:\n", df_multi_index)



print("\n--- 2. Advanced Selection and Filtering ---")

# 2.1 Selecting rows based on multiple conditions with .loc[]
# Students who are CS majors AND have a GPA > 3.5
cs_high_gpa = df_students.loc[(df_students['Major'] == 'CS') & (df_students['GPA'] > 3.5)]
print("\nCS Majors with GPA > 3.5:\n", cs_high_gpa)

# 2.2 Using .isin() for filtering multiple values
# Cities in USA or UK
usa_uk_cities = df_cities[df_cities['Country'].isin(['USA', 'UK'])]
print("\nCities in USA or UK:\n", usa_uk_cities)

# 2.3 Selecting specific rows and columns using .loc[]
# Name and GPA for students with StudentID 2 and 4
specific_students_data = df_students.loc[df_students['StudentID'].isin([2, 4]), ['Name', 'GPA']]
print("\nName and GPA for StudentID 2 and 4:\n", specific_students_data)

# 2.4 Using .iloc[] for selection by integer positions
# First 3 rows, and columns at positions 1 and 3 (Name and GPA)
iloc_selection = df_students.iloc[:3, [1, 3]]
print("\nFirst 3 rows, Name and GPA columns (iloc):\n", iloc_selection)

# 2.5 Filtering using .query() (more readable for complex string queries)
# Note: .query() requires numexpr to be installed for complex queries if not default.
# pip install numexpr
try:
    high_pop_cities = df_cities.query('Population > 5 and Country == "USA"')
    print("\nCities with Population > 5 and Country is USA (.query):\n", high_pop_cities)
except ImportError:
    print("\nInstall 'numexpr' (pip install numexpr) to use .query() for complex queries.")
    print("Example of .query(): df_cities.query('Population > 5 and Country == \"USA\"')")



print("\n--- 3. Adding, Modifying, and Deleting Columns ---")

# 3.1 Adding a new column
df_students['Status'] = 'Active'
print("\nDataFrame with new 'Status' column:\n", df_students)

# 3.2 Modifying an existing column
df_students['GPA'] = df_students['GPA'] + 0.1 # Increase all GPAs by 0.1
print("\nDataFrame with updated 'GPA' column:\n", df_students)

# 3.3 Creating a new column based on existing ones
df_cities['Pop_Millions'] = df_cities['Population'] * 1000000
print("\nDataFrame with 'Pop_Millions' column:\n", df_cities)

# 3.4 Deleting a column
df_students_cleaned = df_students.drop(columns=['Status']) # Creates a new DataFrame
print("\nDataFrame after dropping 'Status' column:\n", df_students_cleaned)

# Or use `del df_students['Status']` for in-place deletion (modifies original df)
# del df_students['Status']
# print("\nDataFrame after in-place deletion of 'Status':\n", df_students)



print("\n--- 4. Handling Duplicates ---")

df_duplicates = pd.DataFrame({
    'A': [1, 2, 1, 3, 2],
    'B': ['x', 'y', 'x', 'z', 'y'],
    'C': [10, 20, 10, 30, 20]
})
print("\nDataFrame with duplicates:\n", df_duplicates)

# 4.1 Check for duplicate rows
print("\nDuplicate rows (boolean):\n", df_duplicates.duplicated())

# 4.2 Drop duplicate rows (keeps first occurrence by default)
df_no_duplicates = df_duplicates.drop_duplicates()
print("\nDataFrame after dropping duplicates:\n", df_no_duplicates)

# 4.3 Drop duplicates based on specific columns
df_no_duplicates_on_A = df_duplicates.drop_duplicates(subset=['A'])
print("\nDataFrame after dropping duplicates based on 'A':\n", df_no_duplicates_on_A)

# 4.4 Keep the last occurrence of duplicates
df_keep_last = df_duplicates.drop_duplicates(keep='last')
print("\nDataFrame after dropping duplicates (keeping last):\n", df_keep_last)



print("\n--- 5. Grouping and Aggregating (More Examples) ---")

# 5.1 Group by one column and get multiple aggregations
major_stats = df_students.groupby('Major').agg(
    Total_Students=('StudentID', 'count'),
    Avg_GPA=('GPA', 'mean'),
    Max_GPA=('GPA', 'max')
)
print("\nStudent statistics by Major:\n", major_stats)

# 5.2 Group by multiple columns
df_sales_data = pd.DataFrame({
    'Region': ['East', 'East', 'West', 'West', 'East'],
    'Product': ['A', 'B', 'A', 'B', 'A'],
    'Sales': [100, 150, 200, 120, 130],
    'Units': [10, 15, 20, 12, 13]
})
print("\nSales Data:\n", df_sales_data)

sales_by_region_product = df_sales_data.groupby(['Region', 'Product']).sum()
print("\nTotal Sales and Units by Region and Product:\n", sales_by_region_product)

# 5.3 Using .apply() with groupby for custom aggregation
def gpa_range(series):
    return series.max() - series.min()

gpa_ranges_by_major = df_students.groupby('Major')['GPA'].apply(gpa_range)
print("\nGPA Range by Major (using apply with groupby):\n", gpa_ranges_by_major)



print("\n--- 6. Reshaping DataFrames ---")

# 6.1 Pivoting data (from long to wide format)
# Create a dummy DataFrame suitable for pivoting
df_pivot_data = pd.DataFrame({
    'Year': [2020, 2020, 2021, 2021, 2022, 2022],
    'Quarter': ['Q1', 'Q2', 'Q1', 'Q2', 'Q1', 'Q2'],
    'Sales': [100, 120, 150, 130, 180, 160]
})
print("\nOriginal DataFrame for pivoting:\n", df_pivot_data)

# Pivot 'Quarter' column to be new columns
df_pivoted = df_pivot_data.pivot(index='Year', columns='Quarter', values='Sales')
print("\nPivoted DataFrame (Sales by Year and Quarter):\n", df_pivoted)

# 6.2 Stacking and Unstacking (for MultiIndex)
print("\nOriginal MultiIndex DataFrame (df_multi_index):\n", df_multi_index)

# Unstack the inner-most level of index
df_unstacked = df_multi_index.unstack()
print("\nUnstacked DataFrame (from MultiIndex):\n", df_unstacked)

# Stack (opposite of unstack)
df_stacked = df_unstacked.stack()
print("\nStacked DataFrame (back to MultiIndex):\n", df_stacked)

# 6.3 Melting data (from wide to long format)
df_wide = pd.DataFrame({
    'ID': ['A', 'B'],
    'Math_Score': [90, 85],
    'Science_Score': [75, 88]
})
print("\nWide format DataFrame:\n", df_wide)

df_long = df_wide.melt(id_vars=['ID'], var_name='Subject', value_name='Score')
print("\nLong format DataFrame (melted):\n", df_long)



print("\n--- 7. Iterating over DataFrames (Use with Caution for Large Data) ---")

# Iterating is generally less efficient than vectorized operations for large datasets.
# Prefer vectorized operations whenever possible.

print("\n--- Iterating over Rows (iterrows) ---")
for index, row in df_students.iterrows():
    print(f"Index: {index}, Name: {row['Name']}, Major: {row['Major']}")

print("\n--- Iterating over Columns (items) ---")
for column_name, column_series in df_students.items():
    print(f"\nColumn: {column_name}")
    print(column_series.head(2)) # Print first 2 elements of each Series

print("\n--- Iterating over Rows (itertuples) - often faster than iterrows ---")
# Access elements by attribute or index
for row_tuple in df_students.itertuples(index=False): # index=False means first element is not index
    print(f"Student: {row_tuple.Name}, GPA: {row_tuple.GPA}")



print("\n--- 8. Data Type Conversion ---")

df_types = pd.DataFrame({
    'Col1': ['1', '2', '3'], # strings
    'Col2': [1.0, 2.5, 3.0], # floats
    'Col3': ['True', 'False', 'True'] # strings
})
print("\nOriginal DataFrame types:\n", df_types.dtypes)

# Convert 'Col1' to integer
df_types['Col1'] = df_types['Col1'].astype(int)

# Convert 'Col3' to boolean
df_types['Col3'] = df_types['Col3'].astype(bool)

print("\nDataFrame types after conversion:\n", df_types.dtypes)
print("\nDataFrame after conversion:\n", df_types)

# Using to_numeric for more robust conversion, especially with errors
mixed_col = pd.Series(['1', '2', 'abc', '4'])
print(f"\nOriginal mixed_col: {mixed_col.tolist()}")
# mixed_col_int = pd.to_numeric(mixed_col) # This would raise an error
mixed_col_numeric_coerce = pd.to_numeric(mixed_col, errors='coerce') # Converts errors to NaN
print(f"mixed_col converted with errors='coerce': {mixed_col_numeric_coerce.tolist()}")


print("\n--- End of Pandas DataFrame Practice ---")