import pandas as pd
import numpy as np

data = {
    "Month": ["January", "February", "March",
              "April", "May", "June"],
    "Sales": [45000, 52000, 48000, 60000, 75000, 68000]
}

df = pd.DataFrame(data)

print("===== MONTHLY SALES =====")
print(df)

# NumPy calculations
total = np.sum(df["Sales"])
average = np.mean(df["Sales"])
maximum = np.max(df["Sales"])
minimum = np.min(df["Sales"])

# Find months
best_month = df.loc[df["Sales"].idxmax(), "Month"]
worst_month = df.loc[df["Sales"].idxmin(), "Month"]

print("\n===== SALES ANALYSIS =====")
print("Total Sales:", total)
print("Average Sales:", average)
print("Highest Sales:", maximum)
print("Lowest Sales:", minimum)
print("Best Month:", best_month)
print("Lowest Sales Month:", worst_month)