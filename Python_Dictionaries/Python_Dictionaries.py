# **Python Dictionaries: Complete Guide with Examples**  

# A **dictionary** in Python is an **unordered, mutable (changeable) collection**
#  that stores **key-value pairs**. It is one of the most efficient ways to 
# **map unique keys to specific values**.
 
# ## **1. Creating a Dictionary**  
# Dictionaries are defined using **curly braces `{}`** or the `dict()` function.

 
# Creating a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(person)  
# Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Creating an empty dictionary
empty_dict = {}
print(type(empty_dict))  # Output: <class 'dict'>

# Creating a dictionary using dict() function
person = dict(name="Alice", age=25, city="New York")
print(person)
 

# ✅ **Keys must be unique and immutable** (strings, numbers, tuples).  
# ✅ **Values can be of any data type** (string, number, list, tuple, another dictionary, etc.).

 

## **2. Accessing Dictionary Elements**  
# Access values using **keys**.

 
person = {"name": "Alice", "age": 25, "city": "New York"}

# Accessing a value using a key
print(person["name"])  # Output: Alice

# Using get() to avoid KeyError if the key does not exist
print(person.get("age"))  # Output: 25
print(person.get("gender", "Not Found"))  # Output: Not Found
 
# ✅ `get()` prevents errors if the key is missing.

 

## **3. Changing Dictionary Values**  
# Dictionaries are **mutable**, so values can be updated.
 
person = {"name": "Alice", "age": 25, "city": "New York"}

# Updating a value
person["age"] = 30
print(person)  
# Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
 

# ✅ **Keys are case-sensitive**, `"Name"` and `"name"` are different.

 

## **4. Adding and Removing Items**
### **4.1 Adding a New Key-Value Pair**
 
person["gender"] = "Female"
print(person)  
# Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'gender': 'Female'}
 
### **4.2 Removing Elements**
#### **Using `pop()`**
 
person.pop("age")
print(person)  
# Output: {'name': 'Alice', 'city': 'New York', 'gender': 'Female'}
 
#### **Using `del`**
 
del person["city"]
print(person)  
# Output: {'name': 'Alice', 'gender': 'Female'}
 

#### **Using `popitem()` (Removes the last inserted item)**
 
person = {"name": "Alice", "age": 25, "city": "New York"}
person.popitem()
print(person)  
# Output: {'name': 'Alice', 'age': 25}
 

#### **Using `clear()` (Removes all items)**
 
person.clear()
print(person)  # Output: {}
 

## **5. Looping Through a Dictionary**
### **5.1 Looping Through Keys**
 
person = {"name": "Alice", "age": 25, "city": "New York"}
for key in person:
    print(key)
 
# **Output:**
 
# name
# age
# city
 
### **5.2 Looping Through Values**
 
for value in person.values():
    print(value)
 
# **Output:**
 
# Alice
# 25
# New York
 

### **5.3 Looping Through Key-Value Pairs**
 
for key, value in person.items():
    print(key, ":", value)
 
# **Output:**
 
# name : Alice
# age   : 25
# city : New York
 
 
# ## **6. Checking if a Key Exists**
# Use the `in` keyword to check if a key exists.
 
person = {"name": "Alice", "age": 25}
print("name" in person)  # Output: True
print("gender" in person)  # Output: False
 

## **7. Copying a Dictionary**
### **7.1 Using `copy()`**
 
person_copy = person.copy()
print(person_copy)  
 
### **7.2 Using `dict()`**
 
person_copy = dict(person)
print(person_copy)  
 
#✅ **Avoid using `=` as it creates a reference instead of a new copy.**
 
## **8. Nested Dictionaries**
# Dictionaries can contain other dictionaries.
 
students = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob", "age": 22}
}

print(students["student1"]["name"])  # Output: Alice

## **10. Dictionary Comprehension**
# Python allows **short-hand** dictionary creation.

 
squares = {x: x*x for x in range(1, 6)}
print(squares)  
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
 


 #zip funtion