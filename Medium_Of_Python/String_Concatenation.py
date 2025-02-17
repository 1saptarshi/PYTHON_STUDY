# # #String Concatenation

# String concatenation means combining two or more strings into a single string. In Python, we can concatenate strings using:

# Using + Operator (Basic Concatenation)
# Using join() Method (Efficient for Multiple Strings)
# Using f-strings (Formatted String Literals) - Python 3.6+
# Using .format() Method
# Using % Formatting (Old Style)


#1. Using + Operator (Basic Concatenation)
#The + operator joins two or more strings.
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2  # Adding a space between words
print(result)  # Output: Hello World


#2. Using join() Method (Efficient for Lists)
#The join() method is useful when concatenating multiple strings, especially in lists.
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)  # Output: Python is awesome


#3. Using f-strings (Formatted String Literals) - Python 3.6+
#f-strings provide an easy way to concatenate variables into a string.

name = "Alice"
age = 25
info = f"My name is {name} and I am {age} years old."
print(info)  # Output: My name is Alice and I am 25 years old.


#4. Using .format() Method

#The .format() method allows inserting variables into a string.

name = "Bob"
city = "New York"
message = "Hello, my name is {} and I live in {}.".format(name, city)
print(message)  # Output: Hello, my name is Bob and I live in New York.

#5. Using % Formatting (Old Style)
#The % operator was used before .format() and f-strings.
language = "Python"
version = 3.10
text = "I love %s version %.1f" % (language, version)
print(text)  # Output: I love Python version 3.1

