# **Python Boolean: Complete Guide with Examples**

# ## **What is a Boolean in Python?**
# A Boolean represents one of two values:  
# ✅ **`True`**  
# ❌ **`False`**  

# Booleans are commonly used in **comparisons, conditions, and logical operations**.

 

## **1. Boolean Values in Python**
# Python has two built-in Boolean values:
 
print(True)   # Output: True
print(False)  # Output: False
# ```
# Booleans are case-sensitive, so writing **`true`** or **`false`** will cause an error.

 

## **2. Checking Boolean Type**
# Booleans are of type `bool` in Python.
 
print(type(True))   # Output: <class 'bool'>
print(type(False))  # Output: <class 'bool'>
 
 

## **3. Boolean as the Result of a Comparison**
# Comparison operators return Boolean values.
 
print(10 > 5)   # Output: True
print(10 < 5)   # Output: False
print(10 == 10) # Output: True
print(10 != 5)  # Output: True
 
# ### **Comparison Operators:**
# | Operator | Description | Example (`a=10, b=5`) | Output |
# |----------|-------------|------------|--------|
# | `==`     | Equal to    | `a == b`   | False  |
# | `!=`     | Not equal to | `a != b` | True |
# | `>`      | Greater than | `a > b`   | True |
# | `<`      | Less than | `a < b` | False |
# | `>=`     | Greater than or equal | `a >= b` | True |
# | `<=`     | Less than or equal | `a <= b` | False |

 

## **4. Boolean as the Result of Logical Operations**
# Python provides three logical operators: `and`, `or`, and `not`.

### **4.1 `and` Operator (Returns `True` if both conditions are true)**
 
print(True and True)   # Output: True
print(True and False)  # Output: False
print(5 > 2 and 10 > 5)  # Output: True
 

### **4.2 `or` Operator (Returns `True` if at least one condition is true)**
 
print(True or False)  # Output: True
print(False or False) # Output: False
print(5 > 2 or 10 < 5)  # Output: True
 

### **4.3 `not` Operator (Reverses the Boolean value)**
 
print(not True)  # Output: False
print(not False) # Output: True
print(not (5 > 2))  # Output: False
 

 

## **5. Boolean in Conditional Statements**
# Booleans are used in `if`, `elif`, and `else` conditions.
 
x = 10
if x > 5:
    print("x is greater than 5")  # Output: x is greater than 5
 
 

## **6. Boolean and Python Built-in Functions**
### **6.1 `bool()` Function**
# Python automatically converts values to `True` or `False`.

# #### **Falsy Values (Evaluates to `False`)**
# These values are considered `False` in Python:
# - `None`
# - `False`
# - `0` (Integer)
# - `0.0` (Float)
# - `""` (Empty String)
# - `[]` (Empty List)
# - `{}` (Empty Dictionary)
# - `set()` (Empty Set)

 
print(bool(0))      # Output: False
print(bool(""))     # Output: False
print(bool([]))     # Output: False
print(bool(None))   # Output: False
 

#### **Truthy Values (Evaluates to `True`)**
# Any non-empty or non-zero value is considered `True`:
 
print(bool(100))   # Output: True
print(bool("Hello"))  # Output: True
print(bool([1, 2, 3]))  # Output: True
 

 

## **7. Boolean in Python Functions**
# Functions return `True` or `False` when conditions are met.

 
def is_even(num):
    return num % 2 == 0

print(is_even(10))  # Output: True
print(is_even(7))   # Output: False
 
 

## **8. Boolean Operators in Membership and Identity**
### **8.1 `in` Operator (Membership Test)**
# Checks if a value exists inside a sequence.
 
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # Output: True
print("grape" in fruits)   # Output: False
 
### **8.2 `is` Operator (Identity Test)**
# Checks if two objects refer to the same memory location.
 
a = [1, 2, 3]
b = a
print(a is b)  # Output: True (Both refer to the same object)

c = [1, 2, 3]
print(a is c)  # Output: False (Different objects)
 
 

## **9. Using Booleans with Lists and Loops**
### **9.1 Filtering with Boolean Conditions**
 
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6]
 
### **9.2 While Loops with Boolean Conditions**
 
count = 5
while count > 0:
    print(count)
    count -= 1
 
# **Output:**
 
# 5
# 4
# 3
# 2
# 1
