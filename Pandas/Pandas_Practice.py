import pandas as pd
import numpy as np

print("--- Pandas Practice Code ---")

# --- 1. Series Creation and Basic Operations ---
print("\n--- 1. Series ---")

# Create a Series from a list
s_list = pd.Series([10, 20, 30, 40, 50])
print("\nSeries from list:\n", s_list)

# Create a Series with a custom index
s_indexed = pd.Series([100, 200, 300], index=['a', 'b', 'c'])
print("\nSeries with custom index:\n", s_indexed)

# Access elements
print("\nAccessing element at index 'b':", s_indexed['b'])
print("Accessing element at position 0:", s_list[0])

# Basic arithmetic operations
print("\ns_list + 5:\n", s_list + 5)
print("s_indexed * 2:\n", s_indexed * 2)

# Conditional selection
print("\nElements in s_list greater than 30:\n", s_list[s_list > 30])


# --- 2. DataFrame Creation ---
print("\n--- 2. DataFrame Creation ---")

# Create a DataFrame from a dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'London', 'Paris', 'Tokyo']
}
df = pd.DataFrame(data)
print("\nDataFrame from dictionary:\n", df)

# Create a DataFrame from a list of dictionaries
data_list_dict = [
    {'Product': 'Laptop', 'Price': 1200, 'Quantity': 5},
    {'Product': 'Mouse', 'Price': 25, 'Quantity': 50},
    {'Product': 'Keyboard', 'Price': 75, 'Quantity': 20}
]
df_products = pd.DataFrame(data_list_dict)
print("\nDataFrame from list of dictionaries:\n", df_products)

# Create a DataFrame with a custom index
df_custom_index = pd.DataFrame(data, index=['user1', 'user2', 'user3', 'user4'])
print("\nDataFrame with custom index:\n", df_custom_index)


# --- 3. Data Inspection ---
print("\n--- 3. Data Inspection ---")

print("\nFirst 3 rows (df.head(3)):\n", df.head(3))
print("\nLast 2 rows (df.tail(2)):\n", df.tail(2))
print("\nDataFrame info (df.info()):")
df.info()
print("\nDescriptive statistics (df.describe()):\n", df.describe())
print("\nShape of df (rows, columns):", df.shape)
print("Column names of df:", df.columns.tolist())
print("Data types of df columns:\n", df.dtypes)
print("\nUnique cities in df:", df['City'].unique())
print("Value counts for City in df:\n", df['City'].value_counts())


# --- 4. Selecting Data ---
print("\n--- 4. Selecting Data ---")

# Select a single column (returns a Series)
names = df['Name']
print("\n'Name' column:\n", names)

# Select multiple columns (returns a DataFrame)
name_city = df[['Name', 'City']]
print("\n'Name' and 'City' columns:\n", name_city)

# Select rows by label using .loc[]
print("\nRow with custom index 'user2' (df_custom_index.loc['user2']):\n", df_custom_index.loc['user2'])
print("\nRows 'user1' and 'user4' (df_custom_index.loc[['user1', 'user4']]):\n", df_custom_index.loc[['user1', 'user4']])

# Select rows by integer position using .iloc[]
print("\nFirst row by integer position (df.iloc[0]):\n", df.iloc[0])
print("\nRows from position 1 to 2 (df.iloc[1:3]):\n", df.iloc[1:3])

# Select specific rows and columns using .loc[] (label-based)
print("\nAge for 'user1' and 'user3' (df_custom_index.loc[['user1', 'user3'], 'Age']):\n", df_custom_index.loc[['user1', 'user3'], 'Age'])

# Select specific rows and columns using .iloc[] (integer-position based)
print("\nName for first two rows (df.iloc[0:2, 0]):\n", df.iloc[0:2, 0])


# --- 5. Filtering Data (Conditional Selection) ---
print("\n--- 5. Filtering Data ---")

# Filter rows where Age is greater than 28
older_than_28 = df[df['Age'] > 28]
print("\nRows where Age > 28:\n", older_than_28)

# Filter rows for a specific city
from_london = df[df['City'] == 'London']
print("\nRows where City is 'London':\n", from_london)

# Multiple conditions (AND - &)
young_in_ny = df[(df['Age'] < 30) & (df['City'] == 'New York')]
print("\nRows where Age < 30 AND City is 'New York':\n", young_in_ny)

# Multiple conditions (OR - |)
ny_or_paris = df[(df['City'] == 'New York') | (df['City'] == 'Paris')]
print("\nRows where City is 'New York' OR 'Paris':\n", ny_or_paris)

# Using .isin() for multiple values
cities_of_interest = df[df['City'].isin(['New York', 'Tokyo'])]
print("\nRows where City is 'New York' or 'Tokyo':\n", cities_of_interest)


# --- 6. Handling Missing Data ---
print("\n--- 6. Handling Missing Data ---")

df_missing = pd.DataFrame({
    'Col1': [1, 2, np.nan, 4],
    'Col2': [5, np.nan, 7, 8],
    'Col3': [9, 10, 11, np.nan],
    'Col4': [np.nan, np.nan, np.nan, np.nan] # All missing
})
print("\nDataFrame with missing values:\n", df_missing)

# Check for missing values
print("\nMissing values (df_missing.isnull()):\n", df_missing.isnull())

# Count missing values per column
print("\nMissing values count per column:\n", df_missing.isnull().sum())

# Drop rows with any missing values
df_dropped_rows = df_missing.dropna()
print("\nDataFrame after dropping rows with NaN:\n", df_dropped_rows)

# Drop columns with any missing values
df_dropped_cols = df_missing.dropna(axis=1) # axis=1 for columns
print("\nDataFrame after dropping columns with NaN:\n", df_dropped_cols)

# Fill missing values with a specific value
df_filled_zero = df_missing.fillna(0)
print("\nDataFrame after filling NaN with 0:\n", df_filled_zero)

# Fill missing values with the mean of the column
df_filled_mean_col1 = df_missing['Col1'].fillna(df_missing['Col1'].mean())
print("\nCol1 after filling NaN with its mean:\n", df_filled_mean_col1)

# Fill all missing values with the mean of their respective columns
df_filled_all_means = df_missing.fillna(df_missing.mean(numeric_only=True))
print("\nDataFrame after filling all NaNs with column means:\n", df_filled_all_means)

# Forward fill (propagates last valid observation forward)
df_ffill = df_missing.fillna(method='ffill')
print("\nDataFrame after forward fill (ffill):\n", df_ffill)

# Backward fill (propagates next valid observation backward)
df_bfill = df_missing.fillna(method='bfill')
print("\nDataFrame after backward fill (bfill):\n", df_bfill)


# --- 7. Grouping and Aggregating Data (.groupby()) ---
print("\n--- 7. Grouping and Aggregating ---")

data_sales = {
    'Region': ['East', 'West', 'East', 'West', 'East', 'Central', 'Central', 'East'],
    'Product': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'A'],
    'Sales': [100, 150, 120, 80, 200, 90, 110, 130]
}
df_sales = pd.DataFrame(data_sales)
print("\nOriginal Sales DataFrame:\n", df_sales)

# Group by 'Region' and calculate the sum of 'Sales'
sales_by_region = df_sales.groupby('Region')['Sales'].sum()
print("\nTotal Sales by Region:\n", sales_by_region)

# Group by 'Product' and calculate the average sales
avg_sales_by_product = df_sales.groupby('Product')['Sales'].mean()
print("\nAverage Sales by Product:\n", avg_sales_by_product)

# Group by multiple columns and calculate multiple aggregations
multi_agg = df_sales.groupby(['Region', 'Product']).agg(
    Total_Sales=('Sales', 'sum'),
    Average_Sales=('Sales', 'mean'),
    Count=('Sales', 'count')
)
print("\nMulti-level Aggregations by Region and Product:\n", multi_agg)

# Reset index after groupby
print("\nMulti-level Aggregations (reset index):\n", multi_agg.reset_index())


# --- 8. Merging and Joining DataFrames (.merge()) ---
print("\n--- 8. Merging and Joining ---")

df_customers = pd.DataFrame({
    'customer_id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David']
})

df_orders = pd.DataFrame({
    'order_id': [101, 102, 103, 104, 105],
    'customer_id': [1, 3, 2, 1, 5], # customer_id 5 not in df_customers
    'amount': [50, 75, 30, 120, 90]
})

print("\nCustomers DataFrame:\n", df_customers)
print("\nOrders DataFrame:\n", df_orders)

# Inner merge (default): only common customer_ids
merged_inner = pd.merge(df_customers, df_orders, on='customer_id', how='inner')
print("\nInner Merge:\n", merged_inner)

# Left merge: all customers, matching orders (NaN for no match)
merged_left = pd.merge(df_customers, df_orders, on='customer_id', how='left')
print("\nLeft Merge:\n", merged_left)

# Right merge: all orders, matching customers (NaN for no match)
merged_right = pd.merge(df_customers, df_orders, on='customer_id', how='right')
print("\nRight Merge:\n", merged_right)

# Outer merge: all rows from both (NaN where no match)
merged_outer = pd.merge(df_customers, df_orders, on='customer_id', how='outer')
print("\nOuter Merge:\n", merged_outer)


# --- 9. Concatenating DataFrames (.concat()) ---
print("\n--- 9. Concatenating ---")

df_part1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df_part2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
df_part3 = pd.DataFrame({'C': [9, 10], 'D': [11, 12]}) # Different columns

print("\nDataFrame Part 1:\n", df_part1)
print("\nDataFrame Part 2:\n", df_part2)
print("\nDataFrame Part 3 (different columns):\n", df_part3)

# Concatenate rows (default axis=0)
concatenated_rows = pd.concat([df_part1, df_part2])
print("\nConcatenated rows (axis=0):\n", concatenated_rows)

# Concatenate columns (axis=1) - fills NaN for non-matching rows/indices
concatenated_cols = pd.concat([df_part1, df_part3], axis=1)
print("\nConcatenated columns (axis=1):\n", concatenated_cols)

# Concatenate with ignore_index=True to reset index
concatenated_rows_reset = pd.concat([df_part1, df_part2], ignore_index=True)
print("\nConcatenated rows (ignore_index=True):\n", concatenated_rows_reset)


# --- 10. Applying Functions ---
print("\n--- 10. Applying Functions ---")

df_apply = pd.DataFrame({
    'A': [10, 20, 30],
    'B': [1, 2, 3]
})
print("\nOriginal DataFrame for apply:\n", df_apply)

# Apply a function to a single column (Series.apply)
df_apply['A_squared'] = df_apply['A'].apply(lambda x: x**2)
print("\nColumn 'A_squared' added:\n", df_apply)

# Apply a function row-wise (axis=1) (DataFrame.apply)
# Sum 'A' and 'B' for each row
df_apply['Sum_AB'] = df_apply.apply(lambda row: row['A'] + row['B'], axis=1)
print("\nColumn 'Sum_AB' added (row-wise apply):\n", df_apply)

# Apply a function to each element (DataFrame.applymap / Series.map)
df_apply_mapped = df_apply[['A', 'B']].applymap(lambda x: x * 10)
print("\nElements in A, B multiplied by 10 (applymap):\n", df_apply_mapped)

# For Series, use .map()
s_map = pd.Series(['apple', 'banana', 'cherry'])
s_mapped = s_map.map(lambda x: x.upper())
print("\nSeries with .map() (to uppercase):\n", s_mapped)


print("\n--- End of Pandas Practice ---")