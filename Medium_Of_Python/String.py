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

    
#7. String Length
#Use the len() function to find the length of a string.
text = "Hello, Python!"
print(len(text))  # Output: 14

#8. Check String (Substring Search)
#Use the in keyword to check if a substring exists in a string.
#Checking for a Substring
text = "Python is fun"
print("Python" in text)  # Output: True
print("Java" in text)    # Output: False


#9. Check if NOT in String
#Use not in to check if a substring is not in a string.
#Checking if a String is NOT Present
text = "Learning Python is fun"
print("Java" not in text)  # Output: True
print("Python" not in text)  # Output: False



# Concept	                    Explanation                       	Example

# Strings	           Sequence of characters in quotes	            "Hello"

# Quotes Inside Quotes	Using different quotes or escape character	'It\'s sunny'

# Assign to Variable	Store a string in a variable	msg = "Hello"

# Multiline Strings	Use triple quotes for multiple lines	"""Line1\nLine2"""

# Strings are Arrays	Access characters using index	s[0] → 'H'

# Loop Through String	Iterate with for loop	for char in s:

# String Length	Use len() to count characters	len("Hello") → 5

# Check String	Use "substring" in string	"Py" in "Python"

# Check if NOT 	Use "substring" not in string	"Java" not in "Python"
