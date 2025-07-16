# 🧩 Merge, Join & Concatenate in Pandas
# Author: AbhinayTheAnalyst
# Learning Source: YouTube + ChatGPT + Real Practice
# ------------------------------------------------------------
# In real-world data analysis, we often combine multiple datasets.
# Let's explore: merge(), join(), and concat() with clear examples.

import pandas as pd

# ✅ Create two sample DataFrames with a common column: EmpID
df1 = pd.DataFrame({
    'EmpID': [101, 102, 103, 104],
    'Name': ['Radha', 'Krishna', 'Sita', 'Ram']
})

df2 = pd.DataFrame({
    'EmpID': [101, 103, 105],
    'Salary': [50000, 60000, 70000]
})

# ✅ MERGE (like SQL join on EmpID)
# Default is INNER JOIN – only common EmpIDs will be merged
merged_df_inner = pd.merge(df1, df2, on='EmpID')
print("🔗 Inner Merge (only matched EmpIDs):")
print(merged_df_inner)

# ✅ LEFT JOIN – all records from df1, matched from df2
merged_df_left = pd.merge(df1, df2, on='EmpID', how='left')
print("\n🔗 Left Merge (all from df1):")
print(merged_df_left)

# ✅ RIGHT JOIN – all records from df2, matched from df1
merged_df_right = pd.merge(df1, df2, on='EmpID', how='right')
print("\n🔗 Right Merge (all from df2):")
print(merged_df_right)

# ✅ OUTER JOIN – all records from both, with NaN where no match
merged_df_outer = pd.merge(df1, df2, on='EmpID', how='outer')
print("\n🔗 Outer Merge (all EmpIDs from both df1 & df2):")
print(merged_df_outer)

# ------------------------------------------------------------
# ✅ JOIN (works on index – not column by default)
df3 = df1.set_index('EmpID')
df4 = df2.set_index('EmpID')

joined_df = df3.join(df4, how='inner')
print("\n🧬 Join using index:")
print(joined_df)

# ------------------------------------------------------------
# ✅ CONCATENATION – Stack dataframes together (row-wise or column-wise)
df5 = pd.DataFrame({
    'EmpID': [201, 202],
    'Name': ['Lakshman', 'Hanuman']
})

# ROW-WISE CONCAT (axis=0) – like appending new records
concat_row = pd.concat([df1, df5], ignore_index=True)
print("\n📎 Concatenation (Row-wise):")
print(concat_row)

# COLUMN-WISE CONCAT (axis=1) – side-by-side columns
df6 = pd.DataFrame({
    'Department': ['HR', 'IT', 'Finance', 'Sales']
})
concat_col = pd.concat([df1, df6], axis=1)
print("\n📎 Concatenation (Column-wise):")
print(concat_col)

# ------------------------------------------------------------
# ✅ Realization:
# 🔸 Use merge() when you have a key column (like EmpID)
# 🔸 Use join() when your key is index-based
# 🔸 Use concat() when adding new rows or columns directly

"""
🎯 Personal Note (By Abhinay):
Pehle merge aur join ka farq samajhna mushkil laga,
lekin jab YouTube se example dekha, aur khud data banakar kiya,
tab clarity aayi. Real projects mein yeh sab bahut kaam aata hai.

Agar EmpID match nahi karta to NaN aa jata hai –
yeh ek sign hota hai ki ya to data incomplete hai,
ya uske cleaning ki jarurat hai.

Now I understand: combine karne ka kaam bhi ek data analyst ka kaafi important task hai.
"""
