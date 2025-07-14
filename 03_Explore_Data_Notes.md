# 📊 Notes: Exploring Data in Pandas

## 🧠 Why Explore Data?
Exploring data helps understand what the dataset contains before cleaning or analyzing it.

### ✅ Functions Learned:
- `.head(n)` → Shows first n rows
- `.tail(n)` → Shows last n rows
- `.info()` → Overview of columns, datatypes, nulls
- `.shape` → (rows, columns)
- `.columns` → List of all column names
- `.dtypes` → Data types of columns
- `.isnull().sum()` → Number of missing values per column
- `.describe()` → Summary stats (mean, std, etc.)

### 🚨 Realizations:
- Large datasets can’t be fully printed, so preview with `.head()` is best.
- `.info()` is super useful to quickly spot missing/null values.
- Summary stats help you know if data is skewed, has outliers, etc.

---

### 🔖 Learning Tip:
Before analysis — **always explore your data**. Understand structure before cleaning.
