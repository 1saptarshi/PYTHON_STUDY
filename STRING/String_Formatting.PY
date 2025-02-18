#1. String .format() Method
#The .format() method replaces {} placeholders with specified values.
name = "Alice"
age = 25
message = "My name is {} and I am {} years old.".format(name, age)
print(message)
# Output: My name is Alice and I am 25 years old.

#Positional and Named Arguments
# Positional Arguments
sentence = "I love {0} and {1}.".format("Python", "JavaScript")
print(sentence)  
# Output: I love Python and JavaScript.

# Named Arguments
info = "My name is {name} and I live in {city}.".format(name="Bob", city="New York")
print(info)  
# Output: My name is Bob and I live in New York.

#2. f-strings (Formatted String Literals)
#Introduced in Python 3.6, f-strings provide an easy and readable way to format strings.
name = "Charlie"
age = 30
message = f"My name is {name} and I am {age} years old."
print(message)
# Output: My name is Charlie and I am 30 years old.

#Inline Expressions in f-strings
a = 10
b = 5
print(f"Sum: {a + b}, Product: {a * b}")
# Output: Sum: 15, Product: 50

#3. Placeholders using % Formatting (Old Style)
#Older Python versions used % for string formatting.
language = "Python"
version = 3.10
text = "I love %s version %.1f" % (language, version)
print(text)
# Output: I love Python version 3.1

#Multiple Variables
name = "David"
age = 35
info = "My name is %s and I am %d years old." % (name, age)
print(info)
# Output: My name is David and I am 35 years old.


#4. Modifiers for Number Formatting
#Python provides special formatting options for numbers, decimals, and alignment.
#1. Decimal Formatting
num = 12.34567
print(f"Rounded: {num:.2f}")  # Output: Rounded: 12.35

#2. Integer Padding
num = 42
print(f"Padded: {num:05}")  # Output: Padded: 00042

#3. Aligning Text
text = "Python"
print(f"Left:  [{text:<10}]")   # Output: Left:  [Python    ]
print(f"Right: [{text:>10}]")   # Output: Right: [    Python]
print(f"Center:[{text:^10}]")   # Output: Center:[  Python  ]
