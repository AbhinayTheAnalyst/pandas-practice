'''
🧠 Pandas Real World Summary Project
🔰 Created by: Abhinay (Self-Taught Analyst)
🎯 Goal: Revise and Understand All Pandas Concepts Through Practical Code
'''

import pandas as pd
import numpy as np

# --------------------------------------
# 1️⃣ Create Sample Real-World Dataset
# --------------------------------------

data = {
    'EmpID': [101, 102, 103, 104, 105, 101],
    'Name': ['Golu', 'Radha', 'Sita', 'Rohan', 'Mohan', 'Golu'],
    'Department': ['HR', 'IT', 'HR', 'Sales', 'Sales', 'HR'],
    'Gender': ['M', 'F', 'F', 'M', 'M', 'M'],
    'Salary': [30000, 50000, np.nan, 45000, 47000, 30000],
    'Bonus %': [0, 10, 15, 0, 5, 0]
}

df = pd.DataFrame(data)
print("📊 Sample Employee Dataset:")
print(df)

# --------------------------------------
# 2️⃣ Handle Duplicate Values
# --------------------------------------
print("\n🚨 Duplicate Rows:")
print(df.duplicated())

df = df.drop_duplicates()
print("\n✅ After Removing Duplicates:")
print(df)

# --------------------------------------
# 3️⃣ Handle Missing (Null) Values
# --------------------------------------
print("\n🔍 Missing Values:")
print(df.isnull().sum())

# Fill missing salary with average
avg_salary = df["Salary"].mean()
df["Salary"] = df["Salary"].fillna(avg_salary)

print("\n✅ Salary Filled with Mean:")
print(df)

# --------------------------------------
# 4️⃣ Column Transformation
# --------------------------------------

# Create full name (uppercase) — real use: data formatting
df["FullName"] = df["Name"].str.upper() + "_" + df["Department"]

# Create Bonus column with logic
df["Get_Bonus"] = df["Bonus %"].apply(lambda x: "No Bonus" if x == 0 else "Bonus")

# Calculate actual bonus amount (assuming bonus is % of salary)
df["Bonus_Amount"] = (df["Salary"] * df["Bonus %"]) / 100

print("\n🔁 Transformed DataFrame:")
print(df.head())

# --------------------------------------
# 5️⃣ Group By & Aggregation
# --------------------------------------

# Count of employees in each department
dept_count = df.groupby("Department").agg({"EmpID": "count"})
print("\n📦 Department-wise Employee Count:")
print(dept_count)

# Avg salary by gender & department
group_summary = df.groupby(["Department", "Gender"]).agg({
    "Salary": "mean",
    "Bonus_Amount": "sum"
})
print("\n💼 Group Summary (Avg Salary & Total Bonus):")
print(group_summary)

# --------------------------------------
# 6️⃣ Merge Two Datasets
# --------------------------------------

# Example: Another dataset with Employee joining year
join_data = {
    'EmpID': [101, 102, 103, 104, 105],
    'JoinYear': [2020, 2021, 2020, 2019, 2022]
}
df_join = pd.DataFrame(join_data)

# Merge based on EmpID
merged = pd.merge(df, df_join, on='EmpID', how='left')
print("\n🔗 Merged Dataset with JoinYear:")
print(merged)

# --------------------------------------
# 7️⃣ Compare Two DataFrames
# --------------------------------------

# Create a modified version
df_copy = df.copy()
df_copy.loc[0, "Salary"] = 35000

# Compare changes
comparison = df.compare(df_copy, keep_shape=True, keep_equal=False)
print("\n🆚 Comparison with Modified Copy:")
print(comparison)

# --------------------------------------
# 8️⃣ Pivot Table (Wide Format Summary)
# --------------------------------------

pivot = pd.pivot_table(df, index="Department", values="Salary", aggfunc="mean")
print("\n📊 Pivot Table - Avg Salary per Department:")
print(pivot)

# --------------------------------------
# 9️⃣ Melting (Wide ➝ Long Format)
# --------------------------------------

# Example: Student Marks Wide Format
marks = pd.DataFrame({
    'Student': ['Golu', 'Radha'],
    'Math': [85, 78],
    'Science': [90, 82],
    'English': [88, 85]
})

melted = pd.melt(marks, id_vars=['Student'], var_name='Subject', value_name='Marks')
print("\n🔥 Melted Format (Subject-wise Marks):")
print(melted)
