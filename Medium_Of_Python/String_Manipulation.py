#String Manipulation in Python

#Python provides various built-in methods 
# to manipulate strings efficiently. Below, 
# we'll explore uppercase conversion, lowercase
#  conversion, whitespace removal, and string
#  replacement with explanations and code examples.


#1. Convert String to Upper Case

#The upper() method converts all characters in a string to uppercase.

text = "hello world"
uppercase_text = text.upper()
print(uppercase_text)  # Output: HELLO WORLD

#2. Convert String to Lower Case
#The lower() method converts all characters to lowercase.
text = "Hello World"
lowercase_text = text.lower()
print(lowercase_text)  # Output: hello world

#3. Remove Whitespace
#The strip() method removes leading and trailing spaces.
# Python also has:

# lstrip() → Removes spaces from the left.
# rstrip() → Removes spaces from the right.
text = "  Python is awesome  "
stripped_text = text.strip()
print(stripped_text)   # Output: Python is awesome

left_stripped = text.lstrip()
print(left_stripped)   # Output: "Python is awesome  "

right_stripped = text.rstrip()
print(right_stripped)  # Output: "  Python is awesome"

#4. Replace a Substring in a String
#The replace(old, new) method replaces occurrences of a substring.
text = "I love Java"
new_text = text.replace("Java", "Python")
print(new_text)  # Output: I love Python
