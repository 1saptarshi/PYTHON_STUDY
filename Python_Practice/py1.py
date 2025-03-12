employee_data = {}

num_employees = int(input("Enter the number of employees: "))

for i in range(num_employees):
    name = input(f"Enter name of employee {i + 1}: ")
    salary = float(input(f"Enter salary of {name}: "))
    employee_data[name] = salary

print("\nEmployee Salary Data:",employee_data)