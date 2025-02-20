# 1. Arithmetic Operators
# These are used for mathematical calculations.

# Operator	Description	Example
# +	Addition	5 + 3 = 8
# -	Subtraction	5 - 3 = 2
# *	Multiplication	5 * 3 = 15
# /	Division	5 / 2 = 2.5
# //	Floor Division (Removes decimal)	5 // 2 = 2
# %	Modulus (Remainder)	5 % 2 = 1
# **	Exponentiation (Power)	5 ** 3 = 125
 
a = 10
b = 3

print("Addition:", a + b)       # 13
print("Subtraction:", a - b)    # 7
print("Multiplication:", a * b) # 30
print("Division:", a / b)       # 3.3333
print("Floor Division:", a // b) # 3
print("Modulus:", a % b)        # 1
print("Exponentiation:", a ** b) # 1000

# 2. Assignment Operators

# Used to assign values to variables.

# Operator	Example	Equivalent To
# =	x = 5	x = 5
# +=	x += 3	x = x + 3
# -=	x -= 3	x = x - 3
# *=	x *= 3	x = x * 3
# /=	x /= 3	x = x / 3
# //=	x //= 3	x = x // 3
# %=	x %= 3	x = x % 3
# **=	x **= 3	x = x ** 3
 
x = 10
x += 5  # x = x + 5
print(x)  # 15

# 3. Comparison (Relational) Operators
# Used to compare values and return True or False.

# Operator	Description	Example
# ==	Equal to	5 == 5 → True
# !=	Not equal to	5 != 3 → True
# >	Greater than	5 > 3 → True
# <	Less than	5 < 3 → False
# >=	Greater than or equal to	5 >= 5 → True
# <=	Less than or equal to	3 <= 5 → True
 
a = 10
b = 5

print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False

# 4. Logical Operators
# Used for boolean logic operations.

# Operator	Description	Example
# and	True if both conditions are true	(5 > 3) and (10 > 2) → True
# or	True if at least one condition is true	(5 < 3) or (10 > 2) → True
# not	Reverses boolean value	not (5 > 3) → False
 
x = 10
y = 5

print((x > 5) and (y < 10))  # True
print((x > 10) or (y < 10))  # True
print(not(x > 5))  # False

# 5. Bitwise Operators

# Used to perform operations at the binary level.

# Operator	Description	Example
# &	AND	5 & 3 → 1
# `	`	OR
# ^	XOR	5 ^ 3 → 6
# ~	NOT	~5 → -6
# <<	Left Shift	5 << 1 → 10
# >>	Right Shift	5 >> 1 → 2
 
a = 5  # 0101 in binary
b = 3  # 0011 in binary

print(a & b)  # 1 (0001 in binary)
print(a | b)  # 7 (0111 in binary)
print(a ^ b)  # 6 (0110 in binary)
print(~a)     # -6 (inverts bits)
print(a << 1) # 10 (Shifts left)
print(a >> 1) # 2 (Shifts right)

# 6. Membership Operators

# Used to check if a value is in a sequence.

# Operator	Description	Example
# in	Returns True if value is in sequence	"a" in "apple" → True
# not in	Returns True if value is not in sequence	"z" not in "apple" → True
 
text = "Python"

print("y" in text)   # True
print("z" not in text) # True

# 7. Identity Operators

# Used to compare memory locations of objects.

# Operator	Description	Example
# is	Returns True if both variables refer to the same object	a is b
# is not	Returns True if both variables do not refer to the same object	a is not b
 
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)   # True (b is assigned same memory as a)
print(a is c)   # False (c is a different object)
print(a == c)   # True (values are equal)