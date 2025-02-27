# **Python `while` Loops: Complete Guide with Examples**  

# A **`while` loop** in Python **executes a block of code repeatedly** as long as a **given condition is `True`**.

 

## **1. Syntax of `while` Loop**
 
# while condition:
    # Code to execute
 
# ✅ **The loop runs until the condition becomes `False`.**

 

## **2. Basic `while` Loop Example**
 
count = 1

while count <= 5:
    print("Iteration:", count)
    count += 1
# ```
# **Output:**
# ```
# Iteration: 1
# Iteration: 2
# Iteration: 3
# Iteration: 4
# Iteration: 5
 
# 📌 **Explanation:**  
# - The loop starts with `count = 1`.  
# - It **runs until** `count` reaches **5**.  
# - `count += 1` increments `count` in each iteration.  

 

## **3. Infinite Loop (Avoid This!)**  
# A loop runs **forever** if the condition **never becomes False**.

 
while True:
    print("This is an infinite loop!")
 
# 📌 **To stop an infinite loop manually, use:**  
# - **CTRL + C** (in terminal)  
# - **Stop button** (in some editors)  

 
## **4. Using `break` to Exit a `while` Loop**  
# `break` **stops** the loop **immediately**.

 
count = 1

while count <= 5:
    if count == 3:
        break
    print("Count:", count)
    count += 1
 
# **Output:**
 
# Count: 1
# Count: 2
 
# ✅ **The loop stops when `count == 3`.**  
 
## **5. Using `continue` to Skip an Iteration**  
# `continue` **skips the rest of the current iteration** and moves to the next one.

 
count = 0

while count < 5:
    count += 1
    if count == 3:
        continue
    print("Count:", count)
 
# **Output:**
 
# Count: 1
# Count: 2
# Count: 4
# Count: 5
# ✅ **Iteration `3` is skipped.**  

 

## **6. Using `else` with `while`**
# The `else` block **executes after the loop completes normally** (not when `break` is used).

 
count = 1

while count <= 3:
    print("Count:", count)
    count += 1
else:
    print("Loop finished!")
 
# **Output:**
 ``
# Count: 1
# Count: 2
# Count: 3
# Loop finished!
 

## **7. `while` Loop with User Input**
 
password = ""

while password != "python123":
    password = input("Enter password: ")

print("Access granted!")
 
# ✅ The loop **keeps running** until the user enters `"python123"`.  
 

## **8. Using `while` Loop for List Iteration**
 
fruits = ["apple", "banana", "cherry"]
i = 0

while i < len(fruits):
    print(fruits[i])
    i += 1
 
# **Output:**
 
apple
banana
cherry
 
## **9. Nested `while` Loops**
# A **`while` loop inside another `while` loop**.

 
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"Outer: {i}, Inner: {j}")
        j += 1
    i += 1
 
# **Output:**
 
# Outer: 1, Inner: 1
# Outer: 1, Inner: 2
# Outer: 2, Inner: 1
# Outer: 2, Inner: 2
# Outer: 3, Inner: 1
# Outer: 3, Inner: 2
 

## **10. `while` Loop with Random Numbers (`random` Module)**
 
import random

number = 0

while number != 5:
    number = random.randint(1, 10)
    print("Generated number:", number)
 
# ✅ The loop **keeps running** until `5` is generated.
 

 