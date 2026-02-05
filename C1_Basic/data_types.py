# Data_types

# Numeric Types
int_var = 10          # Integer
float_var = 10.5     # Floating-point number
complex_var = 2 + 3j # Complex number

# Sequence Types
list_var = [1, 2, 3, 4, 5]          # List
tuple_var = (1, 2, 3)            # Tuple
range_var = range(0, 10, 2)      # Range   
str_var = "Hello, World!"        # String

# Mapping Type
dict_var = {"name": "Yashraj", "age": 19}  # Dictionary
set_var = {1, 2, 3, 4, 5}               # Set

# Boolean Type
bool_var = True  # Boolean

# Example usage
print("Hello World!")
print("Welcome to Data Types in Python")
print("This is Integer Number",int_var)
print("This is Floating Point Number",float_var)
print("This is Complex Number",complex_var)
print("\n")

print("This is List",list_var)
print("This is Tuple",tuple_var)
print("This is Range",list(range_var))
print("This is String",str_var)
print("\n")

print("This is Dictionary",dict_var)
print("This is Set",set_var)
print("\n")

print("This is Boolean",bool_var)
print("\n")

#Expreimenting with different data types
int_var = int_var + 5
float_var = float_var * 2.0
complex_var = complex_var + (1 + 1j)
print("Updated Integer Number",int_var)
print("Updated Floating Point Number",float_var)
print("Updated Complex Number",complex_var)
print("\n")

print("First element of List:", list_var[0])
print("Second element of Tuple:", tuple_var[1])
print("String in uppercase:", str_var.upper())
print("Value associated with 'name' in Dictionary:", dict_var["name"])
print("\n")

a = ["Geeks", "For", "Geeks"]
print("Accessing element from the list")
print(a[0])
print(a[2])

print("Accessing element using negative indexing")
print(a[-1])
print(a[-3])

