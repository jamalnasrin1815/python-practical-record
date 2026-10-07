import pandas as pd
import numpy as np

data = {
    "Product": [
        "Laptop", "Phone", "Tablet",
        "Laptop", "Phone", "Tablet"
    ],
    "Quantity": [2, 5, 3, 4, 6, 5],
    "Price": [50000, 20000, 15000, 50000, 20000, 15000]
}

df = pd.DataFrame(data)

# Calculate revenue
df["Revenue"] = df["Quantity"] * df["Price"]

print("===== SALES DATA =====")
print(df)

# Product-wise analysis
product_sales = df.groupby("Product")["Revenue"].sum()

print("\n===== PRODUCT-WISE SALES =====")
print(product_sales)

# Find best-selling product
best_product = product_sales.idxmax()
highest_sales = product_sales.max()

print("\nBest Selling Product:", best_product)
print("Highest Revenue:", highest_sales)