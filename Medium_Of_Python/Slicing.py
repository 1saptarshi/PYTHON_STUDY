# You can return a range of characters by using the slice syntax.

# Specify the start index and the end index, separated by a colon, to return a part of the string.


#String slicing allows you to extract specific portions of a string using indexing.


#1. Basic String Slicing 
text = "Hello, Python"

print(text[0:5])   # Output: Hello
print(text[7:13])  # Output: Python

#2. Omitting Start or End Index

#  If start is omitted, Python starts from the beginning (0).
# If end is omitted, Python slices till the end.
# Example: Slicing Without Start or End

text="python"

print(text[:2])
print(text[:1])
print(text[:6])


#3. Using Negative Indexing
# Python allows negative indexing, where:

# -1 represents the last character.
# -2 represents the second-last character, and so on.
# Example: Slicing with Negative Indexes


text = "Python"

print(text[-6:-3])  # Output: Pyt  (Characters from index -6 to -4)
print(text[-3:])    # Output: hon  (Last 3 characters)
print(text[:-3])    # Output: Pyt  (Everything except last 3 characters)

#4. Using Step in Slicing
#The step controls how many characters to skip.
#Slicing with Step
text = "Programming"

print(text[0:11:2])  # Output: Pormig  (Every 2nd character)
print(text[::3])     # Output: Pogi  (Every 3rd character)

#5. Reversing a String Using Slicing
#To reverse a string, use a step of -1.
text = "Python"

print(text[::-1])  # Output: nohtyP

#Operation	Slice Syntax	Output (For "Python")
# Get "Pyt"	text[0:3]	Pyt
# Get "thon"	text[2:]	thon
# Get "Pyth"	text[:4]	Pyth
# Get "yth"	text[1:4]	yth
# Get last 3 chars	text[-3:]	hon
# Reverse a string	text[::-1]	nohtyP
 