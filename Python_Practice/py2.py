
n = int(input("Enter the number of elements: "))
numbers = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)
unique_elements = [num for num in numbers if numbers.count(num) == 1]
print("Elements with a single occurrence:", unique_elements)
