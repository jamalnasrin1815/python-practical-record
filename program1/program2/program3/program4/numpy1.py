import pandas as pd
import numpy as np

# Create sales data
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone"],
    "Quantity": [2, 5, 3, 4, 6],
    "Price": [50000, 20000, 15000, 50000, 20000]
}

df = pd.DataFrame(data)

# Calculate sales amount
df["Sales"] = df["Quantity"] * df["Price"]

print("===== SALES DATA =====")
print(df)

# Statistical calculations
total_sales = np.sum(df["Sales"])
average_sales = np.mean(df["Sales"])

print("\nTotal Sales:", total_sales)
print("Average Sales:", average_sales)