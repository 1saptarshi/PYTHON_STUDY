# **Python Sets: Complete Guide with Examples**  

# A **set** is an **unordered, mutable collection** that **does not allow duplicate values**.
#  It is commonly used for **mathematical operations like union, intersection, and difference**.

 

## **1. Creating a Set**  
# A **set** is defined using **curly braces `{}`** or the `set()` function.
 
# Creating a set
fruits = {"apple", "banana", "cherry"}
print(fruits)  # Output: {'banana', 'cherry', 'apple'}

# Creating a set using set() function
numbers = set([1, 2, 3, 4, 5])
print(numbers)  # Output: {1, 2, 3, 4, 5}

# Creating an empty set (Must use set(), `{}` creates an empty dictionary)
empty_set = set()
print(type(empty_set))  # Output: <class 'set'>
 
# ✅ **Sets are unordered, meaning elements appear in a random order.**
 

## **2. No Duplicate Values in Sets**  
# Sets **automatically remove duplicates**.
 
numbers = {1, 2, 2, 3, 4, 4, 5}
print(numbers)  # Output: {1, 2, 3, 4, 5}
 

## **3. Accessing Set Elements**  
# Sets **do not support indexing** (since they are unordered), 
# but you can iterate through them.
 
fruits = {"apple", "banana", "cherry"}
for fruit in fruits:
    print(fruit)
 

## **4. Adding and Removing Elements**  
### **4.1 `add()` - Adds an element to a set**
 
fruits = {"apple", "banana"}
fruits.add("cherry")
print(fruits)  # Output: {'apple', 'banana', 'cherry'}
 
### **4.2 `update()` - Adds multiple elements**
 
fruits = {"apple", "banana"}
fruits.update(["cherry", "grape"])
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'grape'}
 
### **4.3 `remove()` - Removes an element (Error if not found)**
 
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)  # Output: {'apple', 'cherry'}
 
### **4.4 `discard()` - Removes an element (No error if not found)**
 
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)  # Output: {'apple', 'cherry'}
 
### **4.5 `pop()` - Removes and returns a random element**
 
fruits = {"apple", "banana", "cherry"}
removed_item = fruits.pop()
print(removed_item)  # Randomly removed item
print(fruits)  # Remaining set
 
### **4.6 `clear()` - Removes all elements from a set**
 
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)  # Output: set()
 

## **5. Set Operations (Union, Intersection, Difference)**
### **5.1 `union()` - Combines two sets (removes duplicates)**
 
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print(result)  # Output: {1, 2, 3, 4, 5}
 
### **5.2 `intersection()` - Returns common elements**
 
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.intersection(set2)
print(result)  # Output: {2, 3}
 

### **5.3 `difference()` - Returns elements in `set1` but not in `set2`**
 
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.difference(set2)
print(result)  # Output: {1}
 

### **5.4 `symmetric_difference()` - Returns elements in either set but not both**
 
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.symmetric_difference(set2)
print(result)  # Output: {1, 4}
 

## **6. Checking Set Properties**
### **6.1 `issubset()` - Checks if a set is a subset of another**
 
set1 = {1, 2}
set2 = {1, 2, 3, 4}
print(set1.issubset(set2))  # Output: True
 
### **6.2 `issuperset()` - Checks if a set is a superset of another**
 
set1 = {1, 2, 3, 4}
set2 = {2, 3}
print(set1.issuperset(set2))  # Output: True
 

### **6.3 `isdisjoint()` - Checks if sets have no common elements**
 
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2))  # Output: True
 
## **7. Copying a Set**
### **7.1 Using `copy()`**
 
original_set = {1, 2, 3}
copied_set = original_set.copy()
print(copied_set)  # Output: {1, 2, 3}
 

## **8. Frozen Sets (Immutable Sets)**
# A **frozenset** is an **immutable** version of a set.
 
fruits = frozenset(["apple", "banana", "cherry"])
print(fruits)  # Output: frozenset({'banana', 'cherry', 'apple'})

# ❌ fruits.add("grape")  # TypeError: 'frozenset' object has no attribute 'add'
 

# ## **📌 Set Methods Cheat Sheet**
# | Method | Description |
# |--------|-------------|
# | `add(x)` | Adds `x` to the set |
# | `update(iterable)` | Adds multiple elements |
# | `remove(x)` | Removes `x` (Error if not found) |
# | `discard(x)` | Removes `x` (No error if not found) |
# | `pop()` | Removes a random element |
# | `clear()` | Removes all elements |
# | `union(set2)` | Combines two sets |
# | `intersection(set2)` | Finds common elements |
# | `difference(set2)` | Finds unique elements of the first set |
# | `symmetric_difference(set2)` | Finds elements in either set but not both |
# | `issubset(set2)` | Checks if a set is a subset |
# | `issuperset(set2)` | Checks if a set is a superset |
# | `isdisjoint(set2)` | Checks if sets have no common elements |
# | `copy()` | Returns a copy of the set |

 

 