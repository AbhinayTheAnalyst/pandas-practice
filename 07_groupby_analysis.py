# 🐼 GROUPBY IN PANDAS
# ----------------------------------------------
# 🔍 Jab humare paas bada dataset ho aur humein group-wise data samajhna ho
# jaise department-wise ya country-wise salary, tab groupby function ka use hota hai.

import pandas as pd

# Sample DataFrame banate hain job-wise analysis ke liye
data = pd.DataFrame({
    'EEID': [101, 102, 103, 104, 105, 106, 107],
    'Name': ['Abhinay', 'Radha', 'Rohan', 'Simran', 'Ali', 'John', 'Zara'],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female'],
    'Department': ['HR', 'IT', 'HR', 'IT', 'Finance', 'Finance', 'HR'],
    'Country': ['India', 'India', 'USA', 'USA', 'India', 'USA', 'India'],
    'Age': [24, 22, 23, 26, 29, 28, 30],
    'Max_Salary': [40000, 45000, 50000, 47000, 52000, 55000, 49000]
})

# ✅ Example 1: Department-wise Gender Count (kitne male/female ek dept me hain)
gb1 = data.groupby("Department").agg({"Gender": "count"})
print("\n🔹 Department-wise Gender Count:\n", gb1)

# ✅ Example 2: Department aur Gender-wise EEID Count (kitne log kis gender se hain har dept me)
gb2 = data.groupby(["Department", "Gender"]).agg({"EEID": "count"})
print("\n🔹 Department & Gender-wise Employee Count:\n", gb2)

# ✅ Example 3: Country-wise Max Salary Analysis
gb3 = data.groupby("Country").agg({"Max_Salary": "max"})
print("\n🔹 Country-wise Maximum Salary:\n", gb3)

# ✅ Example 4: Country & Gender-wise Max Salary and Min Age
gb4 = data.groupby(["Country", "Gender"]).agg({
    "Max_Salary": "max",
    "Age": "min"
})
print("\n🔹 Country & Gender-wise Max Salary and Min Age:\n", gb4)

# ----------------------------------------------
# 🤔 WHY GROUPBY MATTERS:
# Bada data direct samajhna mushkil hota hai,
# isliye GroupBy se hum data ko summarize kar paate hain,
# aur business decisions ke liye insights nikaal paate hain.

"""
🧠 Notes:
- "groupby" ke baad hamesha "agg()" use hota hai, jo aggregation function lagata hai (sum, count, mean, max etc).
- Tum ek ya ek se zyada column pe grouping kar sakte ho.
- Ye analysis real-world dashboards aur reports me bahut kaam aata hai.
"""

# ✅ TILL NOW:
# We have learned how to summarize big data smartly using groupby in Pandas.

print("\n✅ GroupBy Analysis Completed.")
