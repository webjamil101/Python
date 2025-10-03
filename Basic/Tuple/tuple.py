# --- Python Tuples: All About in Code ---

# Tuples are one of Python's fundamental built-in data structures.
# They are used to store collections of items.

# --- 1. Introduction to Tuples ---

# 1.1 What are Tuples?
# - Ordered: The order of items is preserved.
# - Immutable: Once a tuple is created, you cannot change its elements (add, remove, or modify).
# - Allow duplicate members.
# - Can contain items of different data types.
# - Defined by items separated by commas, optionally enclosed in parentheses `()`.

# 1.2 Why use Tuples?
# - Data Integrity: Since they are immutable, tuples are great for data that should not change.
# - Function Arguments: Often used to return multiple values from a function.
# - Dictionary Keys: Because they are immutable, tuples can be used as keys in dictionaries (unlike lists).
# - Performance: Generally slightly faster than lists for iteration over fixed data.
# - Data Unpacking: Easily unpack into multiple variables.

print("--- 1. Introduction ---")
print("Tuples are ordered, immutable collections of items.")
print("They are defined using parentheses or just commas.")


# --- 2. Creating Tuples ---

print("\n--- 2. Creating Tuples ---")

# 2.1 Empty Tuple
empty_tuple_1 = ()
print(f"2.1 Empty tuple using (): {empty_tuple_1}")
print(f"    Type of empty_tuple_1: {type(empty_tuple_1)}")

empty_tuple_2 = tuple() # Using the constructor
print(f"    Empty tuple using tuple(): {empty_tuple_2}")

# 2.2 Tuple with multiple elements (most common)
# Elements are separated by commas, usually enclosed in parentheses.
coordinates = (10.0, 20.5)
print(f"2.2 Coordinates tuple: {coordinates}")

person_info = ("Alice", 30, "New York")
print(f"    Person Info tuple: {person_info}")

# 2.3 Tuple without parentheses (tuple packing)
# Python automatically treats comma-separated values as a tuple.
colors = "red", "green", "blue"
print(f"2.3 Colors tuple (without parentheses): {colors}")
print(f"    Type of colors: {type(colors)}")

# 2.4 Single-element Tuple (CRUCIAL: needs a trailing comma!)
# Without the comma, Python treats it as a simple expression in parentheses.
single_element_tuple = (100,) # The comma is essential!
print(f"2.4 Single-element tuple: {single_element_tuple}")
print(f"    Type of single_element_tuple: {type(single_element_tuple)}")

# Incorrect way to create a single-element tuple (creates an int, not a tuple)
not_a_tuple = (100)
print(f"    (100) is not a tuple: {not_a_tuple}, Type: {type(not_a_tuple)}")

# 2.5 Tuple with mixed data types
mixed_tuple = ("apple", 123, True, 3.14, [1, 2], {"key": "value"})
print(f"2.5 Mixed data types tuple: {mixed_tuple}")

# 2.6 Nested Tuples
nested_tuple = ((1, 2), (3, 4, 5))
print(f"2.6 Nested tuple: {nested_tuple}")

# 2.7 Creating a tuple from an iterable (using tuple() constructor)
# Can convert lists, strings, sets, etc., into tuples.
list_to_tuple = tuple([1, 2, 3, 4])
print(f"2.7 List converted to tuple: {list_to_tuple}")

string_to_tuple = tuple("hello")
print(f"    String converted to tuple: {string_to_tuple}") # Each character becomes an element

set_to_tuple = tuple({5, 1, 3}) # Order is not guaranteed when converting from a set
print(f"    Set converted to tuple (order might vary): {set_to_tuple}")


# --- 3. Accessing Elements in Tuples ---

print("\n--- 3. Accessing Elements ---")

my_tuple = ("alpha", "beta", "gamma", "delta", "epsilon")

# 3.1 Indexing (positive and negative)
# - Positive indexing starts from 0 for the first element.
# - Negative indexing starts from -1 for the last element.
print(f"3.1 First element (index 0): {my_tuple[0]}")
print(f"    Third element (index 2): {my_tuple[2]}")
print(f"    Last element (index -1): {my_tuple[-1]}")
print(f"    Second to last element (index -2): {my_tuple[-2]}")

# Attempting to access an out-of-range index will raise an IndexError
try:
    print(my_tuple[10])
except IndexError as e:
    print(f"    Error: {e} - Index out of range.")

# 3.2 Slicing
# - Extracts a portion of the tuple.
# - Syntax: `tuple[start:end:step]`
# - `end` index is exclusive.
# - Returns a new tuple.
print(f"3.2 Slice from index 1 to 3 (exclusive): {my_tuple[1:4]}") # ('beta', 'gamma', 'delta')
print(f"    Slice from beginning to index 2 (exclusive): {my_tuple[:2]}") # ('alpha', 'beta')
print(f"    Slice from index 3 to end: {my_tuple[3:]}") # ('delta', 'epsilon')
print(f"    Slice with step 2: {my_tuple[::2]}") # ('alpha', 'gamma', 'epsilon')
print(f"    Reverse the tuple: {my_tuple[::-1]}") # ('epsilon', 'delta', 'gamma', 'beta', 'alpha')


# --- 4. Immutability of Tuples ---

print("\n--- 4. Immutability ---")

# The core characteristic of tuples is that they are immutable.
# Once created, their elements cannot be changed.

immutable_tuple = (1, 2, 3)
print(f"4.1 Original tuple: {immutable_tuple}")

# Attempting to modify an element will raise a TypeError
try:
    immutable_tuple[0] = 10 # This line will cause an error
except TypeError as e:
    print(f"    Error: {e} - Tuples do not support item assignment.")

# 4.2 Immutability vs. Mutable Elements within a Tuple
# While the tuple itself is immutable, if it contains mutable elements (like lists),
# those mutable elements *can* be changed. The reference to the list object
# within the tuple remains the same, but the list's content can change.
tuple_with_list = (1, [2, 3], 4)
print(f"    Tuple with a list: {tuple_with_list}")
tuple_with_list[1].append(5) # This modifies the list inside the tuple
print(f"    Tuple after modifying its internal list: {tuple_with_list}")
# The tuple object itself hasn't changed, only the object it refers to at index 1.


# --- 5. Tuple Operations ---

print("\n--- 5. Tuple Operations ---")

tuple_a = (1, 2)
tuple_b = (3, 4)

# 5.1 Concatenation (`+` operator)
# Creates a new tuple by joining existing tuples.
combined_tuple = tuple_a + tuple_b
print(f"5.1 Concatenation (tuple_a + tuple_b): {combined_tuple}") # (1, 2, 3, 4)

# 5.2 Repetition (`*` operator)
# Repeats the tuple elements a specified number of times.
repeated_tuple = tuple_a * 3
print(f"5.2 Repetition (tuple_a * 3): {repeated_tuple}") # (1, 2, 1, 2, 1, 2)

# 5.3 Membership testing (`in` operator)
# Checks if an item exists within the tuple.
print(f"5.3 Is 2 in tuple_a? {2 in tuple_a}") # True
print(f"    Is 5 in tuple_a? {5 in tuple_a}") # False

# 5.4 Length (`len()` function)
print(f"5.4 Length of combined_tuple: {len(combined_tuple)}") # 4


# --- 6. Tuple Methods ---

print("\n--- 6. Tuple Methods ---")

my_tuple_methods = (1, 2, 2, 3, 4, 2)

# 6.1 `count(value)`: Returns the number of times a specified value occurs in the tuple.
print(f"6.1 Count of 2 in {my_tuple_methods}: {my_tuple_methods.count(2)}") # 3
print(f"    Count of 5 in {my_tuple_methods}: {my_tuple_methods.count(5)}") # 0

# 6.2 `index(value, start=0, end=len(tuple))`
# - Returns the index of the first occurrence of a specified value.
# - Raises a `ValueError` if the value is not found.
# - Optional `start` and `end` parameters to search within a slice.
print(f"6.2 Index of 3 in {my_tuple_methods}: {my_tuple_methods.index(3)}") # 3 (0-indexed)
print(f"    Index of first 2 in {my_tuple_methods}: {my_tuple_methods.index(2)}") # 1
print(f"    Index of 2 starting from index 2: {my_tuple_methods.index(2, 2)}") # 2

try:
    print(my_tuple_methods.index(5))
except ValueError as e:
    print(f"    Error: {e} - Value not found.")


# --- 7. Tuple Unpacking (Sequence Unpacking) ---

print("\n--- 7. Tuple Unpacking ---")

# Assigning elements of a tuple to multiple variables.
# The number of variables on the left must match the number of elements in the tuple.

# 7.1 Basic unpacking
point = (10, 20)
x, y = point
print(f"7.1 Unpacked point: x={x}, y={y}")

# 7.2 Unpacking function return values
def get_user_data():
    return "John Doe", 45, "Engineer"

name, age, occupation = get_user_data()
print(f"    Unpacked user data from function: Name={name}, Age={age}, Occupation={occupation}")

# 7.3 Swapping variables using tuple unpacking
a = 5
b = 10
print(f"    Before swap: a={a}, b={b}")
a, b = b, a # This creates a temporary tuple (10, 5) and unpacks it.
print(f"    After swap: a={a}, b={b}")

# 7.4 Extended Unpacking (Python 3.0+)
# Using `*` to capture multiple elements into a list.
data = (1, 2, 3, 4, 5, 6)
first, *middle, last = data
print(f"    Extended unpack: first={first}, middle={middle}, last={last}") # middle is a list: [2, 3, 4, 5]

# Using `*_` to ignore elements
header, *_, footer = ("ID", "Name", "Age", "City", "Country", "Timestamp")
print(f"    Extended unpack (ignoring middle): header={header}, footer={footer}")


# --- 8. When to Use Tuples vs. Lists ---

print("\n--- 8. When to Use Tuples vs. Lists ---")

# - **Choose Tuples when:**
#   - The collection of items is fixed and should not change (e.g., coordinates, RGB colors, database records where fields are fixed).
#   - You need to use the collection as a dictionary key (because tuples are hashable if their contents are immutable).
#   - You are returning multiple values from a function.
#   - You need slightly better performance for fixed-size collections (though this is often negligible).

# - **Choose Lists when:**
#   - The collection of items needs to be modified (add, remove, change elements).
#   - The order of items might change.
#   - You need dynamic resizing.

# Example:
# A point (x, y) is naturally a tuple because its components are fixed.
point = (10, 20)

# A list of items in a shopping cart is naturally a list because items can be added/removed.
shopping_cart = ["milk", "bread", "eggs"]