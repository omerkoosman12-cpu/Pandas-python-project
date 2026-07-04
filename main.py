import pandas as pd

# Read CSV files
employees = pd.read_csv("employees.csv")
attendance = pd.read_csv("attendance.csv")

# 1. Display only the employees working in the HR department.
print("1. HR Employees")
print(employees[employees["Department"] == "HR"])

# 2. Display employees whose Salary is greater than 50000.
print("\n2. Salary > 50000")
print(employees[employees["Salary"] > 50000]) 

# 3. Display employees who belong to Delhi.
print("\n3. Employees from Delhi")
print(employees[employees["City"] == "Delhi"])

# 4. Display employees who belong to Mohali and have Experience greater than 2 years.
print("\n4. Mohali employees with Experience > 2")
print(employees[(employees["City"] == "Mohali") & (employees["Experience"] > 2)])

# 5. Sort the employees according to Salary in descending order.
print("\n5. Salary Descending")
print(employees.sort_values(by="Salary", ascending=False))

# 6. Sort the employees according to Experience in ascending order.
print("\n6. Experience Ascending")
print(employees.sort_values(by="Experience"))

# 7. Find the average salary of each department.
print("\n7. Average Salary")
print(employees.groupby("Department")["Salary"].mean())

# 8. Find the maximum salary in each department.
print("\n8. Maximum Salary")
print(employees.groupby("Department")["Salary"].max())

# 9. Find the minimum salary in each department.
print("\n9. Minimum Salary")
print(employees.groupby("Department")["Salary"].min())

# 10. Find the total salary of employees department-wise.
print("\n10. Total Salary")
print(employees.groupby("Department")["Salary"].sum())

# 11. Count the number of employees in each city.
print("\n11. Employees in Each City")
print(employees.groupby("City").size())

# 12. Display the number of missing values in each column.
print("\n12. Missing Values")
print(employees.isnull().sum())

# 13. Replace the missing salary with 0.
employees["Salary"] = employees["Salary"].fillna(0)
print("\n13. Salary after replacing missing values")
print(employees)

# 14. Merge the employees.csv and attendance.csv files.
merged = pd.merge(employees, attendance, on="EmpID")
print("\n14. Merged Data")
print(merged)

# 15. Display only those employees whose Attendance is "Present".
print("\n15. Present Employees")
print(merged[merged["Attendance"] == "Present"])