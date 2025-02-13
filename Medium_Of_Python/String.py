#Strings in Python

#A string in Python is a sequence of characters enclosed in 
# single ('), double ("), or triple (''' or """) quotes.

# Declaring Strings

# Single and Double Quotes
str1 = 'Hello'
str2 = "Python"

print(str1)  # Output: Hello
print(str2)  # Output: Python


#2. Quotes Inside Quotes

#You can use different types of quotes to include quotes inside a string.

#Using Quotes Inside a String

# Using double quotes inside single quotes
str1 = 'He said, "Python is awesome!"'

# Using single quotes inside double quotes
str2 = "It's a beautiful day"

# Using escape character (\) to include same type of quotes
str3 = 'It\'s a sunny day'
str4 = "He said, \"Python is amazing!\""

print(str1)  # Output: He said, "Python is awesome!"
print(str2)  # Output: It's a beautiful day
print(str3)  # Output: It's a sunny day
print(str4)  # Output: He said, "Python is amazing!"


#3. Assign String to a Variable

#Instead of using direct strings, assign them to variables.

#Assigning a String to a Variable

greeting = "Hello, World!"
print(greeting)  # Output: Hello, World!

#4. Multiline Strings

#Use triple quotes (''' or """) to define a string spanning multiple lines.

# Creating Multiline Strings

message = """This is a
multiline string
in Python."""
print(message)

#5. Strings are Arrays
#Strings behave like arrays, meaning you can access individual characters using indexing.

#Accessing String Characters

text = "Python"
print(text[3])  # Output: P
print(text[5])  # Output: h


#6. Looping Through a String

#You can iterate through a string using a for loop.

text = "Python"
for char in text:
    print(char)
