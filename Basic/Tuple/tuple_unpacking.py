# --- Python Tuples: All About Tuple Unpacking in Code ---

# Tuple unpacking (also known as sequence unpacking or iterable unpacking)
# is a powerful feature in Python that allows you to assign elements of a
# tuple (or any iterable) to multiple variables in a single line of code.

# --- 1. Basic Tuple Unpacking ---

print("--- 1. Basic Tuple Unpacking ---")

# The most straightforward use case is when the number of variables on the
# left-hand side exactly matches the number of elements in the tuple on the right.

# 1.1 Unpacking a simple tuple
coordinates = (10, 20)
x, y = coordinates
print(f"1.1 Unpacked coordinates: x={x}, y={y}") # Output: x=10, y=20

# 1.2 Unpacking with different data types
person_info = ("Alice", 30, "alice@example.com")
name, age, email = person_info
print(f"1.2 Unpacked person info: Name={name}, Age={age}, Email={email}")

# 1.3 Unpacking values returned by a function
# Functions often return tuples implicitly or explicitly.
def get_user_details():
    return "John Doe", 45, "Engineer" # This is tuple packing on the return side

user_name, user_age, user_occupation = get_user_details()
print(f"1.3 Unpacked function return: Name={user_name}, Age={user_age}, Occupation={user_occupation}")

# 1.4 Swapping variable values (a classic use case)
a = 5
b = 10
print(f"1.4 Before swap: a={a}, b={b}")
a, b = b, a # Python first evaluates (b, a) to (10, 5) then unpacks it.
print(f"    After swap: a={a}, b={b}")

# 1.5 Unpacking from other iterables (not just tuples)
# List unpacking
my_list = [100, 200, 300]
val1, val2, val3 = my_list
print(f"1.5 Unpacked from list: {val1}, {val2}, {val3}")

# String unpacking (each character)
my_string = "ABC"
char1, char2, char3 = my_string
print(f"    Unpacked from string: {char1}, {char2}, {char3}")


# --- 2. Extended Unpacking (Starred Assignment) ---

print("\n--- 2. Extended Unpacking (Starred Assignment) ---")

# Introduced in Python 3.0 (PEP 3132), extended unpacking allows you to
# capture multiple elements into a single list using the `*` (asterisk) operator.
# Only one starred expression is allowed on the left-hand side.

# 2.1 Catch-all at the end: `first, second, *rest = iterable`
data_stream = (1, 2, 3, 4, 5, 6, 7)
first_val, second_val, *remaining_vals = data_stream
print(f"2.1 Catch-all at end: First={first_val}, Second={second_val}, Remaining={remaining_vals}")
# Output: First=1, Second=2, Remaining=[3, 4, 5, 6, 7]
print(f"    Type of 'remaining_vals': {type(remaining_vals)}") # Always a list

# 2.2 Catch-all at the beginning: `*beginning, last = iterable`
*initial_vals, last_val = data_stream
print(f"2.2 Catch-all at beginning: Initial={initial_vals}, Last={last_val}")
# Output: Initial=[1, 2, 3, 4, 5, 6], Last=7

# 2.3 Catch-all in the middle: `first, *middle, last = iterable`
start_val, *middle_vals, end_val = data_stream
print(f"2.3 Catch-all in middle: Start={start_val}, Middle={middle_vals}, End={end_val}")
# Output: Start=1, Middle=[2, 3, 4, 5, 6], End=7

# 2.4 What if the starred variable captures zero or one element?
# It will still be a list.
short_data = (10, 20)
s1, *s_rest, s2 = short_data
print(f"2.4 Starred captures zero: s1={s1}, s_rest={s_rest}, s2={s2}")
# Output: s1=10, s_rest=[], s2=20 (s_rest is an empty list)

single_item = (50,)
*single_list, = single_item # Note the comma after `*single_list` is crucial for single-element iterable
print(f"    Starred captures one: single_list={single_list}")
# Output: single_list=[50] (still a list)

# 2.5 Using `*_` to ignore captured elements
# It's a common convention to use `_` as a variable name for values you don't intend to use.
header, *_, footer = ("ID", "Name", "Age", "City", "Country", "Timestamp")
print(f"2.5 Ignoring elements with `*_`: Header={header}, Footer={footer}")
# Output: Header=ID, Footer=Timestamp
# The intermediate elements are still collected into `_`, but we signal intent to ignore.


# --- 3. Error Handling in Unpacking ---

print("\n--- 3. Error Handling in Unpacking ---")

# 3.1 `ValueError`: When the number of variables doesn't match the iterable's length
# (for basic unpacking without `*`).
try:
    too_few_vars = (1, 2, 3)
    a, b = too_few_vars # Expected 3, got 2 variables
except ValueError as e:
    print(f"3.1 Error (Too few variables): {e}")

try:
    too_many_vars = (10, 20)
    x, y, z = too_many_vars # Expected 2, got 3 variables
except ValueError as e:
    print(f"    Error (Too many variables): {e}")

# 3.2 `SyntaxError`: When more than one starred expression is used in an assignment.
try:
    *first_part, *second_part = (1, 2, 3, 4)
except SyntaxError as e:
    print(f"3.2 Error (Multiple starred expressions): {e}")


# --- 4. Practical Use Cases for Tuple Unpacking ---

print("\n--- 4. Practical Use Cases ---")

# 4.1 Iterating over items in a dictionary (items() returns tuples)
my_scores = {"Math": 90, "Science": 85, "History": 78}
print(f"4.1 Iterating over dictionary items:")
for subject, score in my_scores.items():
    print(f"    {subject}: {score}")

# 4.2 Processing structured data (e.g., CSV rows)
# Imagine each row is a tuple from a CSV file.
csv_rows = [
    ("Alice", 30, "New York"),
    ("Bob", 24, "London"),
    ("Charlie", 35, "Paris")
]
print(f"\n4.2 Processing CSV-like data:")
for name, age, city in csv_rows:
    print(f"    Name: {name}, Age: {age}, City: {city}")

# 4.3 Function arguments with `*args` and `**kwargs`
# Unpacking is used internally when a function receives `*args` or `**kwargs`.
def process_args(*args, **kwargs):
    print(f"    Received positional args: {args}")
    print(f"    Received keyword args: {kwargs}")

my_list_args = [10, 20, 30]
my_dict_kwargs = {"param1": "value1", "param2": "value2"}

print(f"\n4.3 Function arguments with *args and **kwargs:")
process_args(*my_list_args, **my_dict_kwargs) # Here, unpacking is in the function CALL
# The `*` unpacks the list into positional arguments.
# The `**` unpacks the dictionary into keyword arguments.


# --- 5. Tuple vs. List Unpacking ---

print("\n--- 5. Tuple vs. List Unpacking ---")

# The unpacking syntax works identically for both tuples and lists.
# The choice between tuple and list for the source iterable depends on your data's mutability needs.

tuple_source = (1, 2, 3)
list_source = [10, 20, 30]

t1, t2, t3 = tuple_source
l1, l2, l3 = list_source

print(f"Tuple unpacking: {t1}, {t2}, {t3}")
print(f"List unpacking: {l1}, {l2}, {l3}")