

## **1. Creating Lists**
# A list is defined using square brackets `[]`:
 
# Creating a list
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

print(fruits)  # Output: ['apple', 'banana', 'cherry']
print(numbers) # Output: [1, 2, 3, 4, 5]
print(mixed)   # Output: [1, 'hello', 3.14, True]
 

## **2. Accessing List Elements**
# Elements are accessed using an **index** (starting from `0`).

 
fruits = ["apple", "banana", "cherry"]

# Access first element
print(fruits[0])  # Output: apple

# Access last element
print(fruits[-1])  # Output: cherry
 

## **3. Changing List Items**
# Lists are **mutable**, meaning elements can be modified.

 
fruits = ["apple", "banana", "cherry"]
fruits[1] = "mango"
print(fruits)  # Output: ['apple', 'mango', 'cherry']
 

## **4. List Length**
# Use `len()` to find the number of elements in a list.

 
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # Output: 3
 

## **5. Adding Items to a List**
### **5.1 `append()` - Adds an element at the end**
 
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # Output: ['apple', 'banana', 'cherry']
 

### **5.2 `insert()` - Adds an element at a specific index**
 
fruits = ["apple", "banana"]
fruits.insert(1, "mango")
print(fruits)  # Output: ['apple', 'mango', 'banana']
 

### **5.3 `extend()` - Adds multiple elements**
 
fruits = ["apple", "banana"]
fruits.extend(["cherry", "grape"])
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'grape']
 
## **6. Removing Items from a List**
### **6.1 `remove()` - Removes a specific element**
 
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry']
 
### **6.2 `pop()` - Removes an element by index**
 
fruits = ["apple", "banana", "cherry"]
fruits.pop(1)  # Removes "banana"
print(fruits)  # Output: ['apple', 'cherry']
 

### **6.3 `del` - Deletes an element or the entire list**
 
fruits = ["apple", "banana", "cherry"]
del fruits[1]  # Removes "banana"
print(fruits)  # Output: ['apple', 'cherry']

# Delete the entire list
del fruits
 

### **6.4 `clear()` - Removes all elements**
 
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)  # Output: []
 

## **7. Looping Through a List**
### **7.1 Using a `for` loop**
 
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
 

### **7.2 Using `while` loop**
 
fruits = ["apple", "banana", "cherry"]
i = 0
while i < len(fruits):
    print(fruits[i])
 
 
### **7.3 Using List Comprehension**
 
fruits = ["apple", "banana", "cherry"]
[print(fruit) for fruit in fruits]
 
 

## **8. List Slicing**
 
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:6])  # Output: [2, 3, 4, 5]
print(numbers[:4])   # Output: [0, 1, 2, 3]
print(numbers[5:])   # Output: [5, 6, 7, 8, 9]
print(numbers[-3:])  # Output: [7, 8, 9]
 

 
## **9. Sorting Lists**
### **9.1 `sort()` - Sorts the list in ascending order**
 
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4]
 
### **9.2 `sort(reverse=True)` - Sorts in descending order**
 
numbers.sort(reverse=True)
print(numbers)  # Output: [4, 3, 2, 1]
 

### **9.3 `sorted()` - Returns a sorted copy without modifying the original**
 
numbers = [3, 1, 4, 2]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 2, 3, 4]
print(numbers)         # Original list remains unchanged
 

## **10. Copying a List**
 
fruits = ["apple", "banana", "cherry"]

# Copy using slicing
copy1 = fruits[:]

# Copy using list() function
copy2 = list(fruits)

# Copy using copy() method
copy3 = fruits.copy()

print(copy1, copy2, copy3)

 

## **11. Joining Two Lists**
### **11.1 Using `+` Operator**
 
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)  # Output: [1, 2, 3, 4, 5, 6]
 

### **11.2 Using `extend()`**
 
list1.extend(list2)
print(list1)  # Output: [1, 2, 3, 4, 5, 6]
 
# ## **12. List Methods Cheat Sheet**
# | Method | Description |
# |--------|-------------|
# | `append(x)` | Adds `x` to the end |
# | `insert(i, x)` | Inserts `x` at index `i` |
# | `remove(x)` | Removes first occurrence of `x` |
# | `pop(i)` | Removes element at index `i` |
# | `clear()` | Removes all elements |
# | `sort()` | Sorts the list |
# | `reverse()` | Reverses the list |
# | `index(x)` | Returns index of `x` |
# | `count(x)` | Returns count of `x` |
# | `copy()` | Returns a copy of the list |
# | `extend(iterable)` | Extends list with elements from `iterable` |

 

 