#Python - Escape Characters


#1. Using Escape Characters in Strings
print("She said, \"Python is amazing!\"")  # Output: She said, "Python is amazing!"
print('It\'s a great day!')  # Output: It's a great day!

#2. Adding a New Line with \n
print("Hello\nWorld")
# Output:
# Hello
# World

#3. Using a Tab Space with \t
print("Python\tProgramming")  
# Output: Python    Programming

#4. Using Backslash \\
print("This is a backslash: \\")  
# Output: This is a backslash: \

#5. Using Carriage Return \r
print("Hello\rWorld")  
# Output: World (Replaces 'Hello' with 'World')


#6. Using Backspace \b
print("Hello\bWorld")  
# Output: HellWorld (Removes 'o' before 'W')

#7. Using Octal \ooo and Hex \xhh Values
print("\110\145\154\154\157")  # Output: Hello (Octal Representation)
print("\x48\x65\x6C\x6C\x6F")  # Output: Hello (Hex Representation)

