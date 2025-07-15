# ---------------------------------------------
# 📁 04_handling_duplicates_value.py
# 🧠 Topic: How to detect and remove duplicate rows in Pandas
# ✍️ Written by: Abhinay (GitHub: AbhinayTheAnalyst)
# ---------------------------------------------

import pandas as pd

# ✅ Sample DataFrame with duplicate values
data = {
    'id': [101, 102, 103, 104, 102, 105, 103],
    'name': ['Radha', 'Sita', 'Golu', 'Rohan', 'Sita', 'Mohan', 'Golu'],
    'city': ['Patna', 'Delhi', 'Ranchi', 'Kolkata', 'Delhi', 'Bhopal', 'Ranchi']
}

df = pd.DataFrame(data)

print("🔹 Original DataFrame:")
print(df)

# ✅ Check for duplicate rows (based on all columns)
print("\n🔍 Duplicate Rows (all columns):")
print(df.duplicated())

# ✅ Count total duplicates in entire DataFrame
print("\n📊 Total duplicate rows (all columns):")
print(df.duplicated().sum())

# ✅ Check for duplicates based on a specific column (e.g. 'id')
print("\n🔍 Duplicates based only on 'id' column:")
print(df['id'].duplicated())

print("\n📊 Total duplicates in 'id' column:")
print(df['id'].duplicated().sum())

# ✅ Remove duplicates (keep='first' by default)
df_cleaned = df.drop_duplicates()

print("\n✅ DataFrame after dropping duplicates:")
print(df_cleaned)

# ✅ If you want to drop duplicates based on a specific column
df_id_cleaned = df.drop_duplicates(subset='id')

print("\n✅ DataFrame after dropping duplicates from 'id' column:")
print(df_id_cleaned)
