'''
📊 09_Compare DataFrames in Pandas
Author: AbhinayTheAnalyst
Learning Mode: YouTube + ChatGPT + Real Practice

🔍 Why Compare DataFrames?
When you have two versions of a dataset — maybe original and modified —
comparison helps you:
✔️ Identify what's changed
✔️ Validate data processing
✔️ Debug mismatches in reporting

Pandas makes this super easy using: ✅ `DataFrame.compare()`

🔥 Let's learn step-by-step with our own fruit market example.
'''

import pandas as pd

# ✅ Create original DataFrame (df1)
data = {
    'Fruit': ['Apple', 'Banana', 'Orange', 'Mango', 'Grapes'],
    'Quantity': [100, 150, 120, 130, 160],
    'Price': [50, 30, 40, 60, 90]
}

df1 = pd.DataFrame(data)
print("📦 Original DataFrame (df1):")
print(df1)

# ✅ Create a copy of df1 and modify some values (df2)
df2 = df1.copy()

# Changing some prices and quantities
df2.loc[0, 'Price'] = 55
df2.loc[1, 'Price'] = 35
df2.loc[2, 'Price'] = 42

df2.loc[0, 'Quantity'] = 120
df2.loc[1, 'Quantity'] = 125
df2.loc[2, 'Quantity'] = 140

print("\n🛠️ Modified DataFrame (df2):")
print(df2)

# ✅ Compare df1 and df2 (default behavior – only differences)
comparison = df1.compare(df2)
print("\n🔍 Comparison (Only differences shown):")
print(comparison)

# ✅ Compare with keep_shape=True to keep all rows
comparison_keep_shape = df1.compare(df2, keep_shape=True)
print("\n🔍 Comparison (Keep shape = True):")
print(comparison_keep_shape)

# ✅ Compare with keep_equal=True to also show equal values
comparison_all = df1.compare(df2, keep_shape=True, keep_equal=True)
print("\n🔍 Full Comparison (Keep equal = True):")
print(comparison_all)

'''
🧠 Learning Summary:
- df1.compare(df2) → Shows only differences
- keep_shape=True → Keeps full shape (same number of rows), but unmatched rows as NaN
- keep_equal=True → Shows even equal values (useful for full audit)

🎯 Real-World Tip:
Always compare two DataFrames after cleaning, transformation, or merging to check what’s affected.

✍️ Personal Note:
Pehle lagta tha compare sirf testing wale karte hain, par ab samajh gaya hoon ki analyst ko bhi kaafi kaam padta hai.
'''
