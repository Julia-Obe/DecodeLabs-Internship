# Importing Library
import pandas as pd

# Loading the cleaned dataset from project 1, handling blanks
df = pd.read_excel("C:/Users/USER/Desktop/AYABA New/DecodeLabs/Project 2/project_1_cleaned_dataset.xlsx", keep_default_na=False)

# Viewing the first five rows
df.head()

# Dataset information
df.info()

# The geometry of distribution
import matplotlib.pyplot as plt

df["TotalPrice"].hist(bins=20)
plt.title("Distribution of Total Price")
plt.xlabel("Total Price")
plt.ylabel("Frequency")
plt.show()

# Calculating average Total price
print(f"Average Total Price: {df["TotalPrice"].mean()}")

# Calculating the median price
print(f"Median Total Price: {df["TotalPrice"].median()}")

# Five-Number summary
summary = (df[["TotalPrice", "Quantity", "UnitPrice", "ItemsInCart"]].describe())
print(summary)
summary.to_excel("Descriptive_Statistics.xlsx")

# Unmasking the Outliers
df.boxplot(column= "TotalPrice")
plt.show()

# The Fingerprint of Variability
Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)

IQR = Q3 - Q1
print(IQR)

lower_bound = Q1 - 1.5 * IQR
print(lower_bound)

upper_bound = Q3 + 1.5 * IQR
print(upper_bound)

outliers = df[
    (df["TotalPrice"] < lower_bound) |
    (df["TotalPrice"] > upper_bound)
]

print(outliers)
print("Number of Outliers:", len(outliers))

# Correlation Analysis
correlation = df[["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]].corr()

import matplotlib.pyplot as plt

plt.imshow(correlation)
plt.colorbar()

plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=45)
plt.yticks(range(len(correlation.columns)), correlation.columns)

plt.title("Correlation Matrix")

plt.show()

correlation.to_excel("Correlation_Matrix.xlsx")
