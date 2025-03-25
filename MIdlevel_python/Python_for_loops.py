

## 1️⃣ **Iterating Over a List**
# A `for` loop can go through each element in a list.
 
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
 
# **Output:**
# ```
# apple
# banana
# cherry
 
## 2️⃣ **Using `range()` in a `for` Loop**
# The `range()` function generates a sequence of numbers.

### 🟢 Example: Looping through a range of numbers
 
for i in range(5):
    print(i)
 
# **Output:**
# ```
# 0
# 1
# 2
# 3
# 4
 
# 📌 `range(5)` generates numbers from `0` to `4` (not including `5`).

 

## 3️⃣ **Using `range(start, stop, step)`**
# We can specify a `start`, `stop`, and `step` value in `range()`.
 
for i in range(2, 10, 2):
    print(i)
 
# **Output:**
# ```
# 2
# 4
# 6
# 8
 
# 📌 The loop starts at `2`, ends before `10`, and increments by `2`.
 

## 4️⃣ **Iterating Over a String**
# A string is a sequence of characters, so we can loop through it.
 
for char in "Python":
    print(char)
 
# **Output:**
# ```
# P
# y
# t
# h
# o
# n
 
## 5️⃣ **Iterating Over a Tuple**
# Tuples work the same way as lists.
 
numbers = (1, 2, 3, 4)
for num in numbers:
    print(num)
 
# **Output:**
# ```
# 1
# 2
# 3
# 4
 

## 6️⃣ **Iterating Over a Dictionary**
# When looping through a dictionary, we can access keys and values.

### 🟢 Example: Looping through keys
 
person = {"name": "John", "age": 25, "city": "New York"}
for key in person:
    print(key)
 
# **Output:**
 
# name
# age
# city
 

### 🟢 Example: Looping through keys and values
 
for key, value in person.items():
    print(f"{key}: {value}")
 
# **Output:**
 
# name: John
# age: 25
# city: New York
 

## 7️⃣ **Using `else` with `for` Loops**
# An `else` block can be used with a `for` loop. It runs when the loop completes normally.

 
for i in range(3):
    print(i)
else:
    print("Loop completed!")
 
# **Output:**
# ```
# 0
# 1
# 2
# Loop completed!
 

# 📌 If a `break` statement interrupts the loop, the `else` block won’t execute.

 
for i in range(3):
    print(i)
    if i == 1:
        break
else:
    print("Loop completed!")  # This won't execute
 
# **Output:**
# ```
# 0
# 1
 

## 8️⃣ **Nested `for` Loops**
# A `for` loop inside another `for` loop is called a **nested loop**.

 
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
 
# **Output:**
# ```
# i=0, j=0
# i=0, j=1
# i=1, j=0
# i=1, j=1
# i=2, j=0
# i=2, j=1
 

## 9️⃣ **Using `break` in a `for` Loop**
# The `break` statement exits the loop immediately.

 
for i in range(5):
    if i == 3:
        break
    print(i)
 
# **Output:**
# ```
# 0
# 1
# 2
 

## 🔟 **Using `continue` in a `for` Loop**
# The `continue` statement skips the current iteration and moves to the next one.

 
for i in range(5):
    if i == 2:
        continue
    print(i)
 
# **Output:**
 
# 0
# 1
# 3
# 4
 
# 📌 When `i == 2`, `continue` skips that iteration.
 

## 1️⃣1️⃣ **Using `pass` in a `for` Loop**
# The `pass` statement is a placeholder that does nothing.

 
for i in range(5):
    if i == 2:
        pass  # Placeholder
    print(i)
 
# **Output:**
# ```
# 0
# 1
# 2
# 3
# 4
 
# 📌 The `pass` statement allows us to have an empty loop body.

 

## 1️⃣2️⃣ **List Comprehension with `for` Loops**
# Python allows compact loop expressions using **list comprehension**.

 
squares = [x**2 for x in range(5)]
print(squares)
 
# **Output:**

[0, 1, 4, 9, 16]
 

# ## 🔥 **Summary of `for` Loop Features**
# ✅ Loops through sequences (lists, tuples, dictionaries, strings)  
# ✅ Can use `range()` for numerical loops  
# ✅ Can have an `else` block  
# ✅ Supports `break`, `continue`, and `pass`  
# ✅ Can be nested inside other loops  
# ✅ Supports list comprehension  

 
 