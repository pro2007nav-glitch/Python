import pandas as pds
import matplotlib.pyplot as plt

# 1. Read employee details from CSV file
df = pd.read_csv("employee.csv")

# 2. Display employee names, departments, and salaries
print("Employee Details:")
print(df[["Name", "Department", "Salary"]])

# 3. Calculate average salary for each department
avg_salary = df.groupby("Department")["Salary"].mean()

print("\nAverage Salary for Each Department:")
print(avg_salary)

# Plot average salary by department
avg_salary.plot(kind="bar", color="skyblue")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
