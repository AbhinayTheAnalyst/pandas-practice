# ---------------------------------------------------------------
# 📁 05_handling_missing_values.py
# 🧠 Topic: How to detect and handle missing/null values in Pandas
# ✍️ By: AbhinayTheAnalyst (Learning & growing, one step at a time)
# ---------------------------------------------------------------

import pandas as pd
import numpy as np

# ✅ Sample DataFrame with missing (NaN) values
data = {
    'name': ['Radha', 'Sita', 'Golu', np.nan, 'Rohan'],
    'gender': ['F', np.nan, 'M', 'M', 'M'],
    'age': [22, 21, np.nan, 23, 24],
    'salary': [35000, 42000, 30000, np.nan, np.nan]
}

df = pd.DataFrame(data)
print("🔹 Original DataFrame with NaN values:")
print(df)

# ✅ Check where values are null — gives True/False
print("\n🔍 Is Null (True where value is NaN):")
print(df.isnull())

# ✅ Count of null values in each column
print("\n📊 Total Null Values per Column:")
print(df.isnull().sum())

# ✅ Drop all rows that have any null value
print("\n🗑️ Drop rows with any NaN values (useful in some cases):")
print(df.dropna())

# 🧠 Realization:
# Suppose we are calculating total salary and a row has missing gender or name, 
# dropping the row might make sense — but only if it doesn't affect business logic.

# ❌ Not always good to drop rows — better to fill them in many cases.

# ✅ Replace all NaN values with a fixed value — Not always recommended
print("\n⚠️ Replace all NaNs with 'hii' (for demonstration only):")
print(df.replace(np.nan, 'hii'))

# ✅ Better: Replace NaN in a specific column like 'salary' with fixed value
df['salary'] = df['salary'].replace(np.nan, 30000)
print("\n💰 Replaced NaN in salary with 30000:")
print(df)

# ✅ Use mean to fill missing values
salary_mean = df['salary'].mean()
df['salary'] = df['salary'].replace(np.nan, salary_mean)
print("\n📈 Replaced NaN in salary with mean:", salary_mean)

# ✅ Fill missing values using method = 'bfill' (backward fill)
print("\n🔁 Fill NaN using Backward Fill:")
print(df.fillna(method='bfill'))

# ✅ Fill missing values using method = 'ffill' (forward fill)
print("\n🔁 Fill NaN using Forward Fill:")
print(df.fillna(method='ffill'))

# 🧠 Summary:
# 👉 Drop if nulls affect result badly (like total salary)
# 👉 Replace with logic: fixed value, mean, median, mode
# 👉 Or use smart fill techniques: ffill, bfill

'''
✅ Covered:
- Detecting missing values with `.isnull()`
- Counting nulls with `.sum()`
- Dropping rows using `.dropna()`
- Replacing nulls with static values, column mean
- Using `ffill` (forward fill) and `bfill` (backward fill)

🧠 Realizations:
- NaN doesn’t always mean "error" — sometimes, it means "decision point"
- It’s not always smart to drop rows — sometimes filling is smarter
- Clean data = Better insights = Smarter decisions

🚀 Slowly but steadily learning each piece of Pandas to be job-ready!
'''
