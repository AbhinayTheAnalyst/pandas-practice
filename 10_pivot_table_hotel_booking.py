'''
🧠 Pivot Table Practice using Pandas – by Abhinay

📌 Topic: Learn how to summarize large datasets using pivot tables in Python (just like Excel)
📁 Real-world example: Hotel booking data

✅ Why Pivot Table?
When data becomes large (like 1000+ rows), we can't understand trends just by reading.
Pivot tables help in summarizing data — e.g., monthly guest count, total revenue per hotel.

🎯 What You Will Learn:
- Creating pivot tables in pandas
- Summarizing values (Guests, Revenue)
- Adding total rows & columns
- Real insights for business decision
'''

# 🔃 Step 1: Import Pandas
import pandas as pd

# 📊 Step 2: Create sample hotel data
data = {
    'Hotel': ['Resort Hotel', 'City Hotel', 'Resort Hotel', 'City Hotel', 'City Hotel'],
    'Month': ['January', 'January', 'February', 'February', 'March'],
    'Guests': [100, 120, 90, 130, 110],
    'Revenue': [50000, 60000, 45000, 65000, 55000]
}

# ✅ Creating a DataFrame from dictionary
df = pd.DataFrame(data)
print("📋 Original Dataset:\n")
print(df)

'''
📍 We want to answer:
1. Har hotel mein kis month mein kitne guest aaye?
2. Har hotel ne kis month mein kitna revenue kamaya?
3. Kis month mein demand high/low thi?
'''

# 🔁 Step 3: Create Pivot Table
pivot_df = pd.pivot_table(df,
                          index='Hotel',            # Group by Hotel
                          columns='Month',          # Split columns by Month
                          values=['Guests', 'Revenue'],  # What to summarize
                          aggfunc='sum',            # Aggregation function
                          fill_value=0              # If data not present, show 0
                         )

print("\n📊 Pivot Table (Guests and Revenue per Hotel per Month):\n")
print(pivot_df)

# ✅ Step 4: Add total for each hotel (row-wise)
pivot_df['Total Guests'] = pivot_df['Guests'].sum(axis=1)
pivot_df['Total Revenue'] = pivot_df['Revenue'].sum(axis=1)

# ✅ Step 5: Add total for all hotels (column-wise)
pivot_df.loc['All Hotels Total'] = pivot_df.sum(numeric_only=True)

print("\n📈 Pivot Table with Totals (Row & Column):\n")
print(pivot_df)

'''
📌 Insights You Can Get:
- "City Hotel" had more guests in February than "Resort Hotel"
- March bookings happened only in City Hotel
- Resort Hotel earned ₹45,000 in Feb, ₹50,000 in Jan
'''

# 🎯 Summary:
# Pivot table is great when you want to:
# - Analyze large dataset (sales, bookings, students, etc.)
# - Create report for managers
# - Find trends easily (e.g., which month had most sales?)
# - Group and summarize automatically

# 💬 Personal Note (by Abhinay):
# I understood pivot table better by this practice. It's like Excel ka superpower in Python.
# I'll use it in my real projects like hotel booking, product sales, school analysis etc.
# Practice se confidence badh raha hai 😇

# 📍 Next Topics:
# → Compare DataFrames
# → Advanced Joins
# → Creating Dashboards (Excel + Python)
