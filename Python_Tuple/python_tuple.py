 
 
## **1. Creating Tuples**
# A tuple is created using **parentheses `()`**.
 
# Creating a tuple
fruits = ("apple", "banana", "cherry")
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True)

print(fruits)  # Output: ('apple', 'banana', 'cherry')
print(numbers) # Output: (1, 2, 3, 4, 5)
print(mixed)   # Output: (1, 'hello', 3.14, True)
 

# ✅ **Tuples can hold different data types.**

 

## **2. Tuple with One Element**
# A tuple with **one item** must have a **trailing comma**.
 
single_element_tuple = ("hello",)  # Correct
not_a_tuple = ("hello")  # Incorrect, treated as a string

print(type(single_element_tuple))  # Output: <class 'tuple'>
print(type(not_a_tuple))  # Output: <class 'str'>
 

## **3. Accessing Tuple Elements**
# Tuples use **indexing (starting from `0`)** to access elements.
 
fruits = ("apple", "banana", "cherry")

# Access first element
print(fruits[0])  # Output: apple

# Access last element
print(fruits[-1])  # Output: cherry
 

# ✅ **Negative indexing** starts from `-1` (last element).
 

## **4. Slicing Tuples**
# Tuples support slicing like lists.
 
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(numbers[2:6])  # Output: (2, 3, 4, 5)
print(numbers[:4])   # Output: (0, 1, 2, 3)
print(numbers[5:])   # Output: (5, 6, 7, 8, 9)
print(numbers[-3:])  # Output: (7, 8, 9)
 

# ✅ **Slicing syntax:** `tuple[start:end:step]`

 
## **5. Tuple Length**
# Use `len()` to find the number of elements in a tuple.
 
fruits = ("apple", "banana", "cherry")
print(len(fruits))  # Output: 3
 

## **6. Immutable Nature of Tuples**
# Tuples **cannot be changed** after creation.
 
fruits = ("apple", "banana", "cherry")
fruits[1] = "mango"  # ❌ TypeError: 'tuple' object does not support item assignment
 

# ✅ **Workaround:** Convert tuple to **list**, modify, and convert back.
 
fruits = ("apple", "banana", "cherry")
temp_list = list(fruits)
temp_list[1] = "mango"
fruits = tuple(temp_list)

print(fruits)  # Output: ('apple', 'mango', 'cherry')
 

## **7. Looping Through Tuples**
### **7.1 Using `for` loop**
 
fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit)
 
### **7.2 Using `while` loop**
 
fruits = ("apple", "banana", "cherry")
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
 
# ## **8. Checking if an Item Exists**
# Use the `in` keyword.
 
fruits = ("apple", "banana", "cherry")
print("banana" in fruits)  # Output: True
print("grape" in fruits)   # Output: False
 

## **9. Tuple Concatenation & Repetition**
### **9.1 Concatenation using `+`**
 
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(result)  # Output: (1, 2, 3, 4, 5, 6)
 

### **9.2 Repetition using `*`**
 
numbers = (1, 2, 3)
result = numbers * 3
print(result)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)
 

## **10. Unpacking Tuples**
# Tuple **unpacking** assigns values to multiple variables.
 
fruits = ("apple", "banana", "cherry")

# Assign each value to a variable
fruit1, fruit2, fruit3 = fruits
print(fruit1)  # Output: apple
print(fruit2)  # Output: banana
print(fruit3)  # Output: cherry
 
# ✅ **Use `*` to collect multiple values**
 
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(first)   # Output: 1
print(middle)  # Output: [2, 3, 4]
print(last)    # Output: 5
 

## **11. Tuple Methods**
# | Method | Description |
# |--------|-------------|
# | `count(x)` | Returns the number of times `x` appears in the tuple |
# | `index(x)` | Returns the index of the first occurrence of `x` |

### **11.1 `count()` - Count occurrences**
 
numbers = (1, 2, 3, 1, 4, 1)
print(numbers.count(1))  # Output: 3
 

### **11.2 `index()` - Find the index**
 
numbers = (10, 20, 30, 40)
print(numbers.index(30))  # Output: 2
 

## **12. Converting Between Tuples and Lists**
### **12.1 Convert Tuple to List**
 
fruits = ("apple", "banana", "cherry")
fruits_list = list(fruits)
print(fruits_list)  # Output: ['apple', 'banana', 'cherry']
 

### **12.2 Convert List to Tuple**
 
fruits_list = ["apple", "banana", "cherry"]
fruits = tuple(fruits_list)
print(fruits)  # Output: ('apple', 'banana', 'cherry')
 

## **13. Using Tuples in Functions**
# Functions can **return multiple values** using tuples.
 
def calculate(x, y):
    sum_val = x + y
    diff_val = x - y
    return sum_val, diff_val  # Returns a tuple

result = calculate(10, 5)
print(result)       # Output: (15, 5)
print(result[0])    # Output: 15
print(result[1])    # Output: 5
