# Here's a complete overview of **Python arrays**, specifically lists (since native arrays in Python are most commonly implemented using `list`), including **everything you've mentioned** and **additional important points**:

 

# ### ✅ **Python List (Array) - Full Guide**

# #### 🧱 **Definition**

# * A list in Python is an ordered, mutable (changeable) collection of elements.
# * Lists can contain elements of **different data types**.

 
my_list = [1, 2, 3, "Hello", True]
 

 

### 📌 **Common List Methods (with Description)**

# | Method             | Description                                                    |
# | ------------------ | -------------------------------------------------------------- |
# | `append(x)`        | Adds an element `x` at the end of the list                     |
# | `clear()`          | Removes all the elements from the list                         |
# | `copy()`           | Returns a **shallow copy** of the list                         |
# | `count(x)`         | Returns the number of times `x` appears in the list            |
# | `extend(iterable)` | Adds elements of an iterable (list, tuple, etc.) to the end    |
# | `index(x)`         | Returns the index of the first occurrence of `x`               |
# | `insert(i, x)`     | Inserts `x` at index `i`                                       |
# | `pop([i])`         | Removes and returns the element at index `i` (last by default) |
# | `remove(x)`        | Removes the **first occurrence** of value `x`                  |
# | `reverse()`        | Reverses the list in-place                                     |
# | `sort()`           | Sorts the list in-place (ascending by default)                 |

 

### 🔄 **Other Useful Operations**

#### ✅ **Creating Lists**

 
lst = list()          # Empty list
lst2 = [1, 2, 3]      # List with elements
 

#### ✅ **List Slicing**
 
a = [0, 1, 2, 3, 4]
print(a[1:4])   # Output: [1, 2, 3]
 

#### ✅ **List Comprehension**
 
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
 

#### ✅ **Membership Test**

 
3 in [1, 2, 3]     # True
 

 

### 🔍 **Looping Through a List**

 
for item in my_list:
    print(item)
 

### 🎯 **Built-in Functions with Lists**

# | Function      | Description                                              |
# | ------------- | -------------------------------------------------------- |
# | `len(lst)`    | Number of elements in the list                           |
# | `max(lst)`    | Maximum element                                          |
# | `min(lst)`    | Minimum element                                          |
# | `sum(lst)`    | Sum of elements                                          |
# | `sorted(lst)` | Returns a new sorted list without modifying the original |

 

### 🛠️ **List vs Array (From `array` module)**

# * Python also has an `array` module:

 
from array import array
arr = array('i', [1, 2, 3])  # Only stores integers
 

# * Use `array` module if you need **typed arrays** for performance.
 

### ⚠️ **Important Notes**

# * Lists are **mutable** – you can change elements:
 
a[0] = 100
 

# * `list.sort()` modifies the list in place. Use `sorted()` to return a new sorted list.
# * Lists support **nesting**:
 
matrix = [[1, 2], [3, 4]]
 

### 🧠 **Advanced List Methods/Concepts**

# | Method/Concept      | Description                              |
# | ------------------- | ---------------------------------------- |
# | `del lst[i]`        | Deletes the element at index `i`         |
# | `lst[i:j:k]`        | Advanced slicing (start\:stop\:step)     |
# | `enumerate(lst)`    | Returns index and value in a loop        |
# | `zip(list1, list2)` | Combines two lists into a list of tuples |

 

 
