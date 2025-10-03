import pandas as pd
import numpy as np

print("--- Pandas .query() Method Practice Code ---")

# --- 1. Setup: Create a Sample DataFrame ---
print("\n--- 1. Sample DataFrame Setup ---")

data = {
    'OrderID': np.arange(1001, 1021),
    'CustomerID': np.random.randint(100, 105, 20),
    'ProductCategory': np.random.choice(['Electronics', 'Books', 'Clothing', 'Food'], 20),
    'Quantity': np.random.randint(1, 10, 20),
    'Price_USD': np.random.uniform(5.0, 1500.0, 20).round(2),
    'OrderDate': pd.to_datetime(pd.date_range(start='2024-01-01', periods=20, freq='D')),
    'Discount_Percent': np.random.choice([0.0, 0.1, 0.15, 0.2, np.nan], 20, p=[0.3, 0.3, 0.2, 0.1, 0.1]),
    'IsExpressShipping': np.random.choice([True, False], 20),
    'Customer_Rating': np.random.randint(1, 6, 20), # 1 to 5 stars
    'Item_Weight (kg)': np.random.uniform(0.1, 5.0, 20).round(1) # Column with space and special char
}
df = pd.DataFrame(data)

# Add a calculated column for total price
df['Total_Price_USD'] = df['Quantity'] * df['Price_USD'] * (1 - df['Discount_Percent'].fillna(0))

print("Original DataFrame (df):\n", df.head())
print("\nDataFrame Info:\n")
df.info()


print("\n--- 2. Basic Queries (Single Conditions) ---")

# 2.1 Numerical comparison: Orders with Quantity greater than 5
query_qty_gt_5 = df.query('Quantity > 5')
print("\nOrders with Quantity > 5:\n", query_qty_gt_5.head())

# 2.2 String comparison: Orders from 'Electronics' category
query_electronics = df.query('ProductCategory == "Electronics"')
print("\nOrders from 'Electronics' category:\n", query_electronics.head())

# 2.3 Boolean comparison: Orders with Express Shipping
query_express_shipping = df.query('IsExpressShipping == True')
print("\nOrders with Express Shipping:\n", query_express_shipping.head())

# 2.4 Floating point comparison (use approx for equality, or range for inequality)
query_price_exact = df.query('Price_USD == 100.00') # Might return empty if no exact match
print("\nOrders with Price_USD exactly 100.00:\n", query_price_exact)


print("\n--- 3. Multiple Conditions (AND, OR, NOT) ---")

# 3.1 AND condition: Quantity > 3 AND Price_USD < 500
query_and = df.query('Quantity > 3 and Price_USD < 500')
print("\nOrders with Quantity > 3 AND Price_USD < 500:\n", query_and.head())

# 3.2 OR condition: ProductCategory is 'Books' OR 'Clothing'
query_or = df.query('ProductCategory == "Books" or ProductCategory == "Clothing"')
print("\nOrders where ProductCategory is 'Books' OR 'Clothing':\n", query_or.head())

# 3.3 NOT condition: Orders NOT by CustomerID 101
query_not_customer = df.query('not CustomerID == 101')
print("\nOrders NOT by CustomerID 101:\n", query_not_customer.head())


print("\n--- 4. Using 'in' and 'not in' Operators ---")

# 4.1 'in' operator: Filter for multiple categories
query_in_categories = df.query('ProductCategory in ["Electronics", "Food"]')
print("\nOrders where ProductCategory is in ['Electronics', 'Food']:\n", query_in_categories.head())

# 4.2 'not in' operator: Filter out multiple customer IDs
query_not_in_customers = df.query('CustomerID not in [100, 102]')
print("\nOrders where CustomerID not in [100, 102]:\n", query_not_in_customers.head())

# 4.3 Using a Python list/tuple with 'in' (external variable)
target_products = ['Laptop', 'Mouse']
query_target_products = df.query('ProductCategory in @target_products')
print("\nOrders where ProductCategory is in target_products list (using @):\n", query_target_products.head())


print("\n--- 5. Referencing External Variables using '@' ---")

# Define external variables
min_price = 100
max_quantity = 5
desired_rating = 4

# Query using external numerical variables
query_external_num = df.query('Price_USD > @min_price and Quantity <= @max_quantity')
print(f"\nOrders with Price_USD > {min_price} AND Quantity <= {max_quantity}:\n", query_external_num.head())

# Query using external string variable
query_external_str = df.query('Customer_Rating == @desired_rating')
print(f"\nOrders with Customer_Rating == {desired_rating}:\n", query_external_str.head())


print("\n--- 6. Queries Involving Index and Calculated Columns ---")

# 6.1 Query by index
# Using `index` keyword to refer to the DataFrame's index
query_by_index_range = df.query('index >= 5 and index < 10')
print("\nOrders with original DataFrame index from 5 to 9:\n", query_by_index_range)

# 6.2 Query using a newly calculated column (within the chain or before)
# Query for total price, which was calculated earlier
query_total_price = df.query('Total_Price_USD > 500 and Total_Price_USD < 1000')
print("\nOrders with Total_Price_USD between 500 and 1000:\n", query_total_price.head())


print("\n--- 7. Handling Missing Values and Special Characters ---")

# 7.1 Querying for NaNs
# For NaN: use `isna()` or `isnull()`. Do NOT use `== np.nan` directly as it won't work.
query_missing_discount = df.query('Discount_Percent.isna()')
print("\nOrders with missing Discount_Percent:\n", query_missing_discount)

# 7.2 Querying for non-NaNs
query_has_discount = df.query('Discount_Percent.notna()')
print("\nOrders where Discount_Percent is NOT missing:\n", query_has_discount.head())

# 7.3 Handling column names with spaces or special characters
# Wrap column names in backticks (`)
query_weight = df.query('`Item_Weight (kg)` > 2.5')
print("\nOrders with Item_Weight > 2.5 kg:\n", query_weight.head())


print("\n--- 8. Combining .query() with Method Chaining ---")

# Example: Get high-value, fast-shipping electronics orders with good ratings,
# and select specific columns, then sort.
final_filtered_data = (
    df
    .query('ProductCategory == "Electronics" and IsExpressShipping == True') # Filter by category & shipping
    .query('Total_Price_USD > 500 and Customer_Rating >= 4') # Further filter by value & rating
    .dropna(subset=['Discount_Percent']) # Remove orders where discount info is missing
    .sort_values(by='Total_Price_USD', ascending=False) # Sort results
    [['OrderID', 'ProductCategory', 'Quantity', 'Price_USD', 'Total_Price_USD', 'Customer_Rating']] # Select columns
)
print("\nChained Query: High-value, Express-Shipping Electronics Orders:\n", final_filtered_data)


print("\n--- 9. Performance Considerations ---")
# .query() compiles the query expression into bytecode for faster execution
# for large DataFrames, especially with complex string expressions.
# For simple queries on small DataFrames, direct boolean indexing might be similar or faster.

# Example of a complex query that benefits from .query() readability
complex_query_example = (
    df.query(
        '`Item_Weight (kg)` > 1.5 and '
        'Price_USD < 1000 and '
        '(ProductCategory == "Books" or Customer_Rating >= 4)'
    )
)
print("\nComplex query example (benefits from .query() readability):\n", complex_query_example.head())


print("\n--- End of Pandas .query() Method Practice Code ---")