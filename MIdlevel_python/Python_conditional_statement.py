# **Python Conditional Statements: Complete Guide with Examples**  

# Conditional statements in Python 
# **control the flow of execution** 
# based on conditions (True/False). 
# They help in decision-making.

 

## **1. Types of Conditional Statements in Python**
# 1. `if` statement  
# 2. `if-else` statement  
# 3. `if-elif-else` statement  
# 4. **Nested `if` statement**  
# 5. **Ternary (short-hand `if-else`)**  

 
## **2. The `if` Statement**  
# Executes a block of code **only if** the condition is `True`.  
 
age = 18

if age >= 18:
    print("You are eligible to vote.")
 
# ✅ If `age` is **18 or more**, the message will be printed.  

 

## **3. The `if-else` Statement**  
# Executes **one block if the condition is `True`**, otherwise, another block is executed.  

 
age = 16

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
 
# ✅ Output: `You are not eligible to vote.`  

 
## **4. The `if-elif-else` Statement**  
# Checks **multiple conditions** in sequence.  
 
marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D")
 
# ✅ **Output:** `Grade: B`  

# 📌 **How it works:**  
# - If `marks >= 90`, prints `"Grade: A"` and exits.  
# - If `marks` is between **80-89**, prints `"Grade: B"`.  
# - If `marks` is between **70-79**, prints `"Grade: C"`.  
# - Else, it prints `"Grade: D"`.

 
## **5. Nested `if` Statement**  
# An `if` statement inside another `if` statement.

 
num = 10

if num > 0:
    print("Positive Number")
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
else:
    print("Negative Number")
# ```
# ✅ **Output:**  
# ```
# Positive Number
# Even Number
# ```
# 📌 **Explanation:**  
# - First `if` checks if `num > 0` (**Yes** → `"Positive Number"` is printed).  
# - Then, the inner `if` checks if `num` is even.

 
## **6. The Ternary Operator (Short-hand `if-else`)**  
# Python provides a **short-hand version** of `if-else`.
 
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)
# ```
# ✅ **Output:** `Adult`  

# 📌 **How it works:**  
# **Syntax:** `value_if_true if condition else value_if_false`

 
## **7. Boolean Conditions in `if` Statements**  
# Python treats some values as **False**:
# - `0` (Zero)
# - `None`
# - `""` (Empty string)
# - `[]` (Empty list)
# - `{}` (Empty dictionary)
# - `set()` (Empty set)
  
# All other values are considered **True**.

 
if "":
    print("This will not print.")
if 10:
    print("This will print.")
 
# ✅ **Output:** `This will print.`  

 
## **8. Using `and`, `or`, `not` in Conditions**
### **8.1 The `and` Operator**  
# All conditions **must be True** to execute the block.
 
age = 20
has_id = True

if age >= 18 and has_id:
    print("You can enter the club.")
else:
    print("Entry denied.")
 
# ✅ **Output:** `"You can enter the club."`  

 
### **8.2 The `or` Operator**  
# At least **one condition must be True**.
 
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's a weekday.")
 
# ✅ **Output:** `"It's the weekend!"`  

 
### **8.3 The `not` Operator**  
# Reverses a Boolean value.
 
is_raining = False

if not is_raining:
    print("Go outside!")
 
# ✅ **Output:** `"Go outside!"`  
 

## **9. Match-Case (Python 3.10+)**
# Python 3.10 introduced `match-case` (similar to `switch` in other languages).

 
day = "Monday"

match day:
    case "Monday":
        print("Start of the workweek.")
    case "Friday":
        print("Weekend is coming!")
    case _:
        print("A normal day.")
 
# ✅ **Output:** `"Start of the workweek."`  
  