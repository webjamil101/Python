import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

print("--- Using iterrows() ---")
for index, row in df.iterrows():
    print(f"Index: {index}, Name: {row['Name']}, Age: {row['Age']}, City: {row['City']}")

# Example: Calculate a new column based on existing ones
# (Though better done with vectorized operations, for demonstration)
df['Age_Category'] = '' # Initialize new column
for index, row in df.iterrows():
    if row['Age'] < 30:
        df.at[index, 'Age_Category'] = 'Young' # Use .at for safe assignment within loop
    else:
        df.at[index, 'Age_Category'] = 'Adult'
print("\nDataFrame after iterrows() modification:")
print(df)


import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

print("\n--- Using itertuples() ---")
for row in df.itertuples():
    print(f"Index: {row.Index}, Name: {row.Name}, Age: {row.Age}, City: {row.City}")

# You can also access by index if you set name=None
for row_tuple in df.itertuples(index=False, name=None): # Returns regular tuple
    print(f"Name: {row_tuple[0]}, Age: {row_tuple[1]}")


import pandas as pd

data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

print("\n--- Iterating over column names ---")
for col in df:
    print(f"Column Name: {col}")
    print(f"Column Data (Series):\n{df[col]}\n")

import pandas as pd

data = {'Quantity': [10, 20, 30],
        'Price': [0.5, 0.3, 0.7]}
df = pd.DataFrame(data)

print("--- Vectorized Operations ---")

# Calculate Total Sales (Element-wise multiplication)
df['Total_Sales'] = df['Quantity'] * df['Price']
print("\nAfter vectorized multiplication:")
print(df)

# Conditional assignment (often done with np.where or boolean indexing)
df['Price_Category'] = pd.Series('Normal', index=df.index) # Default
df.loc[df['Price'] > 0.6, 'Price_Category'] = 'High'
print("\nAfter vectorized conditional assignment:")
print(df)

# Sum a column
total_quantity = df['Quantity'].sum()
print(f"\nTotal Quantity: {total_quantity}")

import pandas as pd

data = {'Sales_Q1': [200, 150, 300],
        'Sales_Q2': [300, 200, 400],
        'Product': ['A', 'B', 'C']}
df = pd.DataFrame(data)

print("\n--- Using apply() ---")

# Applying a function to each row (axis=1)
def calculate_total_sales(row):
    return row['Sales_Q1'] + row['Sales_Q2']

df['Total_Sales_Apply'] = df.apply(calculate_total_sales, axis=1)
print("\nAfter apply() for row-wise calculation:")
print(df)

# Using a lambda function with apply()
df['Sales_Difference'] = df.apply(lambda row: row['Sales_Q2'] - row['Sales_Q1'], axis=1)
print("\nAfter apply() with lambda for row-wise calculation:")
print(df)