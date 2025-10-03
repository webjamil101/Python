# --- Python Tuples: All About Operations in Code ---

# Tuples, despite being immutable, support a variety of operations that
# allow you to combine them, repeat their elements, check for membership,
# and determine their size. Importantly, these operations *always* result
# in the creation of a *new* tuple, as the original tuples cannot be modified.

# Let's define some sample tuples for demonstration.
tuple1 = (1, 2, 3)
tuple2 = (4, 5)
tuple_mixed = ("apple", 123, True)
tuple_repeated_item = ("hello",) # Single-element tuple for repetition
tuple_search = (10, 20, 30, 20, 40, 50)


print("--- 1. Concatenation (`+` Operator) ---")

# The `+` operator is used to concatenate (join) two or more tuples.
# It creates a *new* tuple containing all elements from the operands in order.

# 1.1 Basic concatenation
combined_tuple = tuple1 + tuple2
print(f"1.1 {tuple1} + {tuple2} = {combined_tuple}") # Output: (1, 2, 3, 4, 5)

# 1.2 Concatenating multiple tuples
longer_tuple = tuple1 + tuple2 + (6, 7, 8)
print(f"1.2 {tuple1} + {tuple2} + (6, 7, 8) = {longer_tuple}") # Output: (1, 2, 3, 4, 5, 6, 7, 8)

# 1.3 Concatenating with an empty tuple
empty_tuple = ()
result_with_empty = tuple1 + empty_tuple
print(f"1.3 {tuple1} + {empty_tuple} = {result_with_empty}") # Output: (1, 2, 3)

# 1.4 Concatenating mixed types (elements are just combined)
mixed_combined = tuple1 + tuple_mixed
print(f"1.4 {tuple1} + {tuple_mixed} = {mixed_combined}") # Output: (1, 2, 3, 'apple', 123, True)

# Important: You cannot concatenate a tuple with a non-tuple type directly.
try:
    tuple1 + [6, 7] # This would raise a TypeError
except TypeError as e:
    print(f"\n1.5 Error: Cannot concatenate tuple with list: {e}")


print("\n--- 2. Repetition (`*` Operator) ---")

# The `*` operator is used to repeat the elements of a tuple a specified number of times.
# It creates a *new* tuple.

# 2.1 Basic repetition
repeated_tuple = tuple1 * 2
print(f"2.1 {tuple1} * 2 = {repeated_tuple}") # Output: (1, 2, 3, 1, 2, 3)

# 2.2 Repetition with a single-element tuple (remember the comma!)
repeated_single_item = tuple_repeated_item * 4
print(f"2.2 {tuple_repeated_item} * 4 = {repeated_single_item}") # Output: ('hello', 'hello', 'hello', 'hello')

# 2.3 Repetition by 0 (results in an empty tuple)
empty_repetition = tuple1 * 0
print(f"2.3 {tuple1} * 0 = {empty_repetition}") # Output: ()

# 2.4 Repetition by a negative number (also results in an empty tuple)
negative_repetition = tuple1 * -2
print(f"2.4 {tuple1} * -2 = {negative_repetition}") # Output: ()


print("\n--- 3. Membership Testing (`in` Operator) ---")

# The `in` operator checks if a specific item exists within the tuple.
# It returns `True` if the item is found, and `False` otherwise.

# 3.1 Checking for existing elements
print(f"3.1 Is 2 in {tuple1}? {2 in tuple1}") # Output: True
print(f"    Is 'apple' in {tuple_mixed}? {'apple' in tuple_mixed}") # Output: True

# 3.2 Checking for non-existent elements
print(f"3.2 Is 5 in {tuple1}? {5 in tuple1}") # Output: False
print(f"    Is 'banana' in {tuple_mixed}? {'banana' in tuple_mixed}") # Output: False

# 3.3 Case sensitivity for strings
print(f"3.3 Is 'Apple' in {tuple_mixed}? {'Apple' in tuple_mixed}") # Output: False (case-sensitive)


print("\n--- 4. Length (`len()` Function) ---")

# The `len()` built-in function returns the number of elements in the tuple.

# 4.1 Basic length
print(f"4.1 Length of {tuple1}: {len(tuple1)}") # Output: 3
print(f"    Length of {tuple_mixed}: {len(tuple_mixed)}") # Output: 3
print(f"    Length of empty_tuple: {len(empty_tuple)}") # Output: 0

# 4.2 Length of nested tuples (counts the nested tuple as one element)
nested_tuple = ((1, 2), (3, 4, 5))
print(f"4.2 Length of {nested_tuple}: {len(nested_tuple)}") # Output: 2 (counts two inner tuples)


print("\n--- 5. Min, Max, Sum (for numeric tuples) ---")

# For tuples containing only numeric types, you can use `min()`, `max()`, and `sum()`.

numeric_tuple = (10, 5, 20, 15)
print(f"Numeric tuple: {numeric_tuple}")

# 5.1 `min()`: Returns the smallest item in the tuple.
print(f"5.1 Minimum value: {min(numeric_tuple)}") # Output: 5

# 5.2 `max()`: Returns the largest item in the tuple.
print(f"5.2 Maximum value: {max(numeric_tuple)}") # Output: 20

# 5.3 `sum()`: Returns the sum of all items in the tuple.
print(f"5.3 Sum of values: {sum(numeric_tuple)}") # Output: 50

# Attempting to use min/max/sum on non-numeric or mixed-type tuples will raise a TypeError.
try:
    sum(tuple_mixed)
except TypeError as e:
    print(f"\n5.4 Error: Cannot sum non-numeric tuple: {e}")


print("\n--- 6. Tuple Unpacking (Sequence Unpacking) ---")

# Assigning elements of a tuple to multiple variables.
# This is an operation on the tuple's elements, not the tuple itself, but it's crucial.

# 6.1 Basic unpacking
point = (10, 20)
x, y = point
print(f"6.1 Unpacked point: x={x}, y={y}")

# 6.2 Extended Unpacking (Python 3.0+)
# Using `*` to capture multiple elements into a list.
data = (1, 2, 3, 4, 5, 6)
first, *middle, last = data
print(f"6.2 Extended unpack: first={first}, middle={middle}, last={last}") # middle is a list: [2, 3, 4, 5]

# Using `*_` to ignore elements
header, *_, footer = ("ID", "Name", "Age", "City", "Country", "Timestamp")
print(f"    Extended unpack (ignoring middle): header={header}, footer={footer}")


print("\n--- 7. Comparison Operations ---")

# Tuples can be compared using standard comparison operators (`==`, `!=`, `<`, `<=`, `>`, `>=`).
# Comparison is performed element by element, from left to right.

# 7.1 Equality (`==`)
print(f"7.1 Is (1, 2, 3) == (1, 2, 3)? {(1, 2, 3) == (1, 2, 3)}") # True
print(f"    Is (1, 2, 3) == (1, 2, 4)? {(1, 2, 3) == (1, 2, 4)}") # False

# 7.2 Less than (`<`) - Lexicographical comparison
# Compares the first differing element.
print(f"7.2 Is (1, 2, 3) < (1, 2, 4)? {(1, 2, 3) < (1, 2, 4)}") # True (3 < 4)
print(f"    Is (1, 5) < (2, 1)? {(1, 5) < (2, 1)}") # True (1 < 2)
print(f"    Is ('apple', 10) < ('apple', 5)? {('apple', 10) < ('apple', 5)}") # False (10 is not < 5)

# Elements must be comparable (e.g., cannot compare int with string directly).
try:
    (1, 'a') < (1, 2)
except TypeError as e:
    print(f"\n7.3 Error: Cannot compare mixed types in tuple: {e}")