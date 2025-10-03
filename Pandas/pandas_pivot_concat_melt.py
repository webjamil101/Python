import pandas as pd
import numpy as np

print("--- Pandas melt(), concat(), pivot_table() Practice Code ---")

# --- 1. Introduction: Data Setup ---
print("\n--- 1. Data Setup ---")

# Data for melt(): Imagine quarterly sales data in wide format
data_wide_sales = {
    'Region': ['North', 'South', 'East', 'West'],
    'Sales_Q1': [100, 150, 120, 90],
    'Sales_Q2': [110, 160, 130, 95],
    'Sales_Q3': [125, 170, 135, 100],
    'Sales_Q4': [130, 180, 140, 105],
    'Profit_Q1': [20, 25, 22, 18],
    'Profit_Q2': [21, 26, 23, 19]
}
df_wide_sales = pd.DataFrame(data_wide_sales)
print("Original Wide Sales DataFrame (df_wide_sales):\n", df_wide_sales)

# Data for concat(): Imagine monthly performance reports from different departments
data_dept_a = {
    'Month': ['Jan', 'Feb', 'Mar'],
    'Department': ['A', 'A', 'A'],
    'Revenue': [5000, 5200, 5100],
    'Expenses': [2000, 2100, 2050]
}
df_dept_a = pd.DataFrame(data_dept_a)

data_dept_b = {
    'Month': ['Jan', 'Feb', 'Mar'],
    'Department': ['B', 'B', 'B'],
    'Revenue': [3000, 3100, 3050],
    'Expenses': [1500, 1550, 1520]
}
df_dept_b = pd.DataFrame(data_dept_b)

data_dept_c = {
    'Month': ['Jan', 'Feb', 'Mar'],
    'Department': ['C', 'C', 'C'],
    'Revenue': [4000, 4200, 4100],
    'Employees': [10, 11, 10] # Different column
}
df_dept_c = pd.DataFrame(data_dept_c)

print("\nDepartment A Data (df_dept_a):\n", df_dept_a)
print("\nDepartment B Data (df_dept_b):\n", df_dept_b)
print("\nDepartment C Data (df_dept_c - note different column):\n", df_dept_c)

# Data for pivot_table(): Imagine detailed transaction logs
data_transactions = {
    'TransactionID': np.arange(1, 15),
    'Date': pd.to_datetime(['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-01',
                            '2023-01-03', '2023-01-03', '2023-01-04', '2023-01-04', '2023-01-05',
                            '2023-01-05', '2023-01-06', '2023-01-06', '2023-01-07']),
    'Store': np.random.choice(['StoreA', 'StoreB', 'StoreC'], 14),
    'ProductType': np.random.choice(['Electronics', 'Groceries', 'Apparel'], 14),
    'Amount': np.random.uniform(10, 500, 14).round(2),
    'Quantity': np.random.randint(1, 5, 14),
    'PaymentMethod': np.random.choice(['Cash', 'Credit Card', 'Debit Card'], 14)
}
df_transactions = pd.DataFrame(data_transactions)
print("\nTransactions Data (df_transactions):\n", df_transactions.head())


print("\n--- 2. .melt(): Transforming Wide to Long Format ---")
# .melt() is used to "unpivot" a DataFrame from a wide format to a long format.
# It's useful when you have multiple columns representing measurements of the same variable
# over different periods or categories.

# 2.1 Basic Melt: Unpivoting Sales columns only
# `id_vars`: Columns to keep as identifier variables (won't be unpivoted).
# `value_vars`: Columns to unpivot (their values will go into one column, their names into another).
df_sales_long = df_wide_sales.melt(
    id_vars=['Region'],
    value_vars=['Sales_Q1', 'Sales_Q2', 'Sales_Q3', 'Sales_Q4'],
    var_name='Quarter',   # Name for the new column holding the original column names
    value_name='Sales'     # Name for the new column holding the values
)
print("\n2.1 Basic Melt (Sales only):\n", df_sales_long.head())

# 2.2 Melting multiple groups of variables (Sales and Profit)
# If you melt all `Q#_` columns, the 'Quarter_Type' column will contain 'Sales_Q1', 'Profit_Q1', etc.
df_all_metrics_melted = df_wide_sales.melt(
    id_vars=['Region'],
    var_name='Metric_Quarter',
    value_name='Value'
)
print("\n2.2 Melt all `Q#_` columns (intermediate step):\n", df_all_metrics_melted.head())

# Post-processing the melted data to separate Metric and Quarter
# This is a common step after melting if your original columns follow a pattern like `Metric_Quarter`
df_all_metrics_melted[['Metric', 'Quarter']] = df_all_metrics_melted['Metric_Quarter'].str.split('_', expand=True)
df_all_metrics_melted = df_all_metrics_melted.drop(columns=['Metric_Quarter'])
print("\n2.2 Melt and Split 'Metric_Quarter' into 'Metric' and 'Quarter':\n", df_all_metrics_melted.head())



print("\n--- 3. .concat(): Combining DataFrames ---")
# .concat() is used to stack DataFrames either vertically (rows) or horizontally (columns).
# It's essential for combining datasets that have similar structures or that need to be joined side-by-side.

# 3.1 Concatenating DataFrames vertically (axis=0, default)
# Stacks df_dept_a and df_dept_b. Missing columns will be filled with NaN.
df_combined_ab = pd.concat([df_dept_a, df_dept_b])
print("\n3.1 Concatenating df_dept_a and df_dept_b (vertical):\n", df_combined_ab)

# 3.2 Concatenating with different columns (Department C has 'Employees' instead of 'Expenses')
# Columns not present in all DataFrames will result in NaN where values are missing.
df_combined_all = pd.concat([df_dept_a, df_dept_b, df_dept_c])
print("\n3.2 Concatenating all departments (different columns handled with NaN):\n", df_combined_all)

# 3.3 Concatenating vertically and ignoring the original index
# Useful when you don't want duplicate index labels after concatenation.
df_combined_reset_index = pd.concat([df_dept_a, df_dept_b], ignore_index=True)
print("\n3.3 Concatenating with ignore_index=True:\n", df_combined_reset_index)

# 3.4 Concatenating horizontally (axis=1) - joining by index
# This is like a SQL JOIN on the index. Requires matching indices for meaningful results.
# Let's create two DataFrames with common indices for horizontal concatenation.
df_product_info = pd.DataFrame({
    'ProductType': ['Electronics', 'Groceries', 'Apparel'],
    'Avg_Price': [500, 50, 80]
}, index=['P_Elec', 'P_Groc', 'P_App']) # Custom index
df_warehouse_info = pd.DataFrame({
    'Warehouse': ['WH1', 'WH2', 'WH1'],
    'Location': ['NY', 'CA', 'TX']
}, index=['P_Elec', 'P_Groc', 'P_App']) # Matching custom index

df_horizontally_combined = pd.concat([df_product_info, df_warehouse_info], axis=1)
print("\n3.4 Concatenating two DataFrames horizontally (matching indices):\n", df_horizontally_combined)

# 3.5 Concatenating with keys: Creates a MultiIndex to identify source DataFrame
df_keyed_concat = pd.concat([df_dept_a, df_dept_b], keys=['DeptA', 'DeptB'])
print("\n3.5 Concatenating with keys (creates MultiIndex):\n", df_keyed_concat)
print("Accessing DeptA data from keyed concat:\n", df_keyed_concat.loc['DeptA'].head())



print("\n--- 4. .pivot_table(): Summarizing and Reshaping with Aggregation ---")
# .pivot_table() is extremely powerful. It allows you to transform data
# from a long format to a wide format, performing aggregations at the same time.

# 4.1 Basic Pivot Table: Total Amount by Store and ProductType
# `values`: Column(s) to aggregate.
# `index`: Column(s) to become new index (rows).
# `columns`: Column(s) to become new columns.
# `aggfunc`: Function to aggregate values (e.g., 'sum', 'mean', 'count'). Default is 'mean'.
df_sales_by_store_product = df_transactions.pivot_table(
    values='Amount',
    index='Store',
    columns='ProductType',
    aggfunc='sum',
    fill_value=0 # Replace NaN (missing combinations) with 0
)
print("\n4.1 Total Amount by Store and ProductType:\n", df_sales_by_store_product)

# 4.2 Pivot Table with multiple aggregation functions
# Calculate total amount and average quantity for each Store and ProductType.
df_multi_agg = df_transactions.pivot_table(
    values=['Amount', 'Quantity'], # Aggregate these two value columns
    index='Store',
    columns='ProductType',
    aggfunc={'Amount': 'sum', 'Quantity': 'mean'}, # Different functions for different values
    fill_value=0
)
print("\n4.2 Multi-Aggregation Pivot Table (Total Amount, Avg Quantity):\n", df_multi_agg)

# 4.3 Pivot Table with multiple index levels
# Summarize Amount by Date (rows) and then Store, with ProductType as columns
df_daily_store_product_sales = df_transactions.pivot_table(
    values='Amount',
    index=['Date', 'Store'], # Creates a MultiIndex for rows
    columns='ProductType',
    aggfunc='sum',
    fill_value=0
)
print("\n4.3 Pivot Table with MultiIndex Rows (Daily Sales by Store & ProductType):\n", df_daily_store_product_sales)

# 4.4 Pivot Table with margins (row/column totals)
df_sales_by_store_product_margins = df_transactions.pivot_table(
    values='Amount',
    index='Store',
    columns='ProductType',
    aggfunc='sum',
    fill_value=0,
    margins=True, # Adds row and column totals ('All' row/column)
    margins_name='Grand Total' # Custom name for margin rows/cols
)
print("\n4.4 Pivot Table with Margins:\n", df_sales_by_store_product_margins)

# 4.5 Applying a custom aggregation function
def custom_range(series):
    return series.max() - series.min() if not series.empty and series.max() is not np.nan and series.min() is not np.nan else np.nan

df_amount_range = df_transactions.pivot_table(
    values='Amount',
    index='Store',
    columns='ProductType',
    aggfunc=custom_range # Use our custom function
)
print("\n4.5 Pivot Table with Custom Aggregation (Amount Range):\n", df_amount_range)


print("\n--- End of Pandas melt(), concat(), pivot_table() Practice Code ---")