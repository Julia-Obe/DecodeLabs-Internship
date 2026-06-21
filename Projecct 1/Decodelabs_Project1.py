# importing Library
import pandas as pd

# Loading the dataset
df = pd.read_excel("C:/Users/USER/Desktop/AYABA New/DecodeLabs/Dataset for Data Analytics.xlsx")

# Viewing the first five rows
df.head()

# Dataset info
df.info()

# Checking the number of missing cells
df.isnull().sum()

# Filling Missing Cells
df["CouponCode"] = df["CouponCode"].fillna("NULL")

# Verifying No more missing Cells
df.isnull().sum()

# Checking for duplicated with Order ID column
duplicates = df[df.duplicated(subset=["OrderID"])]
print(duplicates)

# Counting the number of duplicates
df["OrderID"].duplicated().sum()

# Deleting duplicates
df = df.drop_duplicates()

# Changed DateTime column title to Date and ensuring it
df["Date"] = pd.to_datetime(df["Date"])

# Splitting the time component into a new 'Time' column before 'Date' is converted to a string.
df["Time"] = df["Date"].dt.time

# Convert the 'Date' column to a string format as seemingly intended.
df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")

# Trimming spaces and cleaning text
text_columns = ["Product", "PaymentMethod", "OrderStatus", "ReferralSource"]
for col in text_columns:
  df[col] = df[col].str.strip()
  df[col] = df[col].str.replace(r'\s+', ' ', regex=True)
  df[col] = df[col].str.title()

# Verifying Dataset
df.info()
df.head()
df.isnull().sum()
df["OrderID"].duplicated().sum()


