As we all ready know:
A DataFrame is like a 2D table (Excel-style) in Python
# It stores data in rows and columns

import pandas as pd
# ✅ Create DataFrame using dictionary
data_dict = {
    'Name': ['Abhinay', 'Radha', 'Rohan'],
    'Age': [21, 22, 23],       
df1 = pd.DataFrame(data_dict)# All lists must have the same length, otherwise it will throw an error.
print("✅ DataFrame from dictionary:")
print(df1)

# ✅ Create DataFrame using list of lists
data_list = [
    ['Abhinay', 21, 'Patna'],
    ['Radha', 22, 'Delhi'],
    ['Rohan', 23, 'Mumbai']
]

columns = ['Name', 'Age', 'City']
df2 = pd.DataFrame(data_list, columns=columns)
print("\n✅ DataFrame from list of lists:")
print(df2)

# ✅ Create empty DataFrame (if needed)
df_empty = pd.DataFrame()
print("\n✅ Empty DataFrame:")
print(df_empty)

'''
'''
Note: In real-world data analysis, we usually work with CSV, Excel, or databases —
but it's still important to know how to create DataFrames manually.
'''
"""
NOW WE FINALLY LEARNED HOW TO CREATE DATAFRAMES 🤓  
We’ll meet again in the next part of the series...  
Till then, haste raho, muskurate raho 😁
"""
