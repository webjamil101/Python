import pandas as pd
import numpy as np
import os
import csv # For creating CSV files

print("--- Pandas: Loading Different File Formats Practice Code ---")

# Define a directory for temporary files
output_dir = "pandas_load_examples"
os.makedirs(output_dir, exist_ok=True)
print(f"Temporary files will be created in: {output_dir}")


# --- 1. CSV (Comma Separated Values) Files ---
print("\n--- 1. CSV (Comma Separated Values) Files ---")
print("`pd.read_csv()` is one of the most frequently used Pandas functions.")

# Create a sample CSV file
csv_file_path = os.path.join(output_dir, "sample_data.csv")
csv_data = [
    ['Name', 'Age', 'City', 'Score'],
    ['Alice', 25, 'New York', 88.5],
    ['Bob', 30, 'London', 72.0],
    ['Charlie', 22, 'Paris', np.nan], # NaN for missing
    ['David', 35, 'Tokyo', 95.5]
]
with open(csv_file_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(csv_data)
print(f"Created CSV file: {csv_file_path}")

# 1.1 Basic CSV Load
df_csv_basic = pd.read_csv(csv_file_path)
print(f"\nDataFrame from basic CSV load:\n{df_csv_basic}")

# 1.2 Handling common `read_csv` parameters
# `header`: row number to use as column names (0-indexed). None if no header.
# `names`: list of column names if no header or to override.
# `index_col`: column(s) to use as the row labels.
# `sep`/`delimiter`: character used to separate values (e.g., '\t' for TSV).
# `skiprows`: number of rows to skip at the beginning of the file.
# `nrows`: number of rows to read from the file.
# `na_values`: additional strings to recognize as NaN/NA.
# `dtype`: dictionary of column name to data type.
# `parse_dates`: list of columns to parse as dates.

# Create a more complex CSV for demonstration
complex_csv_path = os.path.join(output_dir, "complex_data.csv")
complex_csv_data = [
    ['# This is a comment', '', '', ''],
    ['id', 'value1', 'value2', 'date_str'],
    ['A001', '100', '10.5', '2023-01-15'],
    ['A002', '150', 'bad_data', '2023-01-16'], # Bad data
    ['A003', '200', '12.3', '2023-01-17'],
    ['A004', '250', '', '2023-01-18'] # Empty string
]
with open(complex_csv_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(complex_csv_data)
print(f"\nCreated complex CSV file: {complex_csv_path}")

df_complex_csv = pd.read_csv(
    complex_csv_path,
    skiprows=[0],           # Skip the first row (comment)
    index_col='id',         # Use 'id' column as index
    na_values=['bad_data', ''], # Treat 'bad_data' and empty strings as NaN
    dtype={'value1': int},  # Ensure 'value1' is integer
    parse_dates=['date_str'] # Parse 'date_str' as datetime
)
print(f"\nDataFrame from complex CSV load:\n{df_complex_csv}")
print(f"Dtypes of complex CSV DataFrame:\n{df_complex_csv.dtypes}")


# --- 2. Excel Files (.xlsx, .xls) ---
print("\n--- 2. Excel Files (.xlsx, .xls) ---")
print("`pd.read_excel()` requires `openpyxl` or `xlrd` engines.")

# Create a sample Excel file (requires openpyxl)
excel_file_path = os.path.join(output_dir, "sample_excel.xlsx")
excel_df = pd.DataFrame({
    'Product': ['Apple', 'Banana', 'Orange'],
    'Price': [1.0, 0.5, 0.75],
    'Quantity': [100, 200, 150]
})
excel_df.to_excel(excel_file_path, index=False, sheet_name='Sheet1')
print(f"Created Excel file: {excel_file_path}")

# 2.1 Basic Excel Load
df_excel_basic = pd.read_excel(excel_file_path)
print(f"\nDataFrame from basic Excel load:\n{df_excel_basic}")

# 2.2 Loading specific sheet
excel_df2 = pd.DataFrame({
    'Item': ['Pen', 'Notebook'],
    'Cost': [2.5, 5.0]
})
with pd.ExcelWriter(excel_file_path, engine='openpyxl', mode='a') as writer:
    excel_df2.to_excel(writer, sheet_name='Sheet2', index=False)
print(f"Added 'Sheet2' to {excel_file_path}")

df_excel_sheet2 = pd.read_excel(excel_file_path, sheet_name='Sheet2')
print(f"\nDataFrame from 'Sheet2':\n{df_excel_sheet2}")

# 2.3 Other `read_excel` parameters (similar to `read_csv`)
# `header`, `names`, `index_col`, `skiprows`, `nrows`, `na_values`, `dtype`, `parse_dates`
# `usecols`: list of column names or 0-indexed column numbers to parse.


# --- 3. JSON (JavaScript Object Notation) Files ---
print("\n--- 3. JSON (JavaScript Object Notation) Files ---")
print("`pd.read_json()` is great for semi-structured data.")

# Create a sample JSON file
json_file_path = os.path.join(output_dir, "sample.json")
json_data = [
    {"id": 1, "name": "Anna", "features": {"height": 170, "weight": 65}},
    {"id": 2, "name": "Ben", "features": {"height": 180, "weight": 75}},
    {"id": 3, "name": "Cathy", "features": {"height": 165, "weight": 58}}
]
# Pandas can directly write dict/list of dicts to JSON
pd.DataFrame(json_data).to_json(json_file_path, orient='records', indent=4)
print(f"Created JSON file: {json_file_path}")

# 3.1 Basic JSON Load
df_json_basic = pd.read_json(json_file_path)
print(f"\nDataFrame from basic JSON load:\n{df_json_basic}")

# 3.2 Handling nested JSON (often requires flattening, not direct `read_json` param)
# For nested 'features' column, you might need to normalize:
# from pandas.io.json import json_normalize # Deprecated in newer pandas; use pd.json_normalize
# df_nested_json = pd.json_normalize(json_data)
# print(f"\nDataFrame from normalized JSON load:\n{df_nested_json}")


# --- 4. HDF5 Files (.h5, .hdf5) ---
print("\n--- 4. HDF5 Files (.h5, .hdf5) ---")
print("HDF5 is a powerful format for storing large amounts of numerical data, often used with PyTables.")
print("`pd.read_hdf()` and `df.to_hdf()` are used.")
print("Requires `pytables` to be installed (`pip install tables`).")

# Create a sample HDF5 file
hdf_file_path = os.path.join(output_dir, "sample.h5")
hdf_df = pd.DataFrame({
    'ValueA': np.random.rand(5),
    'ValueB': np.arange(5)
})

try:
    # Key is like a path inside the HDF5 file
    hdf_df.to_hdf(hdf_file_path, key='my_data_group/df1', mode='w')
    print(f"Created HDF5 file: {hdf_file_path} with key 'my_data_group/df1'")

    # 4.1 Basic HDF5 Load
    df_hdf_basic = pd.read_hdf(hdf_file_path, key='my_data_group/df1')
    print(f"\nDataFrame from HDF5 load:\n{df_hdf_basic}")

    # You can append to existing keys or write new ones
    hdf_df_new = pd.DataFrame({'C': [10, 20]})
    hdf_df_new.to_hdf(hdf_file_path, key='my_data_group/df2', mode='a')
    print(f"Added key 'my_data_group/df2' to {hdf_file_path}")

    # Listing keys in an HDF5 file
    with pd.HDFStore(hdf_file_path, mode='r') as store:
        print(f"Keys in HDF5 file: {store.keys()}")
    
except ImportError:
    print("PyTables not installed. Skipping HDF5 example. Install with `pip install tables`.")
except Exception as e:
    print(f"An error occurred during HDF5 operations: {e}")


# --- 5. SQL Databases ---
print("\n--- 5. SQL Databases ---")
print("`pd.read_sql()` reads data from a SQL database.")
print("Requires a database connector library (e.g., `sqlite3` for SQLite, `psycopg2` for PostgreSQL).")

# Example using SQLite (built-in to Python)
from sqlalchemy import create_engine
sqlite_db_path = os.path.join(output_dir, "sample.db")
engine = create_engine(f'sqlite:///{sqlite_db_path}')

# Create a sample table and insert data
sql_df = pd.DataFrame({
    'student_id': [1, 2, 3],
    'name': ['Eva', 'Frank', 'Grace'],
    'grade': ['A', 'B', 'A']
})
sql_df.to_sql('students', engine, if_exists='replace', index=False)
print(f"Created SQLite database and 'students' table in: {sqlite_db_path}")

# 5.1 Basic SQL Load (reading an entire table)
df_sql_table = pd.read_sql('students', engine)
print(f"\nDataFrame from SQL table 'students':\n{df_sql_table}")

# 5.2 Loading with a custom SQL query
df_sql_query = pd.read_sql("SELECT name, grade FROM students WHERE grade = 'A'", engine)
print(f"\nDataFrame from SQL query (students with grade 'A'):\n{df_sql_query}")

engine.dispose() # Close the database connection


# --- 6. Parquet Files ---
print("\n--- 6. Parquet Files ---")
print("Parquet is a columnar storage format, highly efficient for analytical queries.")
print("Requires `pyarrow` or `fastparquet` (`pip install pyarrow`).")

# Create a sample Parquet file
parquet_file_path = os.path.join(output_dir, "sample.parquet")
parquet_df = pd.DataFrame({
    'col_str': ['foo', 'bar', 'baz'],
    'col_int': [1, 2, 3],
    'col_float': [0.1, 0.2, 0.3],
    'col_bool': [True, False, True]
})
try:
    parquet_df.to_parquet(parquet_file_path, index=False)
    print(f"Created Parquet file: {parquet_file_path}")

    # 6.1 Basic Parquet Load
    df_parquet_basic = pd.read_parquet(parquet_file_path)
    print(f"\nDataFrame from Parquet load:\n{df_parquet_basic}")
except ImportError:
    print("PyArrow not installed. Skipping Parquet example. Install with `pip install pyarrow`.")
except Exception as e:
    print(f"An error occurred during Parquet operations: {e}")


# --- 7. Other Formats (Brief Mention) ---
print("\n--- 7. Other Formats (Brief Mention) ---")
print("Pandas also supports: ")
print(" - `feather`: `pd.read_feather()` (requires `pyarrow`) - another fast columnar format.")
print(" - `pickle`: `pd.read_pickle()` - for saving/loading arbitrary Python objects, including DataFrames.")
print(" - `html`: `pd.read_html()` - reads HTML tables into a list of DataFrames.")
print(" - `xml`: `pd.read_xml()` (new in Pandas 1.3) - reads XML files.")
print(" - `clipboard`: `pd.read_clipboard()` - reads content from your clipboard (useful for quick copy-paste).")


# --- Cleanup ---
print("\n--- Cleaning up generated files ---")
try:
    for root, dirs, files in os.walk(output_dir, topdown=False):
        for name in files:
            file_to_remove = os.path.join(root, name)
            os.remove(file_to_remove)
        for name in dirs:
            dir_to_remove = os.path.join(root, name)
            os.rmdir(dir_to_remove)
    os.rmdir(output_dir)
    print(f"Successfully cleaned up '{output_dir}'.")
except OSError as e:
    print(f"Error during cleanup: {e}")

print("\n--- End of Pandas: Loading Different File Formats Practice Code ---")