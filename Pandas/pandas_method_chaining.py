import pandas as pd
import numpy as np

print("--- Pandas Method Chaining Practice Code ---")

# --- 1. Setup: Create a Sample DataFrame ---
print("\n--- 1. Sample DataFrame Setup ---")

# Data for a hypothetical customer order history
data = {
    'OrderID': range(1001, 1021),
    'CustomerID': np.random.randint(10, 20, 20),
    'Product': np.random.choice(['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Webcam'], 20),
    'Quantity': np.random.randint(1, 5, 20),
    'Price_Per_Unit': np.random.uniform(20, 1500, 20).round(2),
    'OrderDate': pd.to_datetime(pd.date_range(start='2024-01-01', periods=20, freq='D')),
    'Discount_Code': np.random.choice(['SAVE10', 'SAVE20', None], 20, p=[0.2, 0.2, 0.6]),
    'Shipping_Cost': np.random.uniform(5, 20, 20).round(2)
}
df = pd.DataFrame(data)

# Introduce some missing values and duplicates for realistic cleaning scenarios
df.loc[[2, 5, 12], 'Price_Per_Unit'] = np.nan
df.loc[15, 'Quantity'] = np.nan
df.loc[[7, 10], 'CustomerID'] = 12 # Create duplicate customer for specific filtering
df = pd.concat([df, df.iloc[[0]].copy()], ignore_index=True) # Add a full duplicate row

print("Original DataFrame (df):\n", df)
print("\nDataFrame Info (showing dtypes and non-null counts):\n")
df.info()


print("\n--- 2. Basic Chaining: Filtering, Selecting, Sorting ---")

# Non-chained approach
# temp_df = df[df['Quantity'].notna()]
# temp_df = temp_df[temp_df['Price_Per_Unit'].notna()]
# high_value_orders = temp_df[temp_df['Price_Per_Unit'] * temp_df['Quantity'] > 1000]
# sorted_orders = high_value_orders.sort_values(by='OrderDate', ascending=False)
# final_result = sorted_orders[['OrderID', 'CustomerID', 'Product', 'Quantity', 'Price_Per_Unit']]

# Chained approach: Get top 5 recent high-value orders (Total Price > 1000)
# (1) Drop rows with NaN in critical columns (Quantity, Price_Per_Unit)
# (2) Calculate Total_Price
# (3) Filter for Total_Price > 1000
# (4) Sort by OrderDate descending
# (5) Select relevant columns and get top 5
top_recent_high_value_orders = (
    df.dropna(subset=['Quantity', 'Price_Per_Unit'])
    .assign(Total_Price=lambda x: x['Quantity'] * x['Price_Per_Unit'])
    .query('Total_Price > 1000')
    .sort_values(by='OrderDate', ascending=False)
    .head(5)
    [['OrderID', 'CustomerID', 'Product', 'Total_Price', 'OrderDate']]
)
print("\nTop 5 Recent High-Value Orders (Chained):\n", top_recent_high_value_orders)


print("\n--- 3. Chaining with .assign() - Adding/Modifying Columns ---")
# .assign() is excellent for creating new columns in a chain.

# Calculate Total Price and Commission_Amount, then select columns
df_with_calculations = (
    df.dropna(subset=['Quantity', 'Price_Per_Unit']) # Ensure calculations are on valid numbers
    .assign(
        Total_Price=lambda x: x['Quantity'] * x['Price_Per_Unit'],
        Commission_Amount=lambda x: x['Total_Price'] * x['Commission_Rate'].fillna(0) # Handle None in Discount_Code
    )
    [['OrderID', 'Product', 'Quantity', 'Price_Per_Unit', 'Total_Price', 'Commission_Amount']]
)
print("\nDataFrame with Total_Price and Commission_Amount (using assign):\n", df_with_calculations.head())

# Assigning multiple new columns simultaneously
df_complex_assign = (
    df.assign(
        Is_Laptop=lambda x: x['Product'] == 'Laptop',
        Net_Price=lambda x: x['Price_Per_Unit'] - (x['Price_Per_Unit'] * (0.1 if 'SAVE10' in str(x['Discount_Code']) else (0.2 if 'SAVE20' in str(x['Discount_Code']) else 0))),
        # Calculate approximate order month
        Order_Month=lambda x: x['OrderDate'].dt.month_name()
    )
    [['OrderID', 'Product', 'Is_Laptop', 'Discount_Code', 'Net_Price', 'Order_Month']]
)
print("\nDataFrame with multiple new columns (complex assign):\n", df_complex_assign.head())


print("\n--- 4. Chaining with .pipe() - Applying Custom or Non-DataFrame-Returning Functions ---")
# .pipe() allows you to insert custom functions or functions that don't return a DataFrame/Series
# (or return something different than expected in a chain)

def filter_by_product_category(df_in, product_name):
    """Custom function to filter DataFrame by product."""
    return df_in[df_in['Product'] == product_name]

def analyze_commissions(df_in):
    """Custom function to perform a specific analysis and return a result."""
    df_temp = df_in.dropna(subset=['Commission_Amount'])
    return df_temp['Commission_Amount'].sum()

# Chaining with a custom filter function via .pipe()
laptop_orders = (
    df.dropna(subset=['Quantity', 'Price_Per_Unit'])
    .assign(Total_Price=lambda x: x['Quantity'] * x['Price_Per_Unit'])
    .pipe(filter_by_product_category, 'Laptop') # Apply custom filter
    [['OrderID', 'Product', 'Total_Price']]
)
print("\nLaptop Orders (filtered using .pipe() with custom function):\n", laptop_orders)

# Chaining with .pipe() to get a single scalar result after a chain
total_commission_sum = (
    df.dropna(subset=['Quantity', 'Price_Per_Unit'])
    .assign(
        Total_Price=lambda x: x['Quantity'] * x['Price_Per_Unit'],
        Commission_Amount=lambda x: x['Total_Price'] * x['Commission_Rate'].fillna(0)
    )
    .pipe(analyze_commissions) # Apply custom analysis function that returns a scalar
)
print(f"\nTotal Commission Sum (using .pipe() for final aggregation): {total_commission_sum:.2f}")


print("\n--- 5. Chaining for Data Cleaning and Transformation ---")

# Clean, deduplicate, fill NaNs, and calculate total value per order
cleaned_and_transformed_df = (
    df.drop_duplicates(subset=['CustomerID', 'OrderDate', 'Product']) # Drop exact duplicates of core order info
    .dropna(subset=['Quantity', 'Price_Per_Unit']) # Drop rows where essential calculation values are missing
    .fillna({'Discount_Code': 'NONE', 'Shipping_Cost': df['Shipping_Cost'].mean()}) # Fill remaining NaNs
    .assign(
        Total_Order_Value=lambda x: x['Quantity'] * x['Price_Per_Unit'] + x['Shipping_Cost']
    )
    [['OrderID', 'CustomerID', 'Product', 'Quantity', 'Total_Order_Value', 'Discount_Code']]
)
print("\nCleaned and Transformed DataFrame (Chained Cleaning):\n", cleaned_and_transformed_df.head(10))


print("\n--- 6. Chaining with GroupBy and Aggregations ---")

# Get total sales and average quantity per customer and product, sorted by total sales
customer_product_summary = (
    df.dropna(subset=['Quantity', 'Sales_Amount'], how='all') # Drop if both are NaN (or just one if it's essential for group key)
    .groupby(['CustomerID', 'Product']) # Group by two columns
    .agg(
        TotalSales=('Sales_Amount', 'sum'), # Named aggregation
        AverageQuantity=('Quantity', 'mean'),
        NumOrders=('OrderID', 'count')
    )
    .reset_index() # Convert MultiIndex back to columns
    .sort_values(by='TotalSales', ascending=False) # Sort the aggregated result
)
print("\nCustomer-Product Summary (Chained GroupBy):\n", customer_product_summary.head())

# Group by region and find the top product by total sales within each region
top_product_per_region = (
    df.dropna(subset=['Sales_Amount'])
    .groupby('Region')
    .apply(lambda x: x.loc[x['Sales_Amount'].idxmax()]) # Apply a function to each group to get row with max sales
    .reset_index(drop=True) # Reset index and drop the old region index
    [['Region', 'Product', 'Sales_Amount', 'Salesperson']]
)
print("\nTop Product by Sales within Each Region:\n", top_product_per_region)


print("\n--- 7. Readability in Chaining: Using Parentheses and Indentation ---")
# Always wrap multi-line chains in parentheses and use consistent indentation.

# Bad readability (don't do this for long chains):
# result = df.dropna(subset=['Quantity', 'Price_Per_Unit']).assign(Total_Price=lambda x: x['Quantity'] * x['Price_Per_Unit']).query('Total_Price > 500').sort_values(by='Total_Price', ascending=False).head(3)

# Good readability (preferred):
readable_chain = (
    df
    .dropna(subset=['Quantity', 'Price_Per_Unit']) # Step 1: Clean data
    .assign(
        Total_Price=lambda x: x['Quantity'] * x['Price_Per_Unit'], # Step 2: Add calculated column
        Estimated_Revenue=lambda x: x['Total_Price'] * (1 - x['Commission_Rate'].fillna(0)) # Step 3: Another calculated column
    )
    .query('Total_Price > 500') # Step 4: Filter based on new column
    .sort_values(by='Estimated_Revenue', ascending=False) # Step 5: Sort results
    .head(3) # Step 6: Get top N
    [['OrderID', 'Product', 'Total_Price', 'Estimated_Revenue']] # Step 7: Select final columns
)
print("\nReadable Chained Operation:\n", readable_chain)


print("\n--- 8. Cautions with Chaining ---")

# 8.1 In-place operations: Methods like .fillna(inplace=True) break the chain.
# Always use methods that return a DataFrame/Series for chaining.
# Example: df.fillna(value=0, inplace=True) would not work in a chain.
# Use: df.fillna(value=0) instead.

# 8.2 Debugging: Long chains can be hard to debug.
# Break them down temporarily or use .pipe(lambda x: x.debug_print_or_breakpoint())
# or print intermediate results for debugging.
# Example:
# debug_chain = (
#     df.dropna(subset=['Quantity'])
#     .assign(Value=lambda x: x['Quantity'] * x['Price_Per_Unit'])
#     .pipe(lambda x: (print("After assign:\n", x.head()), x)[1]) # Print intermediate state
#     .query('Value > 100')
# )


print("\n--- End of Pandas Method Chaining Practice ---")