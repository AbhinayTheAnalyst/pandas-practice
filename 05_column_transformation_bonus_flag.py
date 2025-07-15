# 🧾 Column Transformation in Pandas — Bonus Flag Logic
# -----------------------------------------------
# 🎯 GOAL: Based on the "bonus %" column, create a new column "get_bonus"
# If bonus % is 0 → write "No Bonus"
# If bonus % > 0 → write "Bonus"

import pandas as pd

# ✅ Step 1: Create a sample DataFrame
data = {
    'employee': ['Abhinay', 'Radha', 'Sita', 'Rohan', 'Geeta'],
    'salary': [30000, 45000, 50000, 25000, 40000],
    'bonus %': [0, 10, 0, 5, 15]
}

df = pd.DataFrame(data)

# ✅ Step 2: Check original data
print("🔹 Original DataFrame:")
print(df)

# ✅ Step 3: Add a new column 'get_bonus' using conditional logic
# 🧠 Using .loc[] to apply condition row-wise
df.loc[df['bonus %'] == 0, 'get_bonus'] = 'No Bonus'
df.loc[df['bonus %'] > 0, 'get_bonus'] = 'Bonus'

# ✅ Step 4: Show the transformed DataFrame
print("\n✅ After Column Transformation:")
print(df)

# -----------------------------------------------
# 🧠 Explanation:
# - We used df.loc[condition, 'new_column'] = value
# - It's very useful for adding flags or labeling rows based on existing data
# - This helps in creating filters, dashboards, and insights
# -----------------------------------------------

"""
Output:

  employee  salary  bonus %  get_bonus
0  Abhinay   30000        0  No Bonus
1    Radha   45000       10     Bonus
2     Sita   50000        0  No Bonus
3    Rohan   25000        5     Bonus
4    Geeta   40000       15     Bonus
"""

# ✅ Bonus Tip:
# Always use descriptive column names like 'bonus_percent' to avoid confusion
# 'bonus %' is valid but may confuse with modulus operator %

# 🚀 This small transformation shows real-world logic building — like flagging, filtering, and segmenting data.

# 🧠 Column Transformation in Pandas – Name, Percentage, and Month Extraction
# ------------------------------------------------------------------------
# 👨‍💻 By AbhinayTheAnalyst – Hands-on Data Transformation Practice

import pandas as pd

# ✅ Step 1: Create a sample DataFrame
data = {
    'first_name': ['Abhinay', 'Radha', 'Sita', 'Rohan'],
    'last_name': ['Kumar', 'Sharma', 'Devi', 'Roy'],
    'salary': [30000, 45000, 50000, 40000],
    'month': ['January', 'February', 'March', 'April']
}

df = pd.DataFrame(data)

print("🔹 Original Data:")
print(df)

# ✅ Step 2: Combine first and last name to create 'full_name'
# Also applying string functions: .str.upper(), .lower(), .capitalize()
df['full_name'] = df['first_name'].str.upper() + '_' + df['last_name'].str.capitalize()

# ✅ Optional: You can also create lowercase or capitalized versions
df['full_name_lower'] = df['first_name'].str.lower() + '_' + df['last_name'].str.lower()
df['full_name_cap'] = df['first_name'].str.capitalize() + ' ' + df['last_name'].str.capitalize()

# ✅ Step 3: Calculate 20% of salary
df['20_percent_salary'] = (df['salary'] / 100) * 20

# ✅ Step 4: Extract short month name from 'month' column
def extract(value):
    return value[0:3]  # first 3 letters

df['short_month'] = df['month'].map(extract)

# ✅ Final Output
print("\n✅ Transformed Data:")
print(df)

# ------------------------------------------------------------------------
# 📌 What You Learned:
# - String manipulation with .str.upper(), .lower(), .capitalize()
# - Column creation using mathematical operations
# - Using .map() with a custom function to extract partial string
# - How to create multiple transformed views from one dataset
# ------------------------------------------------------------------------

"""
📊 Sample Output:

  first_name last_name  salary     month       full_name     full_name_lower     full_name_cap  20_percent_salary short_month
0    Abhinay     Kumar   30000   January   ABHINAY_Kumar     abhinay_kumar     Abhinay Kumar         6000.0           Jan
1      Radha    Sharma   45000  February   RADHA_Sharma     radha_sharma     Radha Sharma         9000.0           Feb
2       Sita      Devi   50000     March     SITA_Devi       sita_devi       Sita Devi            10000.0          Mar
3      Rohan       Roy   40000     April     ROHAN_Roy        rohan_roy        Rohan Roy           8000.0           Apr
"""
"""
✅ Ab Kya Sikha:

✅ String methods in Pandas

✅ Custom function with .map()

✅ Mathematical transformation on columns

✅ Proper column naming and readability
"""


# ✅ Tip for Job Interviews:
# Such transformations are very common in data cleaning before visualization or ML model building.
# Adding logic like name formatting, percentage calculation, and month short-form helps in real-world dashboards & reports.
