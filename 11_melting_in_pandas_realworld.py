'''
🔥 Pandas Melting - Real World Use Case
👨‍💻 By: Abhinay (Self-Taught Data Analyst)
📌 Notes: Jab maine ye topic first time padha, toh honestly thoda confusing laga. 
         Par jab real-world ka example dekha, tab clarity aayi. So yeh file banayi — revise karne ke liye bhi kaam aaye.

🧠 Melting kya hai?
Wide format data (jisme multiple columns hoti hain) ko ek long format me convert karna. 
Ye helpful hota hai jab subject-wise, month-wise ya kisi aur category-wise analysis karna hota hai.

✅ Real Life Example: Student Report Card
'''

import pandas as pd

# 📋 Original Wide Format Data (as we often see in Excel)
marks_df = pd.DataFrame({
    'Student': ['Golu', 'Radha', 'Sita'],
    'Math': [85, 78, 92],
    'Science': [90, 82, 88],
    'English': [88, 85, 91]
})

print("📋 Original Wide Format Data:")
print(marks_df)

'''
Jab mujhe is format me data mila tha, toh initially samajh nahi aaya ki 
subject-wise kis student ka kya score hai usko kaise easily group karu analysis ke liye.
Fir melting use kiya aur sab kuch sorted ho gaya!
'''

# 🔁 Melting the data — converting wide to long
melted_df = pd.melt(
    marks_df,
    id_vars=['Student'],       # Ye woh column hai jo same rahega
    var_name='Subject',        # New column jisme previous column headers (Math, Science...) aa jaayenge
    value_name='Marks'         # New column jisme values (85, 78...) aa jaayenge
)

print("\n🔥 Melted Long Format Data:")
print(melted_df)

'''
👁️ Real-World Use:
Jab analysis karte hain, maan lo kisi coaching institute me:
→ Subject-wise toppers dekhna hai
→ Kis student ka kis subject me strength ya weakness hai

Tab melted format me data jyada helpful hota hai — visualization, groupby, pivot sab ke liye.

✅ Next Step:
Is melted format ka use pivot table, groupby me hota hai — jise hum analysis aur dashboard me use karte hain.
'''

# ✅ Optional: Groupby to find average marks per subject
subject_avg = melted_df.groupby("Subject")["Marks"].mean()
print("\n📊 Subject-wise Average Marks:")
print(subject_avg)
