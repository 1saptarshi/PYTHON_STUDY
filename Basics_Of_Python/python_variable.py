#Numeric Variables
#a.Integer (int)

x = 10  # Integer
print(type(x))  # Output: <class 'int'>

#b. Float (float)
y = 10.5  # Float
print(type(y))  # Output: <class 'float'>
#c. Complex (complex)
z = 3 + 4j  # Complex Number
print(type(z))  # Output: <class 'complex'>

#String Variable (str)
name = "Alice"
print(type(name))  # Output: <class 'str'>


#Boolean Variable (bool)
is_active = True
print(type(is_active))  # Output: <class 'bool'>
#Sequence Types
#List (list) - Mutable (Can be changed)
fruits = ["Apple", "Banana", "Cherry"]
print(type(fruits))  # Output: <class 'list'>

#Tuple (tuple) - Immutable (Cannot be changed)
colors = ("Red", "Green", "Blue")
print(type(colors))  # Output: <class 'tuple'>

# Range (range) - Used for generating sequences
numbers = range(5)  # Generates 0,1,2,3,4
print(type(numbers))  # Output: <class 'range'>

#Set Types
#Set (set) - Unordered collection of unique elements
unique_numbers = {1, 2, 3, 4, 4, 5}
print(type(unique_numbers))  # Output: <class 'set'>

# Frozen Set (frozenset) - Immutable version of a set
frozen_numbers = frozenset([1, 2, 3, 4, 5])
print(type(frozen_numbers))  # Output: <class 'frozenset'>

#Dictionary Type (dict) - Key-Value Pairs
person = {"name": "John", "age": 30}
print(type(person))  # Output: <class 'dict'>

#Binary Types
#Bytes (bytes)
byte_data = b"Hello"
print(type(byte_data))  # Output: <class 'bytes'>

#Bytearray (bytearray)
byte_array = bytearray(5)  # Creates a bytearray of size 5
print(type(byte_array))  # Output: <class 'bytearray'>

#Memoryview (memoryview)
memory = memoryview(byte_data)
print(type(memory))  # Output: <class 'memoryview'>

#None Type (NoneType)
empty_value = None
print(type(empty_value))  # Output: <class 'NoneType'>


# Data Type	Example
# int	x = 10
# float	y = 10.5
# complex	z = 3 + 4j
# str name = "Alice"
# bool is_active = True
# list	fruits = ["Apple", "Banana"]
# tuple	colors = ("Red", "Green")
# range	numbers = range(5)
# set	unique_numbers = {1, 2, 3}
# frozenset	frozen_numbers = frozenset([1, 2, 3])
# dict	person = {"name": "John"}
# bytes	byte_data = b"Hello"
# bytearray	byte_array = bytearray(5)
# memoryview	memory = memoryview(byte_data)
# NoneType	empty_value = None