import pandas as pd
import numpy as np

print("--- Pandas Subsetting Observations (Rows & Columns) Practice Code ---")

# --- 1. Setup: Create a Rich Sample DataFrame ---
print("\n--- 1. Sample DataFrame Setup ---")

data = {
    'OrderID': np.arange(1001, 1021),
    'CustomerID': np.random.randint(100, 105, 20),
    'ProductCategory': np.random.choice(['Electronics', 'Books', 'Clothing', 'Food'], 20),
    'Quantity': np.random.randint(1, 10, 20),
    'Price_USD': np.random.uniform(5.0, 1500.0, 20).round(2),
    'OrderDate': pd.to_datetime(pd.date_range(start='2024-01-01', periods=20, freq='D')),
    'Discount_Applied': np.random.choice([0.0, 0.1, 0.15, np.nan], 20, p=[0.3, 0.3, 0.2, 0.2]),
    'IsExpressShipping': np.random.choice([True, False], 20),
    'Customer_Rating': np.random.randint(1, 6, 20), # 1 to 5 stars
    'Item_Weight_kg': np.random.uniform(0.1, 5.0, 20).round(1) # Column with underscores
}
df = pd.DataFrame(data)

# Introduce some missing values for practice
df.loc[[2, 5, 12], 'Quantity'] = np.nan
df.loc[[1, 8, 11], 'Customer_Rating'] = np.nan
df.loc[15, 'ProductCategory'] = np.nan

# Set a custom index for demonstrating label-based row selection
df = df.set_index('OrderID')

print("Original DataFrame (df):\n", df.head())
print("\nDataFrame Info (showing dtypes and non-null counts):\n")
df.info()


print("\n--- 2. Selecting Columns ---")

# 2.1 Select a single column (returns a Series)
product_category_series = df['ProductCategory']
print("\nProductCategory Series (first 5):\n", product_category_series.head())
print("Type of single column selection:", type(product_category_series))

# 2.2 Select multiple columns (returns a DataFrame)
# Use a list of column names
selected_cols_df = df[['Quantity', 'Price_USD', 'Total_Price_USD']] # Assuming Total_Price_USD exists from previous setup or you create it.
df['Total_Price_USD'] = df['Quantity'] * df['Price_USD'] * (1 - df['Discount_Applied'].fillna(0)) # Ensure it exists
selected_cols_df = df[['Quantity', 'Price_USD', 'Total_Price_USD']]
print("\nSelected 'Quantity', 'Price_USD', 'Total_Price_USD' columns:\n", selected_cols_df.head())
print("Type of multiple column selection:", type(selected_cols_df))

# 2.3 Select columns by data type using .select_dtypes()
numerical_cols_df = df.select_dtypes(include=np.number)
print("\nNumerical columns using .select_dtypes(include=np.number):\n", numerical_cols_df.head())

object_bool_cols_df = df.select_dtypes(include=['object', 'bool'])
print("\nObject and Boolean columns using .select_dtypes(include=['object', 'bool']):\n", object_bool_cols_df.head())

# 2.4 Exclude columns by data type
exclude_numeric_cols_df = df.select_dtypes(exclude=np.number)
print("\nColumns excluding numerical using .select_dtypes(exclude=np.number):\n", exclude_numeric_cols_df.head())


print("\n--- 3. Selecting Rows (using .loc[] and .iloc[]) ---")

# 3.1 .loc[]: Selection by label (index label or column label)
# Select a single row by its index label (OrderID)
single_row_loc = df.loc[1005]
print("\nRow with OrderID 1005 (using .loc[]):\n", single_row_loc)

# Select multiple rows by a list of index labels
multiple_rows_loc = df.loc[[1001, 1003, 1007]]
print("\nRows with OrderID 1001, 1003, 1007 (using .loc[]):\n", multiple_rows_loc)

# Select a slice of rows by index labels (inclusive of end label)
slice_rows_loc = df.loc[1005:1010]
print("\nRows with OrderID from 1005 to 1010 (inclusive, using .loc[]):\n", slice_rows_loc)

# 3.2 .iloc[]: Selection by integer position (0-based)
# Select a single row by its integer position
single_row_iloc = df.iloc[0] # First row
print("\nFirst row (using .iloc[0]):\n", single_row_iloc)

# Select multiple rows by a list of integer positions
multiple_rows_iloc = df.iloc[[0, 2, 6]]
print("\nRows at positions 0, 2, 6 (using .iloc[]):\n", multiple_rows_iloc)

# Select a slice of rows by integer positions (exclusive of end position)
slice_rows_iloc = df.iloc[4:8] # Rows at positions 4, 5, 6, 7
print("\nRows at positions 4 to 7 (exclusive of 8, using .iloc[]):\n", slice_rows_iloc)


print("\n--- 4. Selecting Rows with Boolean Indexing (Conditional Selection) ---")

# 4.1 Single condition: Orders with Price_USD > 1000
high_price_orders = df[df['Price_USD'] > 1000]
print("\nOrders with Price_USD > 1000:\n", high_price_orders)

# 4.2 Multiple conditions (AND - use &)
electronics_high_qty = df[(df['ProductCategory'] == 'Electronics') & (df['Quantity'] >= 2)]
print("\nElectronics orders with Quantity >= 2:\n", electronics_high_qty)

# 4.3 Multiple conditions (OR - use |)
books_or_food = df[(df['ProductCategory'] == 'Books') | (df['ProductCategory'] == 'Food')]
print("\nOrders that are 'Books' OR 'Food':\n", books_or_food.head())

# 4.4 Using .isin() for multiple matches in a column
target_customers = [101, 103]
specific_customer_orders = df[df['CustomerID'].isin(target_customers)]
print("\nOrders by CustomerID 101 or 103 (using .isin()):\n", specific_customer_orders.head())

# 4.5 Selecting rows where a column is null/not null
orders_with_discount_missing = df[df['Discount_Applied'].isnull()]
print("\nOrders where Discount_Applied is missing:\n", orders_with_discount_missing)

orders_with_discount_applied = df[df['Discount_Applied'].notnull()]
print("\nOrders where Discount_Applied is not missing:\n", orders_with_discount_applied.head())


print("\n--- 5. Selecting Rows and Columns Simultaneously ---")

# 5.1 Using .loc[row_labels, col_labels]
# Select specific rows by label and specific columns by label
specific_data_loc = df.loc[[1001, 1005, 1010], ['Quantity', 'Price_USD', 'Total_Price_USD']]
print("\nSpecific rows and columns (using .loc[]):\n", specific_data_loc)

# Select rows based on a condition and specific columns
high_rating_data = df.loc[df['Customer_Rating'] >= 4, ['CustomerID', 'ProductCategory', 'Customer_Rating', 'Total_Price_USD']]
print("\nRows with Customer_Rating >= 4, and selected columns (using .loc[] with boolean):\n", high_rating_data.head())

# Select a slice of rows by label and all columns
slice_rows_all_cols = df.loc[1003:1007, :]
print("\nSlice of rows (1003 to 1007) and all columns (using .loc[]):\n", slice_rows_all_cols)

# 5.2 Using .iloc[row_positions, col_positions]
# Select specific rows by position and specific columns by position
specific_data_iloc = df.iloc[[0, 4, 9], [3, 4, 10]] # Quantity, Price_USD, Total_Price_USD
print("\nSpecific rows and columns by position (using .iloc[]):\n", specific_data_iloc)

# Select a slice of rows by position and a slice of columns by position
slice_rows_slice_cols_iloc = df.iloc[5:10, 0:5] # Rows 5-9, first 5 columns
print("\nSlice of rows and slice of columns by position (using .iloc[]):\n", slice_rows_slice_cols_iloc)


print("\n--- 6. Advanced/Specialized Subsetting Methods ---")

# 6.1 .head() and .tail(): Top/Bottom N rows
print("\nFirst 3 rows (df.head(3)):\n", df.head(3))
print("\nLast 2 rows (df.tail(2)):\n", df.tail(2))

# 6.2 .sample(): Random sampling of rows
random_sample_5 = df.sample(n=5, random_state=42) # random_state for reproducibility
print("\nRandom sample of 5 rows (df.sample(n=5)):\n", random_sample_5)

# Sample a percentage of rows
random_sample_frac = df.sample(frac=0.2, random_state=42) # 20% of rows
print("\nRandom sample of 20% of rows (df.sample(frac=0.2)):\n", random_sample_frac)

# 6.3 .at[] and .iat[]: Fast scalar (single value) access
# .at[]: label-based scalar access
price_at_1005 = df.at[1005, 'Price_USD']
print(f"\nPrice_USD for OrderID 1005 (using .at[]): {price_at_1005}")

# .iat[]: integer-position-based scalar access
price_at_0_4 = df.iat[0, 4] # First row, 5th column (Price_USD)
print(f"Price_USD for row 0, col 4 (using .iat[]): {price_at_0_4}")

# 6.4 .filter(): Select rows/columns based on label patterns
# Select columns containing 'Price'
filtered_cols_by_pattern = df.filter(like='Price', axis=1)
print("\nColumns containing 'Price' (using .filter(like='Price', axis=1)):\n", filtered_cols_by_pattern.head())

# Select rows with index labels containing '005'
filtered_rows_by_pattern = df.filter(like='005', axis=0)
print("\nRows with OrderID containing '005' (using .filter(like='005', axis=0)):\n", filtered_rows_by_pattern)


print("\n--- 7. Using .query() for Row Subsetting (for readability) ---")
# .query() is a powerful way to filter rows based on a string expression.
# (More details were covered in a separate 'pandas query' practice)

# Select orders with high quantity and good rating
query_result = df.query('Quantity > 5 and Customer_Rating >= 4')
print("\nOrders with Quantity > 5 AND Customer_Rating >= 4 (using .query()):\n", query_result.head())

# Query involving column with special characters (must use backticks)
query_special_char_col = df.query('`Item_Weight_kg` < 1.0 and IsExpressShipping == True')
print("\nOrders with Item_Weight_kg < 1.0 AND Express Shipping (using .query() with backticks):\n", query_special_char_col.head())

print("\n--- End of Pandas Subsetting Observations Code ---")