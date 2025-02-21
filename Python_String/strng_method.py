## **Python String Methods with Examples**

### **1. Changing Case**
#### **1.1 `capitalize()` - Converts the first character to uppercase**
 
text = "hello world"
print(text.capitalize())  # Output: Hello world

#### **1.2 `casefold()` - Converts string into lowercase (more aggressive than `lower()`)**
 
text = "HELLO WORLD"
print(text.casefold())  # Output: hello world


#### **1.3 `upper()` - Converts all characters to uppercase**
 
text = "hello world"
print(text.upper())  # Output: HELLO WORLD
 

#### **1.4 `lower()` - Converts all characters to lowercase**
 
text = "Hello World"
print(text.lower())  # Output: hello world
 

#### **1.5 `swapcase()` - Swaps uppercase to lowercase and vice versa**
 
text = "Hello World"
print(text.swapcase())  # Output: hELLO wORLD
 

#### **1.6 `title()` - Capitalizes the first letter of each word**
 
text = "hello world"
print(text.title())  # Output: Hello World
 

### **2. Finding and Checking Substrings**
#### **2.1 `find()` - Finds the first occurrence of a substring**
 
text = "Python programming is fun"
print(text.find("programming"))  # Output: 7
 

#### **2.2 `index()` - Finds the first occurrence (raises error if not found)**
 
text = "Python programming"
print(text.index("Python"))  # Output: 0
 

#### **2.3 `rfind()` - Finds the last occurrence of a substring**
 
text = "Python is fun and Python is powerful"
print(text.rfind("Python"))  # Output: 16
 

#### **2.4 `rindex()` - Finds the last occurrence (raises error if not found)**
 
text = "Python is fun and Python is powerful"
print(text.rindex("Python"))  # Output: 16
 
 

### **3. String Validation Methods**
#### **3.1 `isalnum()` - Checks if string is alphanumeric**
 
text = "Python123"
print(text.isalnum())  # Output: True
 

#### **3.2 `isalpha()` - Checks if string contains only letters**
 
text = "Python"
print(text.isalpha())  # Output: True
 

#### **3.3 `isdigit()` - Checks if string contains only digits**
 
text = "12345"
print(text.isdigit())  # Output: True
 

#### **3.4 `isnumeric()` - Checks if string contains only numeric values**
 
text = "²3456"
print(text.isnumeric())  # Output: True
 
#### **3.5 `isspace()` - Checks if string contains only whitespace**
 
text = "   "
print(text.isspace())  # Output: True
 

#### **3.6 `istitle()` - Checks if the string follows title case rules**
 
text = "Hello World"
print(text.istitle())  # Output: True
 

#### **3.7 `islower()` - Checks if all characters are lowercase**
 
text = "hello"
print(text.islower())  # Output: True
 

#### **3.8 `isupper()` - Checks if all characters are uppercase**
 
text = "HELLO"
print(text.isupper())  # Output: True
 
#### **3.9 `isprintable()` - Checks if all characters are printable**
 
text = "Hello\nWorld"
print(text.isprintable())  # Output: False
 

 

### **4. Modifying Strings**
#### **4.1 `strip()` - Removes leading and trailing spaces**
 
text = "   Hello World   "
print(text.strip())  # Output: "Hello World"
 
#### **4.2 `lstrip()` - Removes leading spaces**
 
text = "   Hello World"
print(text.lstrip())  # Output: "Hello World"
 
#### **4.3 `rstrip()` - Removes trailing spaces**
 
text = "Hello World   "
print(text.rstrip())  # Output: "Hello World"
 

 

### **5. Replacing and Formatting Strings**
#### **5.1 `replace()` - Replaces a substring with another**
 
text = "Hello World"
print(text.replace("World", "Python"))  # Output: Hello Python
 

#### **5.2 `format()` - Inserts values into a string**
 
name = "Alice"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
 

#### **5.3 `f-strings` (Python 3.6+)**
 
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
 

 

### **6. Splitting and Joining Strings**
#### **6.1 `split()` - Splits a string into a list**
 
text = "apple,banana,grape"
print(text.split(","))  # Output: ['apple', 'banana', 'grape']
 
#### **6.2 `rsplit()` - Splits from the right side**
 
text = "apple banana grape"
print(text.rsplit(" ", 1))  # Output: ['apple banana', 'grape']
 

#### **6.3 `splitlines()` - Splits by line breaks**
 
text = "Hello\nWorld"
print(text.splitlines())  # Output: ['Hello', 'World']
 

#### **6.4 `join()` - Joins a list into a string**
 
words = ["Python", "is", "fun"]
print(" ".join(words))  # Output: Python is fun
 
  

### **7. Padding and Justifying**
#### **7.1 `center()` - Centers a string with spaces**
 
text = "Python"
print(text.center(20, "-"))  # Output: "-------Python--------"
 

#### **7.2 `ljust()` - Left aligns a string**
 
text = "Python"
print(text.ljust(10, "-"))  # Output: "Python----"
 

#### **7.3 `rjust()` - Right aligns a string**
 
text = "Python"
print(text.rjust(10, "-"))  # Output: "----Python"
 

#### **7.4 `zfill()` - Fills the string with zeroes from the left**
 
text = "42"
print(text.zfill(5))  # Output: "00042"
 

 